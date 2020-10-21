#!/bin/bash

# We checking for python module dependency

#NUM="$( echo $RANDOM )"
#PY_TEST_FILE="_${NUM}.py"

#touch $PY_TEST_FILE
#echo "try:" >> $PY_TEST_FILE
#echo "   import telegram" >> $PY_TEST_FILE
#echo "except ImportError as e:" >> $PY_TEST_FILE
#echo "   print('Next execution is making no sense')" >> $PY_TEST_FILE

#python3 $PY_TEST_FILE
#rm $PY_TEST_FILE

ANSWER=""

echo ""
echo "You are setting environment for SmartChainBot. Stay online."
echo""
echo "NOTE: this script should be run as << source ./set-env >> "
echo ""
echo "Do not fear possible traceback here, just searching for python dependency"
echo ""
python3 -c "import telegram"
if [ "$?" -eq "1" ]; then  #No such module, if $? equals 0, module is present
	echo ""
	echo "Please, install <telegram> dependency and re-run this script"
	echo "Or we could try to install it now? (yes/no)"
	while [ "$ANSWER" != "yes\n" ] && [ "$ANSWER" != "no\n" ]
	do
		if [ "$ANSWER" = "yes" ]; then
			pip install python-telegram-bot --upgrade
			pip3 install python-telegram-bot --upgrade
			break
		elif [ "$ANSWER" = "no" ]; then
			return
		else
			echo ""
			echo "Answer, please, <yes> or <no>"
			read ANSWER
		fi
	done
fi



# Special cases should be handled by elif

if [ $OSTYPE = "darwin19" ]
then
    echo " We are on Mac"
    echo " So, Pls.."
    echo " We should be very coushious regarding bash scripts on Mac"
    echo " You should MANNUALLY set environment variables TGTOKEN, COINCAPKEY"

else
     echo "Setting nessesary system variables"
     echo "  1. Token"
     echo "  2. CoincapKey"

     echo "Input your Telegram Bot token"
     read TGTOKEN_INPUT
     echo "Input your Coincap key"
     read COINCAPKEY_INPUT
     export TGTOKEN=$(echo $TGTOKEN_INPUT | sed -e 's/\r//g')
     export COINCAPKEY=$(echo $COINCAPKEY | sed -e 's/\r//g') #trimming for \r and \n removal

     if [ -z "$TGTOKEN" ] && [ -z "$COINCAPKEY" ]
     then
         echo "Environment is ready to use"
     fi

fi
