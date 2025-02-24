import zmq
import json
import time

context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

time.sleep(1.5)

# List of tuples to generate random integers (lower bound, upper bound, count)
ranges = [
    (2, 5, 1),
    (4, 8, 2),
    (-100, 100, -1)
]

# Serialize to JSON
message = json.dumps(ranges)

# Send request
socket.send_string(message)

# Receive response (blocking call
response = socket.recv()

try:
    # Deserialize the response to get the random integers
    data = json.loads(response.decode())
    # Check if the response is an error message
    if isinstance(data, dict) and "Error" in data:
        print(f"Error: {data['Error']}")
    else:
        print("Received random numbers: ", data)
except json.JSONDecodeError:
    print("Received invalid JSON response from the server.")
