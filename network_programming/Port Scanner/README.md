# 🔍 Python Multithreaded Port Scanner

> ⚠️ **For educational and authorized use only.** Do not scan systems you do not own or have explicit permission to test.

---

## 📖 Description

This is a basic multithreaded port scanner written in Python. It uses the `socket` module to check for open ports on a specified target and the `threading` module to speed up scanning through concurrency.

It's designed to demonstrate core concepts of:

- Networking with sockets
- Multithreading in Python
- Queue-based job distribution

---

## 🚀 Features

- Scans a target host for open TCP ports (default: 1–1023)
- Uses multithreading to perform fast concurrent scanning
- Simple and beginner-friendly Python code
- Easily configurable for different targets and port ranges

---

## 🛠 Requirements

- Python 3.x
- No external libraries needed (uses only standard library)

---

## 📦 Usage

1. **Clone or download the script** to your local machine:

```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```

2. **Edit the script** (`main.py`) to set your target IP address:

```python
target = "127.0.0.1"  # Replace with desired IP
```

3. **Run the script:**

```bash
python main.py
```

You should see output like:

```
Port 22 is open!
Port 80 is open!
...
Open ports are: [22, 80]
```

---

## 🧠 How It Works

- A queue is filled with port numbers to scan.
- 100 worker threads are created to consume from the queue.
- Each worker attempts to open a TCP socket connection to the target.
- If successful, the port is considered **open**.

---

## ⚙️ Configuration

You can tweak:

- `target`: IP or hostname to scan
- `port_list`: Range of ports to scan (`range(1, 65535)` for full range)
- Number of threads: `for t in range(100)`

---

## 📌 Note

- Requires appropriate permissions on the host system.
- Scanning large port ranges or remote targets may be blocked by firewalls.

---

## ✅ Example Output

```
Port 22 is open!
Port 80 is open!
Port 443 is open!
Open ports are: [22, 80, 443]
```

---

## 📄 License

MIT License

---

## 🤝 Disclaimer

This tool is for **educational purposes** only. Always get explicit permission before scanning any network or system.
