import os
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from langfuse import Langfuse

def test_connection():
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api', '.env'))
    print(f"Loading environment variables from {env_path}...")
    load_dotenv(env_path)

    print("Initializing Langfuse client...")
    try:
        langfuse = Langfuse(
            public_key=os.environ.get("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.environ.get("LANGFUSE_SECRET_KEY"),
            host=os.environ.get("LANGFUSE_BASE_URL")
        )
        
        print("Checking authentication...")
        if langfuse.auth_check():
            print("✅ Success! Successfully authenticated with Langfuse.")
        else:
            print("❌ Error: Authentication failed. Please check your credentials.")
    except Exception as e:
        print(f"❌ Error connecting to Langfuse: {e}")

if __name__ == "__main__":
    test_connection()
