from concurrent.futures import ProcessPoolExecutor
import os

def task(n):
    print("Executing Task {} on Process {}".format(n, os.getpid()))

def main():
    executor = ProcessPoolExecutor(max_workers=3)
    task1 = executor.submit(task, 1)
    task2 = executor.submit(task, 2)

if __name__ == '__main__':
    main()

