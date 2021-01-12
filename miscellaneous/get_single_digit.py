def get_single_digit(number):
    try:
        sum = 0
        a=[int(i) for i in str(number) ]
        for j in a:
            sum += j
        if len(str(sum)) != 1:
            return get_single_digit(sum)
        else:
            return sum
    except Exception as e:
        print("Exception {}".format(e))


b= get_single_digit('1ss099')
