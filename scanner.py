import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f"\n🔍 Scanning Target: {target}")
    print(f"⏳ Scan Started at: {datetime.now()}")
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target, port))

            if result == 0:
                print(f"🟢 Port {port} is OPEN")

            s.close()

    except KeyboardInterrupt:
        print("\n❌ Scan stopped by user.")

    except socket.gaierror:
        print("❌ Hostname could not be resolved.")

    except socket.error:
        print("❌ Server not responding.")

    print("-" * 50)
    print("✔ Scan Completed.")


if __name__ == "__main__":
    print("🔐 Simple Port Scanner\n")

    target = input("Enter target IP or domain: ")

    try:
        start_port = int(input("Start Port: "))
        end_port = int(input("End Port: "))
        scan_ports(target, start_port, end_port)

    except ValueError:
        print("❌ Please enter valid port numbers.")
