Got it 👍 — here’s the **README.md** in proper format so you can copy-paste directly into your repo:

````markdown
# 📊 Razz-LogRadar  

🚀 **Razz-LogRadar** is a lightweight Python-based log analysis tool designed to help security researchers and learners detect suspicious activity hidden inside log files.  
It automatically scans all logs in a given folder for suspicious keywords (like `error`, `failed`, `unauthorized`) and writes them into a new file for easy review.  

> 🛡 Developed by **Razz Security Academy** for cybersecurity training, automation learning, and real-world log analysis practice.  

---

## ✨ Features  
- 🔍 Automatically scan all `.log` or `.txt` files in a folder  
- ⚡ Identify suspicious entries using user-defined keywords  
- 📂 Save results into a new `suspicious_logs.txt` file  
- 🖥 Beginner-friendly, built with **Python**  
- 🎓 Perfect for **students, researchers, and SOC analysts** learning automation  

---

## 🛠 Requirements  
- Python **3.8+**  
- Works on Linux, macOS, and Windows  
- Recommended: Run inside a **virtual environment**  

---

## ⚡ Setup Instructions  

### 1️⃣ Clone the repo  
```bash
git clone https://github.com/Akash-razzsec/razz-logradar.git
cd razz-logradar
````

### 2️⃣ Create & activate a virtual environment

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

(Currently none — but future updates may require libraries)

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the tool

```bash
python logradar.py
```

---

## 📖 Usage Example

1. Place your log files inside a folder (e.g., `logs/`).
2. Run the script:

```bash
python logradar.py
```

3. Enter folder path when asked → e.g., `logs/`
4. Enter suspicious words (comma-separated) → e.g., `error,failed,unauthorized`
5. Tool generates a file → `suspicious_logs.txt` with all matching lines.

---

## 📸 Demo

```bash
$ python logradar.py
Enter log folder path: logs/
Enter suspicious words (comma separated): error, failed

✅ Scan complete! Suspicious entries saved in suspicious_logs.txt
```

---

## 📢 Branding

🔹 **Developed by:** Razz Security Academy

## ⚠ Disclaimer

This tool is built **only for educational purposes**.
Razz Security Academy is **not responsible** for any misuse.

```

---

Do you also want me to prepare a **ready-to-go `requirements.txt` + `logradar.py` starter code** so your repo looks professional right away?
```
