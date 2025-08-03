# 💬 Python TCP Chat Room

> ⚠️ For educational use only. Do not expose this server to the internet without proper security measures.

---

## 📖 Description

This is a simple **multithreaded chat application** built using Python's `socket` and `threading` libraries. It includes both a server and client script that allow multiple users to connect and chat in real-time over a local network.

---

## 🧩 Components

- **Server** (`server.py`): Accepts client connections, handles nicknames, and broadcasts messages.
- **Client** (`client.py`): Connects to the server, sends and receives messages.

---

## 🚀 Features

- Real-time group chat
- Multithreaded for simultaneous message handling
- Nickname identification for each user
- Basic error handling and client disconnection detection

---

## 🛠 Requirements

- Python 3.x

---

## ⚙️ How It Works

### Server

- Binds to `127.0.0.1:55555` (can be changed).
- Waits for client connections.
- Asks for nickname (`'NICK'` signal).
- Maintains lists of active clients and nicknames.
- Broadcasts messages to all connected clients.

### Client

- Connects to the server at `127.0.0.1:55555`.
- Sends nickname on request.
- Runs two threads:
  - One for receiving and printing messages.
  - One for sending user input to the server.

---

## 🧪 How To Use

1. **Start the server**:

```bash
python server.py
```

2. **Run one or more clients** (in different terminals or machines on the same network):

```bash
python client.py
```

3. **Enter a nickname** when prompted and start chatting.

---

## ✅ Example

```
Choose a nickname: Alice
Connected to the server!
Bob joined the chat!
Alice: Hello, Bob!
Bob: Hi Alice!
```

---

## 🔄 To Customize

- **Change IP and port** in both `server.py` and `client.py` to match your network setup.
- Add GUI, encryption, message timestamps, or private messaging for more features.

---

## 📄 License

MIT License

---

## 🤝 Disclaimer

This tool is for learning and local network use only. It lacks encryption and authentication and is **not safe for production or public deployment**.