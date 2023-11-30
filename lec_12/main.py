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

def generate_and_write_numbers(filename, num_lines=100, num_per_line=20):
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            numbers = [random.randint(-50, 90) for _ in range(num_per_line)]
            line = ' '.join(map(str, numbers))
            file.write(line + '\n')

def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    processed_lines = map(lambda line: list(filter(lambda x: x > 40, map(int, line.split()))), lines)

    with open(filename, 'a') as file:
        for line in processed_lines:
            file.write(' '.join(map(str, line)) + '\n')

def read_file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))

filename = 'random_nums.txt'

generate_and_write_numbers(filename)

process_file(filename)

gen = read_file_generator(filename)

for line in gen:
    print(line)
