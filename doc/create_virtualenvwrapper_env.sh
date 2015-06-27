# If you use virtualenvwrapper, this script would help you create a new
# environment , configure it and install everything needed for development.

# To get this file running and the environment created run:
# $ . ./create_virtualenvwrapper_env.sh

PYTHON_EXEC=`which python2.7`
OLD_DIR=`pwd`

if [[ ! -f $PYTHON_EXEC ]]; then
    echo "Missing python2.7 binary required to run"
    exit 1
fi

mkvirtualenv gtv -p $PYTHON_EXEC -r requirements.txt 
pip install -r requirements.dev.txt
cd ..
add2virtualenv src
setvirtualenvproject $VIRTUAL_ENV $(pwd)
cd $OLD_DIR
deactivate

echo ""
echo ""
echo "Virtualenvironment created, helpful commands: "
echo " - workon gtv: will start the virtual environment and take you to the project dir."
echo " - deactivate : will get you out the virtual environment."
echo " - cdproject : will take you to the main repo directory while inside the virtual environment "
echo ""
echo ""
