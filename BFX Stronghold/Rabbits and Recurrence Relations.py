def recursive_rabbits(months, litter):
    newborns = []
    adults = 1
    for i in range(months-1):
        if i == 0:
            newborns.append(litter)
        else:
            newborns.append(adults*litter)
            adults += newborns[i-1]

    return adults


if __name__ == "__main__":
    print(recursive_rabbits(31, 3))
