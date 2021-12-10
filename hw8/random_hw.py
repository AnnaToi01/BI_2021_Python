import numpy as np
import random
import time
import functools
import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
from colorsys import hls_to_rgb


# I'm too lazy to write time.time() all the time, I'm creating a decorator
def timer(func):
    """
    Times a function
    @param func: function
    @return: wrapper
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper that returns how much time elapsed after function execution
        @param args: Arguments for the function
        @param kwargs: Keyword arguments for the function
        @return: time_elapsed: float, time elapsed
        """
        start = time.time()
        func(*args)
        stop = time.time()
        time_elapsed = stop - start
        return time_elapsed

    return wrapper


@timer
def random_ls(n):
    """
    Samples n values from 0 to 1 into a rand (using random)
    @param n: Number of samples
    @return: None
    """
    [random.random for i in range(n)]
    return


@timer
def np_random_ls(n):
    """
    Samples n values from 0 to 1 into a rand (using np.random)
    @param n: Number of samples
    @return: None
    """
    np.random.sample(n)
    return


def ls_num(start, stop, step):
    """
    List of numbers from start to stop with steps (half intervall, [start, stop))
    @param start: int, start
    @param stop: int, stop
    @param step: int, step
    @return: list of interval
    """
    return list(range(start, stop, step))


def calculate_random_time_array(number_of_elements, seeds):
    """
    Calculates arrays of shape (len(seeds), len(number_of_elements) with time needed to generate random list
    @param number_of_elements: list,
    @param seeds: list, seeds to run on
    @return: rand_time_array, np_rand_time_array: np.array
    """
    rand_time_array = np.zeros(shape=(len(seeds), len(number_of_elements)))
    np_rand_time_array = np.zeros(shape=(len(seeds), len(number_of_elements)))
    for n, _ in enumerate(number_of_elements):
        for k in range(len(seeds)):
            random.seed(seeds[k])
            np.random.seed(seeds[k])
            rand_time_array[k, n] = random_ls(n)
            np_rand_time_array[k, n] = np_random_ls(n)
    return rand_time_array, np_rand_time_array


def plot_time_gen_list(rand_time_array, np_rand_time_array, output_dir):
    """
    Plots the time dependency
    @param rand_time_array: np.array, time array for library "random"
    @param np_rand_time_array: np.array, time array for library "np.random"
    @param output_dir: str, output directory
    @return: saves plot in output directory and shows it
    """

    pd_rand_time_array = pd.DataFrame(rand_time_array[:, 0:100], columns=number_of_elements[0:100])
    pd_np_rand_time_array = pd.DataFrame(np_rand_time_array[:, 0:100], columns=number_of_elements[0:100])
    fig, ax = plt.subplots()
    pd_rand_time_array.boxplot(meanline=True, showmeans=True, showcaps=True,
                               showbox=True, showfliers=False, ax=ax, color="blue")
    pd_np_rand_time_array.boxplot(meanline=True, showmeans=True, showcaps=True,
                                  showbox=True, showfliers=False, ax=ax, color="orange")

    ax.plot(number_of_elements, np.median(rand_time_array, axis=0), label="random", color="blue")
    ax.plot(number_of_elements, np.median(np_rand_time_array, axis=0), label="np.random", color="orange")
    ax.set_yscale("log")
    ax.set_xscale("log")
    plt.legend(title="Used library:")
    plt.title("Time dependency of generating random list")
    plt.ylabel("log(time)")
    plt.xlabel("log(length of list)")
    plt.savefig(Path(output_dir, "rand_numpy_time_dependencies.jpg"))
    plt.show()


def check_sorted(ls):
    """
    Checks if list is sorted
    @param ls: list
    @return: True/False: Boolen, True if list is sorted
    """
    return all(ls[i] <= ls[i + 1] for i in range(len(ls) - 1))


@timer
def monkey_sort(ls):
    """
    Sorts list by monkey sort (also bogosort)
    @param ls: list
    @return: None
    """
    while not check_sorted(ls):
        random.shuffle(ls)
    return


def calculate_monkey_sort_time_dependency(length_list, seeds):
    """
    Returns array of shape (len(seeds), length_list-1) of time needed to sort the list
    @param length_list: int, length of lists to be sorted
    @param seeds: list, seeds to be used
    @return: time_elapsed: np.array
    """
    time_elapsed = np.zeros((len(seeds), length_list - 1))
    for i in range(1, length_list):
        for j, seed in enumerate(seeds):
            random.seed(seed)
            ls = list(range(i))
            random.shuffle(ls)
            time_elapsed[j, i - 1] = monkey_sort(ls)
    return time_elapsed


