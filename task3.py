month = 1


def money(deposit, desired_amount, annual_percent, month):
    result = annual_percent/12 * deposit + deposit
    if desired_amount <= result:
        return f'Вот столько месяцев: {month}'
    elif desired_amount != result:
        deposit = result
        month += 1
        return money(deposit, desired_amount, annual_percent, month)


print(money(100000, 1500, 0.12, month))
