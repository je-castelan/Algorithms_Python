
def twoSumv2(nums,target):
    listdiffs = {}
    for i in range(len(nums)):
        if listdiffs.get(nums[i]) is None:
            diff = target - nums[i]
            listdiffs[diff] = i
        else:
            return [listdiffs[nums[i]],i]

def twoSumv1(nums,target):
    for i in range(len(nums)):
        diff = target - nums[i]
        options = nums[i+1:]
        if diff in options: #This comparison represents than python will try a internal search
            return [i, options.index(diff)+i+1]


def printResult(nums, target):
    print("*"*100)
    print("Indexes which sums {} in {} are {} in version 1".format(target,nums, twoSumv1(nums,target)))
    print("Indexes which sums {} in {} are {} in version 2".format(target,nums, twoSumv2(nums,target)))


if __name__ == "__main__":
    printResult([2,7,11,15],9) #[0,1]
    printResult([3,2,4],6) #[1,2]   
    printResult([3,3],6) #[0,1]
    printResult([3,2,3],6) #[0,2]