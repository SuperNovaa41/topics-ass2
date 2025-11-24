#!/bin/bash

OUT=$(ollama --version | awk '{print $1$2}')

if [ "$OUT" != "ollamaversion" ]; then
	echo "Ollama is not installed, or correctly configured."
	exit
else
	echo "Ollama installed and setup correctly."
fi

echo "Installing required model..."

ollama pull llama3.1:8b

echo "Successfully installed model!"
