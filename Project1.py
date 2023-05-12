from typing import Union

def power(x: Union[int, float], y: int, ans: Union[int, float]=1) -> Union[int, float]:
    """
    Computes the power of x raised to y.

    Args:
        x (int, float): The base value.
        y (int): The exponent value.
        ans (int, float): The initial value of the answer.

    Returns:
        int, float: The result of x raised to y.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, int) or not isinstance(ans, (int, float)):
        raise ValueError("Invalid input. x and ans should be integers or floats, y should be an integer.")
    if y < 0:
        raise ValueError("Invalid input. y should be a non-negative integer.")
    if y == 0:
        return ans
    else:    
        ans *= x
        return power(x, y-1, ans)

def cat_ears(n: int, total: int=0) -> int:
    """
    Computes the total number of cat ears for n cats.

    Args:
        n (int): The number of cats.
        total (int): The initial value of the total number of ears.

    Returns:
        int: The total number of cat ears.
    """
    if not isinstance(n, int) or not isinstance(total, int):
        raise ValueError("Invalid input. n and total should be integers.")
    if n < 0:
        raise ValueError("Invalid input. n should be a non-negative integer.")
    if n == 0:
        return total
    else:
        total += 2
        return cat_ears(n-1, total)

def alien_ears(n: int, total: int=0) -> int:
    """
    Computes the total number of alien ears for n aliens.

    Args:
        n (int): The number of aliens.
        total (int): The initial value of the total number of ears.

    Returns:
        int: The total number of alien ears.
    """
    if not isinstance(n, int) or not isinstance(total, int):
        raise ValueError("Invalid input. n and total should be integers.")
    if n < 0:
        raise ValueError("Invalid input. n should be a non-negative integer.")
    if n == 0:
        return total
    else:
        if n % 2 == 0:
            total += 2
        else:
            total += 3
        return alien_ears(n-1, total)
