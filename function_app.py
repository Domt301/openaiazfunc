import azure.functions as func
import datetime
import json
import logging
import os
from openai import OpenAI
app = func.FunctionApp()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route(route="HttpExample", auth_level=func.AuthLevel.ANONYMOUS)
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            prompt = req_body.get('prompt')
            # minor change

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        res_fromai = talk_to_open_ai(prompt)
        return func.HttpResponse(
            json.dumps({
                "response": res_fromai
            }),
            status_code=200,
            mimetype="application/json"
        )
    
def talk_to_open_ai(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

    
    )

    res = completion.choices[0].message.content
    return res