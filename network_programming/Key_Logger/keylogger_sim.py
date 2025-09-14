# keylogger_sim.py
print("Type something (press Enter to finish):")
while True:
    try:
        key = input("> ")
        with open("log.txt", "a") as f:
            f.write(key + "\n")
    except KeyboardInterrupt:
        print("\nStopped.")
        break
