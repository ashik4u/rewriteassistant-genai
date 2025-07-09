# ✨ Clipboard Rewriter — Gemini-Powered Text Polisher

Clipboard Rewriter is a lightweight Python desktop app that uses **Google Gemini 1.5 Flash** to instantly **fix grammar** and **rewrite copied text**.  
Trigger rewrites with a **hotkey**, switch **tone/style**, run silently in the **system tray**, and get real-time **Windows notifications**.

---

## 🚀 Features

- 🧠 Powered by **Google Gemini 1.5 Flash**
- 📝 One-hotkey **clipboard rewrite** (`Ctrl + Shift + B`)
- 🔁 **Writing style switcher**: Formal / Casual / Business
- 📌 **System tray app** with right-click menu
- 🔔 **Native Windows toast notifications**
- 💾 Automatically **logs rewrite history**
- 🪶 Lightweight, **background-friendly** tool

---

## 🔧 Installation

### 1. Clone the repo
```bash
git clone https://github.com/ashik4u/clipboard-rewriter-genai.git
cd clipboard-rewriter-genai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

> Or install manually:
```bash
pip install pyperclip keyboard pystray pillow winotify google-generativeai
```

### 3. Set your Gemini API Key

Open the script and replace the line:
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

Get your API key from: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## ▶️ Usage

1. Run the script:

```bash
python clipboard_rewriter.py
```

2. Press **Ctrl+Shift+B** to rewrite any copied text.
3. Right-click the tray icon to:
   - ✅ Enable/Disable rewriting
   - 🔁 Change writing style
   - 📂 View rewrite history
   - ❌ Exit the app

---

## 🖼 Tray Menu Options

| Option               | Description                          |
|----------------------|--------------------------------------|
| ✍️ Enable/Disable     | Toggle rewriting functionality       |
| 🔁 Change Style       | Switch between formal/casual/business |
| 📂 View Log File      | Opens local rewrite log              |
| ❌ Exit               | Quit the app                         |

---

## 📂 Rewrite Log

All rewrites are saved to `rewrite_log.txt` in this format:

```
---
Original:
Your original text...

Rewritten:
Your improved Gemini-polished version...
```

---

## 📦 Build to .exe (optional)

To package the app into a portable `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole clipboard_rewriter.py
```

Output will appear in the `dist/` folder.

---

## 💡 Future Ideas

- 🔒 Custom rewrite prompt profiles
- 🧠 GPT + Gemini toggle
- 🌐 Multi-language support
- 🖥️ Auto-start with Windows

---

## 🧠 Credits

- [Google Gemini](https://aistudio.google.com/)
- [winotify](https://github.com/gristlabs/winotify)
- [pystray](https://github.com/moses-palmer/pystray)

---

## 📄 License

MIT License © Ashik(https://github.com/ashik4u
