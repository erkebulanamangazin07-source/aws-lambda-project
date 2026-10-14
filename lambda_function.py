def lambda_handler(event, context):
    name = event.get("name", "Student")

    return {
        "statusCode": 200,
        "body": f"Salem, {name}! AWS Lambda jumys istep tur."
    }