def plot_monkey_sort_time_dependency(time_elapsed, length_list, output_dir):
    """
    Plots graph based on the array with elapsed time (time against length of list to be sorted)
    @param time_elapsed: np.array
    @param length_list: int, length of lists to be sorted
    @param output_dir: output directory path
    @return: None, saves and shows figure of the time dependency
    """
    pd_time_elapsed = pd.DataFrame(time_elapsed, columns=list(range(2, length_list + 1)))
    pd_time_elapsed.boxplot(meanline=True, showmeans=True, showcaps=True,
                            showbox=True, showfliers=True, color="blue")
    plt.title("Runtime of monkey sort")
    plt.xlabel("Length of initial list")
    plt.ylabel("log(time)")
    plt.yscale("log")
    plt.savefig(Path(output_dir, "monkey_sort_time_dependencies.jpg"))
    plt.show()


def rainbow_color_stops(n, end=2/3):
    return np.array([ hls_to_rgb(end * i/(n-1), 0.5, 1) for i in range(n) ])


def random_walk(steps, output_dir):
    """
    Plots a graph of random walk, movement in upper, bottom, left, right direction of [-1, 1]
    @param steps: number of steps
    @param output_dir: output directory path
    @return:
    """
    loc = np.zeros((steps, 2))
    fig, ax = plt.subplots()
    for i in range(steps):
        loc[i, :] = loc[i-1, :] + np.random.randint(-1, 2, 2)
    alphas = np.arange(0.25, 0.75, step=0.5/steps)
    colors = rainbow_color_stops(steps)
    plt.scatter(loc[:, 0], loc[:, 1], alpha=alphas, c=colors, s=4)
    plt.plot(loc[:, 0], loc[:, 1], alpha=0.1, c="black")
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    plt.savefig(Path(output_dir, "random_walk.jpg"))
    plt.show()


def random_sierpinski_triangle(cycles, color, output_dir):
    """
    Draws Sierpinski's triangle by random method
    @param cycles: int, number of cycles
    @param color: str, color of the graph
    @param output_dir: output directory path
    @return: plot, saved as random_sierpinski_triangle.jpg
    """

    vertices = np.array([
        [0, 0],
        [0.5, (3**0.5)/2],
        [1, 0]
    ])

    coordinates = np.zeros((cycles, 2))
    coordinates[0, :] = (random.random(), random.random())
    for i in range(cycles):
        vertex = random.choice(vertices)
        coordinates[i, :] = 0.5*(coordinates[i-1, :] + vertex)

    plt.scatter(coordinates[:, 0], coordinates[:, 1], c=color)
    plt.savefig(Path(output_dir, "random_sierpinski_triangle.jpg"))
    plt.show()


def middle_replace(matchobj):
    """
    Shuffles the middle of a matchobject word if its length longer than 2 (only middle letters)
    @param matchobj: regex match object, word
    @return: s: str, shuffled word
    """
    s = matchobj.group(0)
    n = len(s)
    print(s)
    if n > 2:
        s = s[0] + ''.join(random.sample(s[1:n], n-2)) + s[n-1]
        return s
    else:
        return s


def replace(txt):
    """
    Shuffles the middle of the words (punctuation is not affected)
    @param txt: str, text
    @return: txt: str, shuffled text
    """
    pattern = r'\b\w+\b'
    return re.sub(pattern, middle_replace, txt)


if __name__ == '__main__':
    # Exercise 1: random number generation
    output_dir = "./"
    number_of_elements = ls_num(1, 100, 1) + ls_num(100, 10000, 10) + ls_num(10000, 100000, 100)
    num_seeds = 10
    seeds = np.random.randint(0, 100, num_seeds)
    rand_time_array, np_rand_time_array = calculate_random_time_array(number_of_elements=number_of_elements,
                                                                      seeds=seeds)
    plot_time_gen_list(rand_time_array=rand_time_array, np_rand_time_array=np_rand_time_array, output_dir=output_dir)

    # Exercise 2: Monkey sort time dependency
    random.seed(42)
    np.random.seed(42)
    length_list = 10
    time_elapsed = calculate_monkey_sort_time_dependency(length_list=length_list, seeds=seeds)
    plot_monkey_sort_time_dependency(time_elapsed=time_elapsed, length_list=length_list, output_dir=output_dir)

    # Exercise 3: Random walk
    steps = 100000
    random_walk(steps=steps, output_dir=output_dir)

    # Exercise 4: Sierpinski's triangle
    cycles = 1000
    random_sierpinski_triangle(cycles=cycles, color="purple", output_dir=output_dir)

    # Exercise 5: Shuffle the middle of words
    txt = """По рзеузльаттам илссоевадний одонго анлигсйокго унвиертисета, не иеемт занчнеия,
    в каокм проякде рсапжоолены бкувы в солве. Галовне, чотбы преавя и пслонедяя бквуы блыи на мсете.
    осатьлыне бкувы мгоут селдовтаь в плоонм бсепордяке, все-рвано ткест чтаитсея без побрелм.
    Пичрионй эгото ялвятеся то, что мы не чиаетм кдаужю бкуву по отдльенотси, а все солво цлиеком."""
    print(replace(txt))
