# api/views.py
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from decouple import config
import requests
import uuid

CHATBOT_API = config('CHATBOT_API', default='default')
CHATBOT_URL = config('CHATBOT_URL', default='default')

TRANSLATOR_KEY = config('TRANSLATOR_KEY', default='default')
TRANSLATOR_ENDPOINT = config('TRANSLATOR_ENDPOINT', default='default')
TRANSLATOR_REGION = config('TRANSLATOR_REGION', default='default')

client = openai.OpenAI(api_key=CHATBOT_API, base_url=CHATBOT_URL)

@csrf_exempt
def chat(request):
    if request.method == 'GET':
        return JsonResponse({"error": "Please send a POST request"})
    
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return JsonResponse({"response": response.choices[0].message.content})

@csrf_exempt
def translateVtoJ(request):
    if request.method == 'GET':
        return JsonResponse({"error": "Please send a POST request"})
    
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        
        path = '/translate'
        constructed_url = TRANSLATOR_ENDPOINT + path

        params = {
            'api-version': '3.0',
            'from': 'vi',
            'to': ['ja']
        }

        headers = {
            'Ocp-Apim-Subscription-Key': TRANSLATOR_KEY,
            'Ocp-Apim-Subscription-Region': TRANSLATOR_REGION,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': text
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()

        translated_texts = [translation['text'] for translation in response[0]['translations']]
        return JsonResponse({"response": translated_texts})

@csrf_exempt
def translateJtoV(request):
    if request.method == 'GET':
        return JsonResponse({"error": "Please send a POST request"})
    
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        
        path = '/translate'
        constructed_url = TRANSLATOR_ENDPOINT + path

        params = {
            'api-version': '3.0',
            'from': 'ja',
            'to': ['vi']
        }

        headers = {
            'Ocp-Apim-Subscription-Key': TRANSLATOR_KEY,
            'Ocp-Apim-Subscription-Region': TRANSLATOR_REGION,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': text
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()

        translated_texts = [translation['text'] for translation in response[0]['translations']]
        return JsonResponse({"response": translated_texts})