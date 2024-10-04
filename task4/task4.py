import sys


def load_values(filename):
    nums = []
    with open(filename, 'r') as file:
        for line in file:
            nums.append(int(line))
    return nums


def main(file_path):
    nums = load_values(file_path)
    m = sorted(nums)[len(nums) // 2]
    count = sum(abs(v - m) for v in nums)
    print(count)


if __name__ == '__main__':
    main(sys.argv[1])

