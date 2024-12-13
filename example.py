from tqdm import tqdm
import time
# Create a list of numbers
numbers = range(100)

# Wrap the list with tqdm
for num in tqdm(numbers):
    # Simulate some work (e.g., sleep for 0.01 seconds)
    time.sleep(0.01)
    # Do something with num...