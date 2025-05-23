def instructions():
    print("""
    1. Create an Azure Function with HTTP trigger.
    2. Use Azure CLI to deploy:

       func azure functionapp publish <YourFunctionAppName>
    """)

if __name__ == "__main__":
    instructions()
