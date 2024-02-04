import json

def lambda_handler(event, context):
    # TODO implement
    print('Testando nova versão')
    return {
        
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!2')
    }
