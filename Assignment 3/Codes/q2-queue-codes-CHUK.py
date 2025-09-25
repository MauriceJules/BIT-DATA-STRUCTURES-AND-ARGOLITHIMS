from collections import deque

queue = deque(["Patient1", "Patient2", "Patient3", "Patient4", "Patient5", "Patient6", "Patient7", "Patient8", "Patient9"])

print("Initial Queue:", queue)

# Serve 3 patients
served = [queue.popleft() for _ in range(3)]

# The third served is:
print("The third served is:", served[-1])
