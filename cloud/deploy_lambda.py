# Note: This is a placeholder. In real use, you'd zip your model handler and deploy via AWS CLI or SDK

def instructions():
    print("""
    1. Zip your model and handler (e.g. handler.py and model.h5)
    2. Use AWS CLI:

       aws lambda create-function \\
         --function-name image-predictor \\
         --runtime python3.9 \\
         --handler handler.lambda_handler \\
         --zip-file fileb://model_package.zip \\
         --role arn:aws:iam::ACCOUNT_ID:role/LambdaExecRole
    """)

if __name__ == "__main__":
    instructions()
