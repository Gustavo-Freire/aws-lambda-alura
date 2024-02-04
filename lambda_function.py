import json
import os

def lambda_handler(event, context):
    # TODO implement
    MINHA_VAR = os.environ.get('MINHA_VAR')
    print(MINHA_VAR)
    print('Testando nova versão')
    return {
        'statusCode': 200,
        'body': f'<html><body>Dados da requisicap {event}</body></html>',
        'headers': {
            "content-type" : "text/html"
        }
    }
