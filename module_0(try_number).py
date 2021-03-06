import numpy as np # импортируем бибилиотеку, которая позволяет обрабатывать большие массивы данных

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls)) # расчитваем среднее арифметическое значение элементов списка 
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
    
def game_core_v3(number):
    global a # назначем глобальную переменную, чтобы она была видна за пределами функции
    a = 1 # нижняя граница диапазона
    global b # назначем глобальную переменную, чтобы она была видна за пределами функции
    b = 100 # верхняя граница диапазон
    count = 1 # назначаем счетчик, который считает количество итераций
    predict = np.random.randint(a, b) # с помощью библиотеки random выбираем нужное целое число (integer) в заданном диапазоне 
    mid_range = round(b/2) # для бинарного поиска назначаем переменную - середину диапазона
    while mid_range != predict: # задаем условие, при котором цикл будет выполняться
        if mid_range > predict: 
            b = mid_range # сужаем диапазон поиска наполовину, до или после середины списка. 
                          # в этом случае от 1 до 50, тк диапазон от 1 до 100
        else:
            a = mid_range # сужаем диапазон поиска наполовину, до или после середины списка. 
                          # в этом случае от 50 до 100, тк диапазон от 1 до 100
        mid_range = a + round((b - a) / 2) # рассчитываем середину сокращенного диапазона
        count += 1 
    return(count) 

print (score_game(game_core_v3))