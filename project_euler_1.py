n = 1000
n_15 = 15
n_5 = 5
n_3 = 3
num_5 = (n - n % n_5) / n_5
num_3 = (n - n % n_3) / n_3
num_15 = (n - n % n_15) / n_15

if n % n_15 == 0:
    sum_15 = 15 * ((num_15 - 1) * (num_15 / 2))
else:
    sum_15 = 15 * ((num_15) * ((num_15 + 1) / 2))

if n % n_5 == 0:
    sum_5 = 5 * ((num_5 - 1) * (num_5 / 2))
else:
    sum_5 = 5 * ((num_5) * ((num_5 + 1) / 2))

if n % n_3 == 0:
    sum_3 = 3 * ((num_3 - 1) * (num_3 / 2))
else:
    sum_3 = 3 * ((num_3) * ((num_3 + 1) / 2))

print(sum_5+sum_3-sum_15)


