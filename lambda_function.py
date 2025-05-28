import json
import os
import requests # Needs to be included in the Lambda deployment package or as a Layer
from openai import OpenAI # Needs to be included in the Lambda deployment package or as a Layer

def lambda_handler(event, context):
    """
    Handles API Gateway requests to interact with ChatGPT based on personal info.
    """
    print("Lambda function started. Event:", event)

    try:
        # 1. Read configuration from environment variables
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        persona_api_url = os.environ.get('PERSONA_API_URL')
        chatgpt_model = os.environ.get('CHATGPT_MODEL', 'gpt-3.5-turbo')

        if not openai_api_key or not persona_api_url:
            print("Error: Missing required environment variables (OPENAI_API_KEY, PERSONA_API_URL)")
            return {
                'statusCode': 500,
                'headers': {
                    'Access-Control-Allow-Origin': '*', # Allow all origins for CORS
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                'body': json.dumps({'error': 'Server configuration error: Missing API key or Persona API URL.'})
            }

        # 2. Get user query from the API Gateway request body
        #    Assumes the frontend sends a JSON request body, e.g., {"user_query": "Tell me about yourself."}
        try:
            body = json.loads(event.get('body', '{}'))
            user_query = body.get('user_query')
        except json.JSONDecodeError:
            print("Error: Invalid JSON in request body")
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                'body': json.dumps({'error': 'Invalid JSON format in request body.'})
            }

        if not user_query:
            print("Error: 'user_query' not found in request body")
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                'body': json.dumps({'error': "'user_query' is required in the request body."})
            }
        
        print(f"Received user query: {user_query}")

        # 3. Call Django API to get personal information
        print(f"Fetching persona info from: {persona_api_url}")
        try:
            response = requests.get(persona_api_url, timeout=10) # 10-second timeout
            response.raise_for_status() # Raise an exception for 4xx or 5xx status codes
            persona_data = response.json()
            print("Successfully fetched persona data.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching persona data from Django API: {e}")
            return {
                'statusCode': 503, # Service Unavailable
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                'body': json.dumps({'error': f'Could not retrieve personal information: {str(e)}'})
            }

        # 4. Construct the prompt for ChatGPT
        additional_info_text = persona_data.get('additional_info', '').strip()
        
        system_message_parts = [
            "You are a helpful AI assistant representing Yue Wen Peter Li.",
            "Your goal is to answer questions about Yue Wen Peter Li based *only* on the information provided below.",
            "Do not make up information or answer questions outside of this context.",
            "If the answer cannot be found in the provided information, clearly state that you don't have that specific information.",
            "Be friendly and conversational.",
            "\nHere is the general information about Yue Wen Peter Li:",
            f"Full Name: {persona_data.get('full_name', 'N/A')}",
            f"Job Title: {persona_data.get('job_title', 'N/A')}",
            f"Bio: {persona_data.get('bio', 'N/A')}",
            f"Skills Summary: {persona_data.get('skills_summary', 'N/A')}",
            f"Experience Summary: {persona_data.get('experience_summary', 'N/A')}",
            f"Hobbies: {persona_data.get('hobbies', 'N/A')}",
            f"Contact Email: {persona_data.get('contact_email', 'N/A (available upon request for serious inquiries)')}"
        ]

        if additional_info_text:
            system_message_parts.append("\nIn addition to the general information, here are more specific details and answers to frequently asked questions:")
            system_message_parts.append("---")
            system_message_parts.append(additional_info_text)
            system_message_parts.append("---")
            system_message_parts.append("When answering, prioritize information from the detailed Q&A section if it directly addresses the user's query.")
        
        system_message = "\n".join(system_message_parts)

        print("Constructed system message for ChatGPT.")
        # For debugging, you might want to print the full system_message, but be mindful of length in CloudWatch logs
        # print(f"System Message: {system_message}")

        # 5. Call the OpenAI API
        try:
            client = OpenAI(api_key=openai_api_key)
            print(f"Calling OpenAI API with model: {chatgpt_model}")
            chat_completion = client.chat.completions.create(
                model=chatgpt_model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_query}
                ]
            )
            chatgpt_response_content = chat_completion.choices[0].message.content
            print(f"Received response from OpenAI: {chatgpt_response_content}")
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return {
                'statusCode': 502, # Bad Gateway
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                'body': json.dumps({'error': f'Failed to get response from AI model: {str(e)}'})
            }

        # 6. Return ChatGPT's response
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*', # For easy frontend testing, allow all origins.
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS' # Allow POST and OPTIONS (for CORS preflight)
            },
            'body': json.dumps({'answer': chatgpt_response_content})
        }

    except Exception as e:
        print(f"Unhandled error in Lambda function: {e}")
        # This is a catch-all for any other unexpected errors
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': json.dumps({'error': f'An unexpected server error occurred: {str(e)}'})
        }
