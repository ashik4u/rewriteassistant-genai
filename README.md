2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install pyperclip keyboard pystray pillow winotify google-generativeai
3. Set your Gemini API Key
Open the script and replace the line:

python
Copy
Edit
genai.configure(api_key="YOUR_GEMINI_API_KEY")
Get your API key from: https://aistudio.google.com/app/apikey

▶️ Usage
Run the script:

bash
Copy
Edit
python clipboard_rewriter.py
Press Ctrl+Shift+B to rewrite any copied text.

Right-click the tray icon to:

✅ Enable/Disable rewriting

🔁 Change writing style

📂 View rewrite history

❌ Exit the app

🖼 Tray Menu Options
Option	Description
✍️ Enable/Disable	Toggle rewriting functionality
🔁 Change Style	Switch between formal/casual/business
📂 View Log File	Opens local rewrite log
❌ Exit	Quit the app

📂 Rewrite Log
All rewrites are saved to rewrite_log.txt in this format:

yaml
Copy
Edit
---
Original:
Your original text...

Rewritten:
Your improved Gemini-polished version...
📦 Build to .exe (optional)
To package the app into a portable .exe:

bash
Copy
Edit
pip install pyinstaller
pyinstaller --onefile --noconsole clipboard_rewriter.py
Output will appear in the dist/ folder.

💡 Future Ideas
🔒 Custom rewrite prompt profiles

🧠 GPT + Gemini toggle

🌐 Multi-language support

🖥️ Auto-start with Windows

🧠 Credits
Google Gemini
winotify
pystray

