#!/bin/bash

OUT=$(ollama --version | awk '{print $1$2}')

if [ "$OUT" != "ollamaversion" ]; then
	echo "Ollama is not installed, or correctly configured."
	exit
else
	echo "Ollama installed and setup correctly."
fi

echo "Installing required model..."

ollama pull gemma3:270m

echo "Successfully installed model!"
