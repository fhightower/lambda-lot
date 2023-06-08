def lambda_handler(event, context):
    count = int(event.get('queryStringParameters', {}).get('count') or 1)

    return 'λ' * count

