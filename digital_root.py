def digital_root(n):
    new_num = 0
    for num in str(n):
        new_num += int(num)
    return (new_num if new_num < 10 else digital_root(new_num))