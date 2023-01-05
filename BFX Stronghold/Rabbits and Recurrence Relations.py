def iterative_rabbits(months, litter):
    """
    This function takes a given number of 'months' and 'litter' and returns the total number of rabbit pairs that will
    be present after n months. Begin with 1 pair of rabbits and in each generation, every pair of reproduction-age
    rabbits produces a litter of k rabbit pairs (instead of only 1 pair)
    :param months: The number of months
    :param litter: The number of rabbit pairs produced by each litter
    :return adults: Total number of rabbit pairs that will be present after n months
    """
    # initialize empty list for 'newborns' and counter for 'adults'
    newborns = []
    adults = 1

    # main recurrence relation
    for i in range(months-1):
        if i == 0:
            newborns.append(litter)
        else:
            newborns.append(adults*litter)
            adults += newborns[i-1]

    return adults


if __name__ == "__main__":
    n = int(input("What is the number of months? "))
    k = int(input("What is the number of reproduction-age rabbits produced in one litter? "))
    print(iterative_rabbits(n, k))
