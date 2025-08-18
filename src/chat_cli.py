import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def _create_client() -> OpenAI:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY in environment/.env")

    # Auto-detect OpenRouter vs DeepSeek-native keys and set base URL + default model
    is_openrouter = api_key.startswith("sk-or-")
    if is_openrouter:
        base_url = os.getenv("DEEPSEEK_BASE_URL", "https://openrouter.ai/api/v1")
        default_model = os.getenv("DEEPSEEK_MODEL", "deepseek/deepseek-chat")
    else:
        base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
        default_model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    client = OpenAI(api_key=api_key, base_url=base_url)
    # Store chosen default model on the client for later use
    client._default_model = default_model  # type: ignore[attr-defined]
    return client

def run_chat():
    print("🤖 DeepSeek Chatbot is ready! Type 'exit' to quit.\n")

    try:
        client = _create_client()
    except Exception as exc:
        print(f"⚠️ Unable to initialize client: {exc}")
        return

    # Quick auth check
    try:
        _ = client.models.list()
    except Exception as exc:
        print("❌ Authentication check failed.\n- Ensure your `.env` contains a valid `DEEPSEEK_API_KEY` from the DeepSeek console.\n- If needed, set `DEEPSEEK_BASE_URL=https://api.deepseek.com/v1`.\n- Then rerun: python src/main.py")
        print(f"Details: {exc}")
        return

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        try:
            response = client.chat.completions.create(
                model=getattr(client, "_default_model", "deepseek-chat"),
                messages=[{"role": "user", "content": user_input}],
            )
            print("Bot:", response.choices[0].message.content)
        except Exception as exc:
            print(f"❌ Request failed: {exc}")
