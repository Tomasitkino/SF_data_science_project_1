"Guess the number"

import numpy as np


def random_predict(number: int = 1) -> int:
    """[summary]

    Args:
        number (int, optional): [description]. Defaults to 1.

    Returns:
        int: [description]
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break

    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем угадывает наш подход

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


print(f'Количество попыток: {random_predict(10)}')
