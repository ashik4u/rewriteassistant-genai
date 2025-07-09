import pyperclip
import keyboard
import time
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def grammar_and_rewrite(text):
    prompt = (
        "You are a professional grammar checker and rewriting assistant. "
        "Check the grammar of the following text, fix any errors, and rewrite it "
        "in clear, polished English. Only return the corrected and rewritten version.\n\n"
        f"{text}"
    )
    response = model.generate_content(prompt)
    return response.text

def on_hotkey():
    try:
        original_text = pyperclip.paste()
        if not original_text.strip():
            print("Clipboard is empty or no text found.")
            return

        print("Processing clipboard text...")
        rewritten = grammar_and_rewrite(original_text)
        pyperclip.copy(rewritten)
        print("Clipboard text rewritten! You can now paste it.")
    except Exception as e:
        print(f"Error rewriting text: {e}")

def main():
    print("Clipboard Rewrite Tool running...")
    print("Press Ctrl+Shift+R to rewrite clipboard text.")
    keyboard.add_hotkey('ctrl+shift+r', on_hotkey)
    keyboard.wait()  # block forever, waiting for hotkey

if __name__ == "__main__":
    main()
