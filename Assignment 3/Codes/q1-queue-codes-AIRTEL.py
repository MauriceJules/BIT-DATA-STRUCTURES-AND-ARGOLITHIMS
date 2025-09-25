from collections import deque

queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6", "Client7"])

print("Initial Queue:", queue)

# Serve 2 clients
queue.popleft()
queue.popleft()

# New front of the queue
print("After 2 served, front is:", queue[0])
