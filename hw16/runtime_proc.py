import time
import multiprocessing
import random

import matplotlib.pyplot as plt
import seaborn as sns


def do_work(num):
    """
    Multiplies random numbers num-times
    @param num: int
    @return: None
    """
    for _ in range(num):
        random.randint(1, 40) ** random.randint(1, 20)


def measure_proc_time_dependence(func, *args):
    """
    Measures the runtime of function for different number of processes (from 0 to 40)
    @param func: function
    @param args: arguments for the function
    @return: runtimes, list
    """
    runtimes = []
    n_procs = list(range(41))

    # Measuring runtime for different number of processess
    for n_proc in n_procs:
        start_time = time.perf_counter()
        procs = [multiprocessing.Process(target=func, args=args) for _ in range(n_proc)]
        for proc in procs:
            proc.start()
        for proc in procs:
            proc.join()
        runtimes.append(time.perf_counter() - start_time)
    return runtimes


def plot_runtimes(runtimes, n_procs=list(range(41))):
    """
    Plots the runtime of a function against the number of processes
    @param runtimes: list, runtimes of a function
    @param n_procs: list, processes (default from 0 to 40)
    @return: Shows the plot
    """
    sns.set(rc={'figure.figsize': (15, 10)})
    sns.lineplot(x=n_procs, y=runtimes)
    plt.xticks(n_procs)
    plt.xlabel("Number of processes")
    plt.ylabel("Runtime, [sec]")
    plt.show()


if __name__ == "__main__":
    runtimes_4 = measure_proc_time_dependence(do_work, 10 ** 4)
    # runtimes_5 = measure_proc_time_dependence(do_work, 10 ** 5)
    # runtimes_6 = measure_proc_time_dependence(do_work, 10 ** 6)

    plot_runtimes(runtimes_4)
    # plot_runtimes(runtimes_5)
    # plot_runtimes(runtimes_6)

