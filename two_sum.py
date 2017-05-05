
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index = []
        numtosort = num[:]; numtosort.sort()
        i = 0; j = len(numtosort) - 1
        while i < j:
            if numtosort[i] + numtosort[j] == target:
                for k in range(0,len(num)):
                    if num[k] == numtosort[i]:
                        index.append(k)
                        break
                for k in range(len(num)-1,-1,-1):
                    if num[k] == numtosort[j]:
                        index.append(k)
                        break
                index.sort()
                break
            elif numtosort[i] + numtosort[j] < target:
                i = i + 1
            elif numtosort[i] + numtosort[j] > target:
                j = j - 1

        return (index[0]+1,index[1]+1)

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum_V2(self, num, target):
        



def main():
  num = [5,4,3,2,1]
  target= 6
  ans=[]
  sol = Solution()
  ans = sol.twoSum(num,target)      
  print ans



if __name__ == "__main__":
    main()


