import json
import time

def lambda_handler(event, context):
    """
    Lambda function with a long-running operation that will exceed
    API Gateway's maximum integration timeout (29 seconds).
    
    This demonstrates API Gateway timeout behavior.
    """
    print("Lambda function started")

    # Sleep for 25 seconds to exceed API Gateway's 29-second timeout
    sleep_duration = 25
    print(f"Sleeping for {sleep_duration} seconds...")
    
    try:
        time.sleep(sleep_duration)
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Success! Lambda completed execution.",
                "slept_for_seconds": sleep_duration
            })
        }
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
