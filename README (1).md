# 📧 Email Extractor GUI (Tkinter)

This is a simple Python GUI tool that extracts email addresses from a `.txt` file using regular expressions and saves them to a new file.

## 🛠 Features
- Simple GUI using `tkinter`
- Select any `.txt` file with email content
- Extracts all email addresses
- Saves results in a new file `emails_extracted.txt` in the same folder


## 🐍 Requirements

This project uses only Python standard libraries:

- `tkinter`
- `re`
- `os`

### ✅ Tested with:
- Python 3.10+
- Works on Windows/Linux/Mac

## 🔧 How to Run

1. Make sure Python 3 is installed.
2. Save the main code as `email_extractor.py`.
3. Run the script:

```bash
python email_extractor.py
```

4. A GUI will open — select your text file and extract emails.

## 📂 Output

- A new file `emails_extracted.txt` will be created in the same directory as your selected file, containing all extracted email addresses.

## 📄 Example Input (`sample.txt`)
```
Hello, contact us at info@example.com or support@domain.org.
Also check marketing@demo.co.uk and hr@company.net.
```

## 📁 Output (`emails_extracted.txt`)
```
hr@company.net
info@example.com
marketing@demo.co.uk
support@domain.org
```

---

## 📃 License
This project is open-source and free to use for learning or modification.