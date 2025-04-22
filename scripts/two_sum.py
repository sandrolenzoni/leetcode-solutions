class Solution(object):
  def twoSum(nums: list[int], target:int) -> list[int]:
    hasher = {}
    for index, num in enumerate(nums):
      if hasher.get(num) is not None:
        return [hasher.get(num), index]
      hasher[target-num] = index


if __name__ == "__main__":
  print('TARGET 5:')
  print(Solution.twoSum(nums=[1,2,3], target=5))
  print('TARGET 9:')
  print(Solution.twoSum(nums=[2,7,11,15], target=9))