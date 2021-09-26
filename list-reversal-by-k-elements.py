def rightRotate(nums, ag):
    """
    Rotate nums list by ag number of elements using in-place technique.
    """
    for _ in range(ag):
        nums.reverse()
        nums[1:len(nums)] = reversed(nums[1:len(nums)])
    return nums
    
def main():
    nums = [1,2,3,4,5,6,7]
    ag = 3
    rotated_nums = rightRotate(nums, ag)
    print(rotated_nums)
    
if __name__ == '__main__':
    main()