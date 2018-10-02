STARTPATH=$PWD
cd
mkdir homebrew
curl -L https://github.com/Homebrew/homebrew/tarball/master | tar xz --strip 1 -C homebrew
echo 'export PATH="$HOME/homebrew/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
brew update
rm -rf /Users/AraVib/homebrew/share/doc/homebrew
brew update
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install anaconda3-5.2.0
pyenv rehash
cd $STARTPATH
pyenv local anaconda3-5.2.0
pip install msgpack
pip install --upgrade pip
pip install opencv-python
pip install jupyterlab
brew install ffmpeg
brew install imagemagick
