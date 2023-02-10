n = 35
def sum_inc(n , inc):
    n_lower = n - 1
    num = (n_lower - n_lower % inc) / inc
    sum= inc * ((num) * ((num + 1) / 2))
    return sum

def total_sum(n):
    print(sum_inc(n, 5) +sum_inc(n, 3)-sum_inc(n, 15) )
    return sum_inc(n, 5) +sum_inc(n, 3)-sum_inc(n, 15)

total_sum(n)

### way number dos
def smooth_sum(n):
    smoothsum = 0
    for i in range(n):
        if i % 3 == 0:
            smoothsum = smoothsum+ i
        if i % 5 == 0:
            smoothsum = smoothsum + i
        if i % 15 == 0:
            smoothsum = smoothsum - i
    print(smoothsum)
    return smoothsum

smooth_sum(n)





