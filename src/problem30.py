def fifth_power_sum(n):
    n_sum = 0
    while n >= 10:
        d = n % 10
        n = int(n / 10)
        n_sum += d**5
    n_sum += n ** 5
    return n_sum


numbers = [i for i in range(10, 1000000) if i == fifth_power_sum(i)]
print(numbers, sum(numbers))
