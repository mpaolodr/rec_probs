def bunny_ears(n):

    if n == 0:

        return 0

    if n == 1:

        return 2

    return bunny_ears(n - 1) + 2


print(bunny_ears(20))
