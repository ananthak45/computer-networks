import socket

def calculate_cutoff(domain, marks):
    if domain == "engineering":
        return (2 * int(marks[0]) + 4 * int(marks[1]) + 2 * int(marks[2])) / 8
    elif domain == "medical":
        return (2 * int(marks[0]) + 4 * int(marks[1]) + 2 * int(marks[2])) / 8
    elif domain == "commerce":
        return sum(int(m) / 4 for m in marks)
    elif domain == "law":
        return sum(int(m) / 4 for m in marks)
    elif domain == "mba":
        return (int(marks[0]) / 2 + int(marks[1]) / 4 + int(marks[2]) / 4)
    elif domain == "msc":
        return (int(marks[0]) / 2 + int(marks[1]) / 2)
    else:
        return 0

def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0.0.0.0', 12345))
    print("UDP server listening on port 12345")
    
    while True:
        data, addr = server.recvfrom(1024)
        print(f"Connected by {addr}")
        domain, *marks = data.decode().split(',')
        result = calculate_cutoff(domain, marks)
        server.sendto(f"{result}".encode(), addr)

if __name__ == "__main__":
    udp_server()
