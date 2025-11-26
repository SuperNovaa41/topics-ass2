#!/bin/bash

confirmation () {
    while true
    do
	read -r -p "Would you like to sign in now? [Y/n] " input
	case $input in
	    [yY][eE][sS]|[yY])
		break
		;;
	    [nN][oO]|[nN])
		exit 0
		;;
	    *)
	        ;;
	esac
    done
}


OUT=$(ollama --version | awk '{print $1$2}')

if [ "$OUT" != "ollamaversion" ]; then
	echo "Ollama is not installed, or correctly configured."
	exit
else
	echo "Ollama installed and setup correctly."
fi

echo "Installing required model..."

ollama pull gpt-oss:120b-cloud

echo "Successfully installed model!"

echo "You must sign in with ollama to use the cloud model."

confirmation

ollama signin
