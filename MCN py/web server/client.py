import socket
import threading
from concurrent.futures import ThreadPoolExecutor

HOST = "localhost"
PORT = 8888
REQUEST_COUNT = 5


def make_request(request_id: int) -> None:
    try:
        with socket.create_connection((HOST, PORT), timeout=5) as client_socket:
            request = (
                f"GET /?client={request_id} HTTP/1.1\r\n"
                f"Host: {HOST}:{PORT}\r\n"
                "Connection: close\r\n\r\n"
            )
            client_socket.sendall(request.encode())

            response_parts = []
            while True:
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                response_parts.append(chunk)

            response = b"".join(response_parts).decode(errors="replace")
            first_line = response.splitlines()[0] if response else "<empty response>"
            print(f"[Client {request_id} | Thread {threading.get_ident()}] {first_line}")
            print(response)
            print("-" * 60)
    except Exception as exc:
        print(f"[Client {request_id}] Error: {exc}")


def main() -> None:
    print(f"Starting {REQUEST_COUNT} parallel requests to {HOST}:{PORT}...\n")
    with ThreadPoolExecutor(max_workers=REQUEST_COUNT) as executor:
        for request_id in range(1, REQUEST_COUNT + 1):
            executor.submit(make_request, request_id)


if __name__ == "__main__":
    main()
