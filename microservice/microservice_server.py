import zmq
import json
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()

    # Try to deserialize the message as JSON
    try:
        ranges = json.loads(message.decode())
    except Exception:
        error_message = {"Error": "Corrupted JSON request"}
        socket.send_string(json.dumps(error_message))
        continue

    # Validate that input is a list of tuples and each has 3 elements
    valid_request = True
    for r in ranges:
        if not isinstance(r, list) or len(r) != 3:
            valid_request = False
            break

    if not valid_request:
        error_message = {"Error": "Invalid input."}
        socket.send_string(json.dumps(error_message))
        continue

    # Initialize an empty list to hold the lists of random integers
    results = []

    # Generate random numbers for each tuple in the input
    for lower_bound, upper_bound, count in ranges:
        if lower_bound > upper_bound or not isinstance(count, int) or count <= 0:
            results.append([])
        else:
            randomize = [random.randint(lower_bound, upper_bound) for i in range(count)]
            results.append(randomize)

    # Serialize to JSON
    response = json.dumps(results)

    # Send response back to client
    socket.send_string(response)
