#! /bin/bash
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color


VENV_NAME="venv"

# removing previous venv
venv_current_location=$PWD/$VENV_NAME
echo -e "${GREEAN}removing current venv from location: $venv_current_location"
rm -rf $venv_current_location

# create venv
echo -e "${GREEAN}creating venv"
$HOME/.local/bin/virtualenv -p /usr/bin/python3.6 $VENV_NAME

# activate
echo -e "${GREEAN}activating venv"
source $VENV_NAME/bin/activate

# instell requirements
echo -e "${GREEAN}installing dependencies"
pip install -r requirements.txt     

# # instell self-modules
# echo -e "${GREEAN}installing internal modules"
# pip install .  

# deactivate
echo -e "${GREEAN}Done! deactivating venv"
deactivate