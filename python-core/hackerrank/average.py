# 2 5 -> 3.50
def avg(*nums):
    """ average of list passed as nums """
    sum = 0.0  # define the sum as float
    for n in nums:
        sum += n

    return sum / len(nums)  # divide by nums length


def avg2(*nums):
    return sum(nums) / len(nums)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nums = map(int, raw_input().split())
    nums = (2, 5)
    res = avg(*nums)

    # fptr.write('%.2f' % res + '\n')
    # fptr.close()
    print('%.2f' % res + '\n')
    print(f'{avg2(*nums)}')
