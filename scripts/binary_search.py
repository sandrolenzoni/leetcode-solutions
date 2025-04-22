class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        low = 0 
        hight = len(nums) -1 
        while low <= hight:
          mid = (hight + low) // 2
          if nums[mid] < target:
              low = mid + 1
          elif nums[mid] > target:
              hight = mid - 1
          else:
              return mid          

        return -1

if __name__ == '__main__':
    print('BINARY SEARCH')
    solution = Solution()
    print(solution.search(
      nums=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
      target=67  
    ))


    