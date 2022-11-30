import time


def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Run time: {end_time-start_time} for {func.__name__}")
        return result

    return timeit_wrapper
