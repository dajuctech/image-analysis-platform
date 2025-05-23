def instructions():
    print("""
    1. Create a main.py and requirements.txt (including tensorflow).
    2. Deploy:

       gcloud functions deploy predict_image \\
         --runtime python39 \\
         --trigger-http \\
         --allow-unauthenticated
    """)

if __name__ == "__main__":
    instructions()
