import os, cv2
import numpy as np

def img_bulk_read_cv2(path,format=".png"):
    os.chdir(path)
    all_files = os.listdir(path)
    file_names = [i for i in all_files if i.endswith(format)]
    png_files = [cv2.imread(i) for i in file_names]
    return file_names, png_files

def red_trace_generate(img_files, h, s, v):
    for i in img_files:
        img_hsv = cv2.cvtColor(i[0:600,:,:], cv2.COLOR_BGR2HSV)
        blur = cv2.blur(img_hsv,(3,3))
        h_165 = blur[:,:,0]> h[1]
        h_5 = blur[:,:,0]< h[0]
        h_5_165 = h_5|h_165
        s_100 = blur[:,:,1]>s
        v_90 = blur[:,:,2]>v
        yield h_5_165&s_100&v_90
    
def red_trace(fnames, png_files, h =[5, 165], s = 60, v = 90):
    binarized = []
    binarized_append = binarized.append
    kernel1 = np.ones((2,2),np.uint8)
    kernel2 = np.ones((15,15),np.uint8)
    for n,i in enumerate(red_trace_generate(png_files,h, s, v)):
        erosion = cv2.erode(np.array(i,dtype=np.uint8),kernel1,iterations = 1)
        img = cv2.dilate(erosion,kernel2,iterations = 1)
        binarized_append(img*255)
    return binarized

def img_to_center(img_dataframe):
    center_list = []
    cl_list = []
    cl_list_append = cl_list.append
    a = 0
    for i in img_dataframe:
        bin_img = np.array(i/255, dtype=np.uint8)
        imgEdge,contours,hierarchy = cv2.findContours(bin_img, 1, 2)
        cl = len(contours)
        cl_list_append(cl)
        if cl == 0:
            center_list.append(np.array([np.nan,np.nan]))
        elif cl == 1:
            cnt = contours[0]
            M = cv2.moments(cnt)
            center_list.append(np.array([int(M['m10']/M['m00']),int(M['m01']/M['m00'])]))
        else:
            try:
                try:
                    M_list = [cv2.moments(i) for i in contours]
                    center_list_tmp = [np.array([int(i['m10']/i['m00']),int(i['m01']/i['m00'])]) for i in M_list]
                    dist_array = np.array([np.linalg.norm(i - center_list[-1]) for i in center_list_tmp])
                    center_array_tmp = np.array(center_list_tmp)
                    center_array_tmp_list = center_array_tmp[np.where(dist_array == np.min(dist_array))].tolist()
                    center_list.append(np.array(*center_array_tmp_list))
                except:
                    center_list.append(np.array([int(M['m10']/M['m00']),int(M['m01']/M['m00'])]))
            except:
                center_list.append(np.array([np.nan,np.nan]))
    return center_list, np.array(cl_list)

def nan_processing(list1):
    array_copy = np.array([i.tolist() for i in list1])
    array_copy2 = array_copy.copy()
    for i,j in [(1,1),(1,2),(2,1),(1,3),(2,2),(3,1),
              (1,4),(4,1),(3,2),(2,3),(1,5),(5,1),(2,4),(4,2),(3,3)]:
        if (array_copy == array_copy).all():
            break
        else:
            array_right = np.roll(array_copy, i, axis=0)
            array_left = np.roll(array_copy, -j, axis=0)
            array_mean = (array_right*j + array_left*i)/(i+j)
            nan_position = np.where(array_copy != array_copy)[0]
            array_copy[nan_position] = array_mean[nan_position]
    if array_copy2[0][0] == array_copy2[0][0]:
        return array_copy - array_copy[0]
    else:
        return array_copy - np.median(array_copy[:10],axis=0)
    
def center_to_displacement(center_array):
    center_array2 = center_array
    center_list = center_array2.tolist()
    displacement_array_0 = np.array([np.linalg.norm(i) for i in center_list])
    return np.median(displacement_array_0) - displacement_array_0