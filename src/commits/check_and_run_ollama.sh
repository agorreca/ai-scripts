#!/bin/bash

# Check if Ollama is running by checking the port
if ! netstat -an | grep 11434 | grep LISTEN > /dev/null
then
    echo "Ollama is not running. Starting Ollama..."
    ollama serve &
    sleep 5 # Wait for Ollama to start
fi
