stack = []

# Push operations
stack.append("Form1")
stack.append("Form2")
stack.append("Submit")

print("Initial Stack:", stack)

# Undo all (pop everything)
while stack:
    stack.pop()

# Check what remains
print("After undo all, stack is:", stack)
