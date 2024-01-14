# Azure Function - Function App

This repository contains the code for an Azure Function named `function_app.py`.

## Functionality

The function is HTTP-triggered and interacts with OpenAI's GPT-3.5-turbo model. It receives a JSON payload with a 'prompt' and returns a response from the AI model.

## Usage

Send a POST request to the function's URL with a JSON body containing a 'prompt' key. For example:

```json
{
    "prompt": "Translate the following English text to French: '{text}'"
}
