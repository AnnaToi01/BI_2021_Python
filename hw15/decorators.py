import functools
import time
from typing import Callable, TypeVar, ParamSpec, Any
import random
import requests


T = TypeVar('T')
P = ParamSpec('P')


# Exercise 1
def measure_time(func: Callable[P, T]) -> Callable[P, T]:
    """
    Prints the runtime of the decorated function.
    @param func: function, to be decorated
    @return: wrapper_measure_time, function, wrapper function
    """
    @functools.wraps(func)
    def wrapper_measure_time(*args: P.args, **kwargs: P.kwargs) -> T:
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        print(end_time - start_time)
        return value

    return wrapper_measure_time


@measure_time
def some_function(a, b, c, d, e=0, f=2, g='3'):
    time.sleep(a)
    time.sleep(b)
    time.sleep(c)
    time.sleep(d)
    time.sleep(e)
    time.sleep(f)
    return g


# Exercise 2
def function_logging(func: Callable[P, T]) -> Callable[P, T]:
    """
    Prints the positional and keyword arguments of the decorated function.
    @param func: function, to be decorated
    @return: wrapper_measure_time, function, wrapper function
    """
    @functools.wraps(func)
    def wrapper_function_logging(*args: P.args, **kwargs: P.kwargs) -> T:
        value = func(*args, **kwargs)
        # Input positional and keyword arguments
        if args and kwargs:
            kw_str = ", ".join(f"{key}={value}" for key, value in kwargs.items())
            print(f"Function {func.__name__} is called "
                  f"with positional arguments {args} "
                  f"and with keyword arguments {kw_str}")
        elif args:
            print(f"Function {func.__name__} is called "
                  f"with positional arguments {args} ")
        elif kwargs:
            kw_str = ", ".join(f"{key}={value}" for key, value in kwargs.items())
            print(f"Function {func.__name__} is called "
                  f"with keyword arguments {kw_str}")
        else:
            print(f"Function {func.__name__} is called with no arguments")
        # Output type
        print(f"Function {func.__name__} returns output of type {type(value).__name__}")
        return value

    return wrapper_function_logging


@function_logging
def func1():
    return set()


@function_logging
def func2(a, b, c):
    return (a + b) / c


@function_logging
def func3(a, b, c, d=4):
    return [a + b * c] * d


@function_logging
def func4(a=None, b=None):
    return {a: b}


# Exercise 3
def russian_roulette_decorator(probability: float = 0.2, return_value: Any = "Ooops, your output has been stolen"):
    """
    Makes the decorated function return the value (return_value) with given probability
    @param probability: float, probability to return return_value
    @param return_value: Any, return value
    @return: russian_roulette, function
    """
    def russian_roulette(func):
        def russian_roulette_wrapper(*args, **kwargs):
            if random.random() < probability:
                return return_value
            else:
                return func(*args, **kwargs)
        return russian_roulette_wrapper
    return russian_roulette


@russian_roulette_decorator(probability=0.2, return_value="Ooops, your output has been stolen")
def make_request(url):
    return requests.get(url)


# Additional exercise 1
def staticmethod_alt(func: Callable[P, T]) -> Callable[P, T]:
    """
    Returns a static method for a function passed as the parameter.
    Alternative to staticmethod.
    @param func: function, to be decorated
    @return: wrapper_staticmethod_alt, function, wrapper function
    """
    @classmethod
    @functools.wraps(func)
    def wrapper_staticmethod_alt(*args: P.args, **kwargs: P.kwargs) -> T:
        return func(*args[1:], **kwargs)
    return wrapper_staticmethod_alt


# Additional exercise 2
def dataclass_alt(original_class: object) -> T:
    """
    Adds generated special methods to the class
    Alternative to dataclass.
    @param original_class: class, to be decorated
    @return: DataClassWrapper, class, wrapped class
    """
    class DataClassWrapper(original_class):
        def __init__(self, *args: P.args, **kwargs: P.kwargs) -> None:
            """Class constructor"""
            # Args
            for i, arg in enumerate(args):
                setattr(self, list(original_class.__annotations__.keys())[i], arg)

            # Kwargs
            for key, value in kwargs.items():
                if key in original_class.__annotations__:
                    self.__dict__[key] = value
                else:
                    raise TypeError(f"{original_class.__name__}.__init__() got an unexpected keyword argument '{key}'")

            # Default parameters
            for key, value in original_class.__annotations__.items():
                if key in self.__dict__:
                    pass
                else:
                    self.__dict__[key] = dict(original_class.__dict__)[key]

            # match_args
            if "__match_args__" in original_class.__dict__:
                self.__match_args__ = original_class.__match_args__(self)
            else:
                self.__match_args__ = tuple(original_class.__annotations__.keys())

            DataClassWrapper.__name__ = original_class.__name__

        # This is a function in case, the order of the variables in the printed string matters
        # Here it corresponds to the order of the defined attributes
        # def __repr__(self) -> str:
        #     # Dictionary of attributes
        #     attribute_dictionary = {}
        #     for i in original_class.__annotations__:
        #         attribute_dictionary[i] = self.__getattribute__(i)
        #     arg_str = ", ".join(f"{key}={value}" for key, value in attribute_dictionary.items())
        #     return f"{DataClassWrapper.__name__}({arg_str})"

        def __repr__(self) -> str:
            """Class representation"""
            # Do not overwrite __repr__ if already in the original class
            if "__repr__" in original_class.__dict__:
                return original_class.__repr__(self)
            else:
                # The string for print
                arg_str = ", ".join(f"{key}={value}"
                                    for key, value in self.__dict__.items()
                                    if not key.startswith("__match_args__"))
                return f"{DataClassWrapper.__name__}({arg_str})"

        def __eq__(self, other: object) -> bool:
            """Check if equal"""
            # Do not overwrite __eq__ if already in the original class
            if "__eq__" in original_class.__dict__:
                return original_class.__eq__(self, other)
            else:
                if not isinstance(other, DataClassWrapper):
                    return NotImplemented
                return (
                    self.__dict__ == other.__dict__
                )

    return DataClassWrapper


@dataclass_alt
class User:
    first_name: str
    last_name: str
    email: str

    def get_email(self) -> str:
        """
        Return email of the User
        @return: email, str
        """
        return self.email

    @staticmethod_alt
    def is_adult(age: int) -> bool:
        """
        Check if adult
        @return: bool, True/False
        """
        return age >= 18


if __name__ == "__main__":
    # Exercise 1
    some_function(1, 2, 3, 4, e=5, f=6, g="99999")

    # Exercise 2
    print(func1(), end="\n\n")
    print(func2(1, 2, 3), end="\n\n")
    print(func3(1, 2, c=3, d=2), end="\n\n")
    print(func4(a=None, b=float("-inf")), end="\n\n")

    # Exercise 3
    for _ in range(10):
        print(make_request("https://google.com"))

    # Additional exercise 1
    user1 = User(last_name='Иванов', first_name='Иван', email='ivan.ivanov@somemailbox.com')
    user2 = User(first_name="Ваня", last_name='Ермолаев', email='vania.ermolaev@somemailbox.com')

    print(User.is_adult(age=20))
    print(user1.is_adult(age=17))

    # Additional exercise 2
    print(user1.__match_args__)
    print(user1.__eq__(user2))
    print(user1)
