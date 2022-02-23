def sal():
    try:
        time = float(input('Выработка в часах:'))
        salary = int(input('Ставка в $:'))
        bonus = int(input('Премия в $:'))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')


sal()
