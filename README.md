# Python Network Stress Tester

> ⚠️ For **educational use only**. Do not run this script against any system you do not explicitly own or have written permission to test.

---

## 📖 Description

This is a simple Python script that uses multi-threading and sockets to simulate repeated connections to a specified target IP and port. It's intended for **learning purposes only**, such as understanding how sockets and threading behave in Python, and how basic network stress tools work.

---

## 🛠 Features

- Multi-threaded socket flooding
- Basic fake IP header (for simulation)
- Logs connection count
- Lightweight — no dependencies beyond Python standard library

---

## ⚙️ Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/Take-Off-7/Python-Authomation.git
cd Python-Authomation

⸻

2. Start a local HTTP server for testing:

To safely test the script without hitting external servers, run:
python -m http.server 80
This starts a simple HTTP server on your machine at:
http://127.0.0.1:80

---

3. Run the script:
In a different terminal, execute the stress test script:
python main.py
You should see output like:
Connections made: 500
Connections made: 1000
Connections made: 1500
...
This means the script is successfully opening many connections to your test server.

⸻

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

⸻

⚠️ Disclaimer

This script is for educational use only. Do not run it against any system that you do not own or have explicit permission to test. Misuse of this code may violate local laws and network policies.

The author assumes no responsibility for how this code is used.

⸻

👤 Author
	•	GitHub: Take-Off-7
	•	Email: tfakeye7@gmail.com

⸻

💡 Contributing

Contributions are welcome. Suggestions to improve usability, safety, or extensibility (e.g., CLI support, rate limiting, logging) are appreciated. Fork the repo and open a pull request.

⸻

🏁 Final Note

This project is a learning tool. Use it ethically and responsibly.