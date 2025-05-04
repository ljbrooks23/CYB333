import socket
import time

# Scan the ports of the local host and ports
def scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except Exception as ex:
        print(f"[!] Error scanning port {port}: {ex}")
        return False

# Function to get the host and the port range
def main():
    host = input("Enter target host (127.0.0.1): ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

# Makes sure the range is ok
    if start_port < 0 or end_port > 1023 or start_port > end_port:
        print("Port Range Not Possible.")
        return
# Prints the results
    print(f"Scanning {host} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        if scan(host, port):
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
        time.sleep(0.2)  # Slight delay

# Executes the main function
if __name__ == "__main__":
    main()
