def count_ways(n, memo = dict()):
    memo[0] = 0
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4
    if n in memo:
        return memo[n]
    for i in range(4,n+1):
        memo[i] = count_ways(i-3, memo) + count_ways(i-2, memo) + count_ways(i-1, memo)
    return memo[n]


if __name__ == "__main__":
    print("For {} steps there are {} ways".format(4, count_ways(4)))
    print("For {} steps there are {} ways".format(5, count_ways(5)))
    print("For {} steps there are {} ways".format(6, count_ways(6)))
    print("For {} steps there are {} ways".format(40, count_ways(40)))






