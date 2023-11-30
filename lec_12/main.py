import random
import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper

# Function to generate random numbers and write them to a file
def generate_and_write_numbers(filename, num_lines=100, num_per_line=20):
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            numbers = [random.randint(-50, 90) for _ in range(num_per_line)]
            line = ' '.join(map(str, numbers))
            file.write(line + '\n')

# Function to read lines from a file, convert them to integer arrays, filter numbers > 40, and write back to the file
@measure_execution_time
def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    processed_lines = map(lambda line: list(filter(lambda x: x > 40, map(int, line.split()))), lines)

    with open(filename, 'a') as file:
        for line in processed_lines:
            file.write(' '.join(map(str, line)) + '\n')

# Generator function to yield lines from a file
def read_file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))

# Example usage
filename = 'random_nums.txt'

# Step 1: Generate and write random numbers to a file
generate_and_write_numbers(filename)

# Step 2: Process the file and measure execution time using the decorator
process_file(filename)

# Step 3: Read the file using a generator
gen = read_file_generator(filename)

# Step 4: Print the lines yielded by the generator
for line in gen:
    print(line)
