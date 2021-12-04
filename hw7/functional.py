def sequential_map(*args):
    """
    Takes an arbitrary number of functions as arguments, last argument should be a list
    Applies them to the list and returns the modified list
    @param args: functions and a list
    @return: modified list after applying functions
    """
    assert len(args) >= 2, "There should be at least one function, and a list"
    assert isinstance(args[-1], list), "Last argument should be a list"
    ls = args[-1].copy()
    func_ls = args[:-1]
    # for func in func_ls:
    #     ls = list(map(func, ls))
    # return ls #This is without using func_chain
    return func_chain(*func_ls)(ls)


def consensus_filter(*args):
    """
    Takes an arbitrary number of functions as arguments (return True or False)
    Last argument should be a list
    Applies them sequentially to the list and returns values that remained True
    @param args: functions and a list
    @return: ls: list, modified list after applying functions
    """
    assert len(args) >= 2, "There should be at least one function, and a list"
    assert isinstance(args[-1], list), "Last argument should be a list"
    ls = args[-1].copy()
    func_ls = args[:-1]
    for func in func_ls:
        # tf = list(sequential_map(func, ls))
        # ls = [i[0] for i in zip(ls, tf) if i[1]] #Use this if you want to avoid filter function
        ls = list(filter(func, ls))
    return ls


def conditional_reduce(func1, func2, input_ls):
    """
    Takes two functions and a list, return modified list after application of functions
    @param func1: function, returns True or False for each value in list, takes one argument (list)
    @param func2: function, takes two arguments
    @param input_ls: list, functions are going to applied to it
    @return: ls: list
    """
    ls = list(filter(func1, input_ls))
    assert len(ls) >= 2, "Filtered list is less than 2 elements long"
    v1 = ls[0]
    for v2 in ls[1:]:
        v1 = func2(v1, v2)
    return v1


def func_chain(*args):
    """
    Returns a function uniting all input function in sequential order
    @param args: functions
    @return: inner_func: function
    """
    def inner_func(inner):
        """
        Returns the resulting value after application of function
        @param inner: argument for the function
        @return: inner: results of function
        """
        for func in args:
            inner = func(inner)
        return inner
    return inner_func


def multiple_partial(*args, **kwargs):
    """
    Takes functions and kwargs could be applied to all of them
    @param args: functions
    @param kwargs: keyword arguments, applied to each function
    @return: functions: list, with modified keyword arguments
    """
    def wrapper(func, **inner_kwargs):
        """
        Takes function as func and returns it together with the passed keyword arguments
        @param func: function
        @param inner_kwargs: keyword arguments to modify func
        @return inner_wrapper: function, with modified keyword arguments
        """
        def inner_wrapper(*final_args, **final_kwargs):
            """
            Inner wrapper:
            Takes additional arguments and keyword arguments, returns function with them
            @param final_args: additional arguments
            @param final_kwargs: additional keyword arguments
            @return: func: function, with all the keywords modified
            """
            return func(*final_args, **inner_kwargs, **final_kwargs)
        return inner_wrapper
    func_ls = []
    for func in args:
        func_ls.append(wrapper(func, **kwargs))
    return func_ls
