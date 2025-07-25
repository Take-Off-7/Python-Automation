from concurrent.futures import ThreadPoolExecutor
import threading

def task(n):
    print("Processing {}".format(n))
    print("Accessing thread : {}".format(threading.get_ident()))
    print("Thread Executed {}".format(threading.current_thread()))

def main():
    print("Starting ThreadPoolExecutor")
    executor = ThreadPoolExecutor(max_workers=3)

    # Submit tasks and keep the futures
    f1 = executor.submit(task, 2)
    f2 = executor.submit(task, 3)
    f3 = executor.submit(task, 4)

    # Wait for each to complete
    f1.result()
    f2.result()
    f3.result()

    print("All tasks complete")

if __name__ == '__main__':
    main()
