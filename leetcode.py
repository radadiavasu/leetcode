########## Testing ##########

# def main(arr, n):
#     visited = [False for i in range(n)]
    
#     for i in range(n):
#         if visited == True:
#             continue
        
#         count = 1
#         for j in range(n+1, n,1):
#             if arr[i] == arr[j]:
#                 visited[j] = True
#                 count += 1
#                 return max(arr)
#         print(arr[i], count)
        
# if __name__ == "__main__":
#     arr = [1,2,2,3,1,4]
#     mexu = max(arr)
#     print(mexu)
#     n = len(arr)
#     main(arr, n)


########## 1. Find frequencies of each inlcuding duplicate elements. Let's solve it. ##########

# arr = [1,2,2,3,1,4]
# element_count = {}

# for ele in arr:
#     if ele in element_count:
#         element_count[ele] += 1
#     else:
#         element_count[ele] = 1
        
# for key,value in element_count.items():
#     print(f"{key}, {value}")


#----------------------------------->
# Contain Duplicate. Let's solve it.#
#<-----------------------------------

# nums = [1,2,3,1]
# ele = len(nums)

# if ele in nums:
#     print(False)
# else:
#     print(True)
    

########## 1. Find Common elements form 2 arrays. Let's solve it. ##########

# nums1 = [1,2,3]
# nums2 = [2,4]
# i = j = 0
# common = float('inf')

# while i < len(nums1) and j < len(nums2):
#     if nums1[i] == nums2[j]:
#         common = min(common, nums1[i])
#         i += 1
#         j += 1
#     elif nums1[i] < nums2[j]:
#         i += 1
#     else:
#         j += 1


# if common == float('inf'):
#     print(-1)
# else:
#     print(common)


########## 2. Find minimum common values form 2 arrays. Let's solve it. ##########

# nums1 = [1,2,3]
# nums2 = [2,4]

# set1 = set(nums1)
# set2 = set(nums2)

# common = set1.intersection(set2)

# if common:
#     print(min(common))
# else:
#     print(-1)


#----------------------------------------------->
# 1. Intersaction of two arrays. Let's solve it.#
#<-----------------------------------------------

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

# set1 = set(nums1)
# set2 = set(nums2)

# common = set1 & set2

# if common:
#     print(list(common))
# else:
#     print([])


########## Testing ##########
# nums = [2,2,1]

# print(2*sum(set(nums))-sum(nums))


#---------------->
# Is Subsequence.#
#<----------------

# n,m = len(s), len(t)
# i,j = 0,0
# while i==n and j==m:
#     if s[i] == t[j]:
#         i += 1
#     j += 1
# print(i == n)


#--------------------->
# Match word patterns.#
#<---------------------

# pattern = "abba"; s = "dog cat cat dog"

# words = s.split()
# if len(pattern) != len(words):
#     print(False)

# word_to_char = {}
# char_to_word = {}

# for char, word in zip(pattern, words):
#     if char not in char_to_word:
#         char_to_word[char] = word
#     else:
#         if char_to_word[char] != word:
#             print(False)
            
#     if word not in word_to_char:
#         word_to_char[word] = char
#     else:
#         if word_to_char[word] != char:
#             print(False)
# print(True)   


#--------------->
# Valid Anagram.#
#<---------------

# s = "anagrams"; t="nagramas"

# two_sorted, two_sorted_1 = sorted(s), sorted(t)

# if len(two_sorted) == len(two_sorted_1):
#     print(True)
# else:
#     print(False)


########## Testing ##########
# s = "4193"

# digit = []
# x = s.split()
# for i in x:
#     if i.isnumeric():
#         digit.append(int(i))
# print(digit)


#----------------------->
# Find majority element.#
#<-----------------------

# from collections import Counter
# s = [1,2,3,4,4,4,3]
# converter = Counter(s)
# length = len(s)

# for key, values in converter.items():
#     if (values > (length/2)):
#         pass
# print(key)


########## 2. Second way ##########

# s = [1,2,3,4,4,4,3]; target = 4
# count = 0
# for i in range(len(s)):
#     if s[i] == target:
#         count = s
# # print(max(list(s)))
# print(s)

########## 3. Third way ##########

# s = [1,2,2,3,3,4,4]

# store = {}
        
# for i in s:
#     try:
#         store[i]+=1
#     except:
#         store[i]=1
        
# for j in store:
#     if store[j] > 1:
#         print(j)
  
  
#------------------------>
# Search insert position.#
#<------------------------

# import bisect      
# nums = [1,3,4,5,3,5,6]
# target = 2

# insert = bisect.bisect_right(nums,target)
# print(insert)


########## 2. Another method. ##########

# l = len(nums)
# r = len(nums)
# for i in range(l):
#     for j in range(r-1):
#         mid = l+r // 2
#         if nums[i] <= target:
#             i = i+1
#         elif nums[r] > target:
#             j = j+1
#         else:
#             print(i)
# print(mid)


#--------------->
# Single number.#
#<---------------

# from collections import Counter
# nums = [2,1,2,5]

# c = Counter(nums)

# ans = [item[0] for item in c.items() if item[1] == 1]
# print(ans)


#------------>
# Add Digits.#
#<------------

# nums = 38

# ans = (nums-1) % 9 +1

# print(ans)


#-------------------------->
# Remove Duplicate Letters.#
#<--------------------------

# s = "cbacdcbc"
# print(sorted(set(str(s))))


########## 1. First method ##########

# s = "cbacdcbc"
# ans = []

# for i in s:
#     if i not in ans:
#         ans.append(i)
        
# print(ans)


#------------->
# Add Strings.#
#<-------------

# num1 = "456"
# num2 = "77"

# # i,j = len(num1), len(num2)

# ans = int(num1) + int(num2)

# print(ans)

# Find all Duplicate elements in an array (return only duplicates.)
# a = [1,1,2,3,4]
# import collections
# print([item for item, count in collections.Counter(a).items() if count > 1])
# c = collections.Counter(a)
# for item,count in c.items():
#     if count > 1:
#         print(a)
# print(a)


#----------------------------------------->
# Find the Duplicate elements in an array.#
#<-----------------------------------------

# Getting index number of duplicates.
# nums = [1,1,2,3,4,4]
# dupu = []
# for n,x in enumerate(nums):
#     if nums.count(x) > 1:
#         dupu.append(n)
# print(dupu)

########## 2. Getting both duplicate values i.e [1,2,3,4,4], o/p [4,4] ##########

# nums = [1,1,2,3,4,4]
# dupu = []
# for i in nums:
#     if nums.count(i) > 1:
#         dupu.append(i)
# print(dupu)

########## 3. Finally getting duplicates in list. ##########

# nums = [1,1,2,3,4,4]
# dupu = []
# for i in nums:
#     if nums.count(i) > 1 and i not in dupu:
#         dupu.append(i)
# print(dupu)

# 3. With using set method.
# nums = [1,1,2,3,4,4]
# dupu = set()
# for i in nums:
#     if i in dupu:
#         print(i)
#     else:
#         print(dupu.add(i))


#-------------->
# Keyboard Row.#
#<--------------

# def find_words(words):
#     row_mapping = {
#         'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
#         'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
#         'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3
#     }
    
#     matching_words = []
#     for word in words:
#         row = row_mapping[word[0].lower()]
#         if all(row_mapping[char.lower()] == row for char in word):
#             matching_words.append(word)
#     return matching_words

# # Example usage
# words = ["Hello", "Alaska", "Dad", "Peace"]
# matching_words = find_words(words)
# print("Matching words:", matching_words)


#----------------->
# Teemo Attacking.#
#<-----------------

# timeSeries = [1,4]
# duration = 2

# td = 0
# n = len(timeSeries)

# for i in range(n-1):
#     if timeSeries[i+1] - timeSeries[i] < duration :
#         td += timeSeries[i+1] - timeSeries[i] < duration
#     else:
#         td += duration
        
# td += duration
# print(td)


################# work for just first test case. #################

# timeSeries = [1,4]
# duration = 2
# i = len(timeSeries), 0
# j = len(timeSeries), 0

# count = duration

# while i<j:
#     if count[i] != count[j]:
#         count[i] += 1
#         count[j] += 1
# total = len(i) + len(j)
# print(total)


# ---------------------------->
# Student attendence record 1.#
#<------------------------------

# s = "PPAAAALL"

# p = s.count("LLL")
# q = s.count("AAAA")

# if p or q:
#     print(False)
# else:
#     print(True)


#------------------------>
# Most Booked Hotel Room.#
#<------------------------

# n = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]

# a = {}

# for count in n:
#     if count not in a:
#         a[count] = 1
#     else:
#         a[count] += 1
# cl = 0
# k = ""

# for pp in a:
#     if a[count] > cl:
#         cl = a[count]
#         k = pp

# print(k)


# Second Way

########## Testing ##########
# Single Number

# a = [2,2,1]

#--------------------------->
# Reverse Words in a String.#
#<---------------------------

# First method

# s = "the sky is blue"

# for i in s:
#     if i:
#         continue
# print(" ". join(s.split()[::-1]))


########## Second method ##########

# s = "the sky is blue"
# spliting = s.split()

# slow, fast = 0, len(spliting)-1

# while slow < fast:
#     spliting[slow], spliting[fast] = spliting[fast], spliting[slow]
#     slow += 1
#     fast -= 1
# print(" ". join(spliting))


#-------------------->
# Contains Duplicate 2
#<--------------------#

# nums: int = [1,0,1,1]
# k: int = 1

# i: int = 0

# while i < len(nums):
#     j = i + 1
#     while j < min(i+k+1, len(nums)):
#         if nums[i] == nums[j]:
#             print(True)
#             break
#         j += 1
#     else:
#         i += 1
#         continue
#     break
# else:
#     print(False)


#---------->
# Two Sum 2
#<---------#

# nums = [-1,0]
# target = -1
# for k,i in enumerate(nums,start=1):
#     print("k",k,"value",i)
#     for p in range(k,len(nums)):
#         print("k",k,"p",p)
#         print("i value",i,"p value",nums[p])
#         if i + nums[p]== target:
#             print(k,p+1)
# print([])


########## 2. Second Way ##########

# nums = [-1,0]
# target = -1
# for i, j in enumerate(nums,1):
#     for p in range(i,len(nums)):
#         if j + nums[p]== target:
#             print([i,p+1])
    
# print([])


#---------------->
# Basic Calculator
#<---------------#

# s = "(1+(4+5+2)-3)+(6+8)"

# stack = []
# num = 0
# sign = 1
# result = 0

# for char in s:
#     if char.isdigit():
#         num = num * 10 + int(char)
#     elif char == '+':
#         result += sign * num
#         num = 0
#         sign = 1
#     elif char == '-':
#         result += sign * num
#         num = 0
#         sign = -1
#     elif char == '(':
#         stack.append(result)
#         stack.append(sign)
#         result = 0
#         sign = 1
#     elif char == ')':
#         result += sign * num
#         num = 0
#         result *= stack.pop()
#         result += stack.pop()
            
# print(result + sign * num)


########## 2. Second method ##########

###### It may conflit in larger inputs ######

# s = "(1+(4+5+2)-3)+(6+8)"

# t = eval(s)

# print(t)


########### Testing ###########
# s = "lee(t(c)o)de)"

# l = len(s), 0
# r = len(s), 0
# open = set('(')
# close = set(')')
# match = {')': '('}
# stack = []

########### Testing ###########

#----->
# 3Sum
#<----#

# 1. Static version not moving
# nums = [-1,0,1,2,-1,-4]

# empty = []

# i,j,k = 0,1,2

# while i < j < k:
#     if nums not in empty:
#         final = nums[i] + nums[j] + nums[k]
#         empty.append(final)
#         if final == 0:
#             print([nums[i], nums[j], nums[k]])
#         else:
#             print([])
#     break
# print(empty)


########## 2. Final result. ##########

# nums = [-1,0,1,2,-1,-4]
# nums.sort()
# triplets = []

# for i in range(len(nums) -2):
#     if i > 0 and nums[i] == nums[i - 1]:
#         continue
    
#     left, right = i + 1, len(nums) -1
#     while left < right:
#         total = nums[i] + nums[left] + nums[right]
        
#         if total == 0:
#             triplets.append([nums[i], nums[left], nums[right]])
            
#             while left < right and nums[left] == nums[left + 1]:
#                 left += 1
#             while left < right and nums[right] == nums[right - 1]:
#                 right -= 1
        
#             # Move pointers
#             left += 1
#             right -= 1
#         elif total < 0:
#             left += 1
#         else:
#             right -= 1
# print(triplets)


#-------------------------->
# Strings to Integers (atoi)
#<-------------------------#

# 1. Not working in real time gives wrong answer due to integer overflow in 32-bits integer.

# my_string = "words and 987"
# result_string = ""
# index = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# for i in my_string.strip():
#    if i not in index:
#         result_string += i

# print(result_string)


# 2. Not working handling integer overflow in 32-bits integer (same as first).

# my_string = "-91283472332"
# result_string = ""

# for i in my_string.strip():
#     if i.isdigit() or (i == "-" and not result_string) or (i == "+" and not result_string):
#         result_string += i
#     else:
#         result_string
#         break

# print(result_string)


# 2. Final Working Condition

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         result_string = ""
#         for i in s.strip():
#             if i.isdigit() or (i == "-" and not result_string) or (i == "+" and not result_string):
#                 result_string += i
#             else:
#                 break

#         if result_string and result_string != "-" and result_string != "+":
#             result_int = int(result_string)
#             if result_int > 2147483647:
#                 return 2147483647
#             elif result_int < -2147483648:
#                 return -2147483648
#             else:
#                 return result_int
#         return 0
    
# obj = Solution()
# s = "-91283472332"
# obj.myAtoi(s)
# print(s)

#---------------------->
# Top K frequent element.
#<----------------------#

# 1. Not working properly. Testcase error.
# nums = [1,2]; k = 2

# lst = []
# for num in nums:
#     if nums.count(num)>=k:
#         lst.append(num)
        
# print(list(set(lst)))


#--------------------------------------------------------------> 
# Learning purpose Couting left and right elements of the array. 
# <------------------------------------------------------------#

# array = [1,2,3,4,5]

# left = 0
# right = len(array) - 1
# middle = (left + right) // 2 # (0 + 4)) // 2
# # print(middle)  # Ans = 2

# left_count = []
# right_count = []

# while left <= right:
#     if array[left] <= array[middle]:
#         left_count.append(array[left])
#         left += 1
#     if array[right] >= array[middle]:
#         right_count.append(array[right])
#         right -= 1
        
# # print(array[right])
# print("Left counting", left_count)
# print("Right counting", right_count)


#-------------------------------------------->
# Learning purpose Increasing elemnt with + 1. 
# <------------------------------------------#

# arr = [1,2,3,4]
# store = []
# move = 0

# for _ in arr:
#     if arr[move] not in store:
#         arr[move] += 1
#         store.append(arr[move])
# print(store)

#------------------------->
# Longest Common Sequence.
#<------------------------#

########## 1. Working. ##########

# nums = [100,4,200,1,3,2]

# nums.sort()
# n = len(nums)
# v = []
# ans = 0
# count = 0
# v.append(nums[0])

# for i in range(1, n):
#     if (nums[i] != nums[i - 1]):
#         v.append(nums[i])

# for i in range(len(v)):
#     if (i > 0 and v[i] == v[i - 1] + 1):
#         count += 1
        
#     else:
#         count = 1
        
#     ans = max(ans, count)
    
# print(ans)


######### 2. Working and very easy solution. #########

# nums = [100,4,200,1,3,2]

# if not nums: print(0)

# nums.sort()

# maxlen = 1 # For minimum value for find max consecutive sequence from 1.
# currlen = 1 # Required minimum 1 ele for starting to count sequence.

# for i in range(1, len(nums)):
#     if (nums[i] == nums[i-1] +1): # Matching with previous value if its equal than...
#         currlen += 1 # Increasing by 1.
#     elif (nums[i] != nums[i-1]): # Otherwise.... 
#         '''For Example if currlen is 200 and maxlen is 4 so reset currlen is 1, 
#         and start counting from 1.
#         because it's not sequence wise.'''
#         maxlen = max(maxlen, currlen) # Return max of maxlen and currlen.
#         currlen = 1 # Reset by 1 if currlen != maxlen.

# print(max(maxlen, currlen))


# For testcase
# word = "abcdefd"; ch = "d"

# length = ""

# for i in range(0, len(word)):
#     if word[i] == ch:
#         print(True)
# print(False)


#<--------------------------------------------------------
# Largest Positive Integer That Exists With Its Negative.#
#-------------------------------------------------------->

# For testcases.

############# 1. Rough purpose.#############

# nums = [-1,2,-3,3]

# i = 0
# j = 0


# while i < j:
#     if nums[i] != nums[j]:
#         ans = nums[i] - nums[j]
#         nums[i] += 1
#         nums[j] += 1
#     if ans == 0:
#         pass
# print(nums[j])


############### 2. Working but not in 2nd testcase with return max integer. i.e [-1,3,4,7,-7,1] o/p = 7 but gives me 1.#####################

# def findPositive(nums):
#     i = 0
#     j = len(nums) - 1
    
#     while i < j:
#         if nums[i] != -nums[j]:
#             ans = nums[i] + nums[j]
#             if ans == 0:
#                 return nums[i]
#         i += 1
#         j -= 1

#     return -1

# nums = [-1, 2, -3, 3]
# obj = findPositive(nums)
# print(obj)

####################
# 1. Working Approach.
####################

# def findPositive(nums):
#     i = 0
#     j = 0
#     max_value = float("-inf")
    
#     while i < len(nums):
#         j = 0
#         while j < len(nums):
#             if nums[i] == -nums[j]:
#                 max_value =  max(max_value, max(nums[i], -nums[j]))
#             j += 1
#         i += 1

#     if max_value == float("-inf"):
#         return -1
#     return max_value

# nums = [-1,10,6,7,-7,1]
# obj = findPositive(nums)
# print(obj)


####################
# 2. Briliant Method.
####################

# def findPositive(nums):
#     maxu = -1
#     for num in nums:
#         if -num in nums and num > maxu:
#             maxu = num
#     return maxu
    
# nums = [-1,10,6,7,-7,1]
# obj = findPositive(nums)
# print(obj) 


#--------------->
# Relative Ranks.
#<---------------

# 1.

# score = [10,8,3,9,4]
# score.sort(reverse=True)

# i = 0
# j = len(score)-1

# gold = "Gold"
# silver = "Silver"
# bronze = "Bronze"
# store = []

# while i <= j:
#     if i == 0:
#         store.append(gold)
#     elif i == 1:
#        store.append(silver)
#     elif i == 2:
#         store.append(bronze)
#     store.append(i+1)
#     i+=1
#     print(store)
    
    
# while i < len(score):
#     i += 1


# 2.

# score = [10,8,3,9,4]

# top_scores = sorted(score, reverse=True)[:3]
# count = 4
# for i in range(len(score)):
#     if score[i] == top_scores[0]:
#         score[i] = "Gold"
#     elif score[i] == top_scores[1]:
#         score[i] = "Silver"
#     elif score[i] == top_scores[2]:
#         score[i] = "Bronze"
#     else:
#         score.append(str(count+1))
#         # count +=1
        
# print(score)

#------------------>
# 3. Working Method.
#<------------------

# score = [10,3,8,9,4]

# sorted_scores = sorted(score, reverse=True)

# gold = "Gold"
# silver = "silver"
# bronze = "Bronze"
# store = []

# for s in score:
#     if s == sorted_scores[0]:
#         store.append(gold)
#     elif s == sorted_scores[1]:
#         store.append(silver)
#     elif s == sorted_scores[2]:
#         store.append(bronze)
#     else:
#         store.append(str(sorted_scores.index(s)+1))

# print(store)


#----------------------->
# Reverse Prefix of Word.
#<-----------------------

# word = "abcdefd"; ch = "d"

# for i in word:
#     if ch in i:
#         s = word.index(ch)
#         words = word[:s+1][::-1] + word[s+1:]
# print(words)


# Testing another program.

# def maxmatrix(grid):
#     n = len(grid)

#     maxlocal = []
#     for i in range(n-2):
#         higest_row = []
#         for j in range(n-2):
#             maximum = max(grid[i][j], grid[i][j+1], grid[i][j+2],
#                           grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
#                           grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
            
#             higest_row.append(maximum)
#         maxlocal.append(higest_row)
#     return maxlocal
        
# grid = [[100]]

# op = maxmatrix(grid)

# print(op)


#--------------------->
# Trapping Rain Water.#
#<---------------------

# def containwater(height):

#     left = 0
#     right = len(height)-1
#     left_max,right_max = 0,0
#     water = 0
    
#     while left < right:
#         if height[left] < height[right]:
#             if height[left] >= left_max:
#                 left_max = height[left]
#             else:
#                 water += left_max - height[left]
#             left += 1
#         else:
#             if height[right] <= height[left]:
#                 if height[right] >= right_max:
#                     right_max = height[right]
#                 else:
#                     water += right_max - height[right]
#                 right -= 1
                
#     return water
# height = [4,2,0,3,2,5]
# op = containwater(height)
# print(op)


#------------------------------------------>
# Kids With the Greatest Number of Candies.#
#<------------------------------------------

# candies = [12,1,12]
# extra = 10

# max_candies = max(candies)
# final = []

# for i in range(0, len(candies)):
#     total = candies[i] + extra
#     if total >= max_candies:
#         final.append(True)
#     else:
#         final.append(False)
# print(final)


#------------->
# Single Number
#<-------------

# Working Condition

# nums = [2,2,1]
# total = 0
# for i in nums:
#     total ^= i
    
# print(total)


# 1. Another method with popping occurences

# def singleNumber(nums) :
#      for _ in range(len(nums)):
#         if len(nums)< 2:
#             return nums[0]
#         else:
#             popping = nums.pop()
#         try:
#             nums.remove(popping)
#         except:
#             return popping

# nums = [2,1,2]
# obj = singleNumber(nums)
# print(obj)


# 2. Another method with using `collections` module.

# from collections import Counter

# nums = [4,2,1,2,1,2]

# counter = Counter(nums)
# for i, j in counter.items():
#     if j > 1:
#         continue
#     else:
#         print(i)


########## Work in my code space not in leetcode. ##########

# nums = [2,2,1]

# for i in nums:
#     nums[i] ^= i
# print(i)


#------------------------------------------------------>
# Special Array With X Elements Greater Than or Equal X
#<------------------------------------------------------

# 1. First method

# nums = [0,4,3,0,4]
# nums.sort()
# n = len(nums)

# for i in range(n+1):
#     count = 0
#     for num in nums:
#         if num >= i:
#             count +=1
#     if count == i:
#         print(i)
# print(-1)


# 2. Second method

# nums = [0,4,3,0,4]
# nums.sort()
# n = len(nums)

# for i in range(n+1):
#     count = (1 for num in nums if num >= i)
    
#     if count == i:
#         print(i)
        
# print(-1)


# 3. Third method (with Binary search + Linear search)

# Binary search on possible values of n.
# Then use Linear search to count ele that are grerater than or equal to n.

# nums = [0,4,3,0,4]
# nums.sort()
# n = len(nums)

# l, h = 0, n

# count possible values of n.
# while l <= h:
#     m = (l+h) // 2

# count elements that are >= n.
#     count = 0
#     for num in nums:
#         if num >= m:
#             count += 1
            
#     if count == m:
#         print(m)
        
#     elif count > m:
#         l = m +1
#     else:
#         h = m-1
# print(-1)


# 4. Fourth method

# nums = [0,4,3,0,4]
# nums.sort(reverse=True)
# n = 0

# while n < len(nums) and nums[n] > n:
#     n+=1
    
# print(-1) if n < len(nums) and nums[n] == n else n


# s = "10"

# result = int(s, 2)
# print(result)
# count = 0

# while result != 1:
#     count += 1
#     if result % 2 == 0:
#         result //=2
#     else:
#         result+=1
# print(count)


#------------------>
# 1. Single Number 3
#<------------------

# from collections import Counter
# nums = [1,1,2,3,2,5]

# counts = Counter(nums)
# print(counts)
# unique = [num for num in counts if counts[num] == 1]
# print(unique)
# # for i in range(len(unique)):
# #     for j in range(i+1, len(unique)):
# #         if unique[i] ^ unique[j] != 0:
# #             print([unique[i], unique[j]])
    
# # print([])


# 2. Second method with using set.

# nums = [1,1,2,3,2,5]

# dupu = set()

# for i in nums:
#     if i in dupu:
#         # print(dupu)
#         dupu.remove(i)
#         # print(dupu)
#     else:
#         # print(dupu)
#         dupu.add(i)
#         # print(dupu)
        
# # print(list(dupu))


# 3. Third method with using list.

# nums = [1,1,2,3,2,5]

# store = []

# for i in nums:
#     if i in store:
#         # print(store)
#         store.remove(i)
#         # print(store)
#     else:
#         # print(dupu)
#         store.append(i)
#         # print(store)
        
# print(store)


#----------------->
# Number Complement
#<-----------------

# 1. First method

# num = 1

# binary_str = format(num, 'b')

# complement_bit = ''
# for i in binary_str:
#     if i == '0':
#         complement_bit+='1'
#     else:
#         complement_bit+='0'
        
# total_comp_sum = int(complement_bit, 2)

# print(total_comp_sum)


# 2. Second method

# num = 1

# binary_str = format(num, 'b')

# complement_bit = ''
# for i in binary_str: 
#   if i not in complement_bit or i in binary_str:
#     if i == '0':
#         complement_bit+='1'
#     else:
#         complement_bit+='0'
        
# total_comp_sum = int(complement_bit, 2)

# print(total_comp_sum)


# s = "hello"
# count = 0

# for i in range(1, len(s)):
#     count+= abs(ord(s[i-1]) -  ord(s[i]))
# print(count)


# 2. Second method with while loop.

# s = "hello"

# count = 0
# i = 0
# while i < len(s) -1: # 0 < 4. Condition is true.
#     count+= abs(ord(s[i]) -  ord(s[i+1])) # Add count value with get ASCII value like abs(ord(h) - ord(e))  h = '104 - e = 101 and move until the len.
#     i+=1 # Increase the pointer to move like e -> l, l -> l, l -> o.
# print(count) # return or print(for testing) the total count


# 3. Third method with using list.

# s = "hello"

# lists = []

# for i in range(len(s)):
#     lists.append(ord(s[i])) # ['104', '101', '108', '108', '111'].
    
# count = 0
# for i in range(len(s)-1): # end of the length which means at ['111'].
#     count += abs(lists[i] - lists[i+1])  # Then adding total count of substracting ASCII values each.
#                                             # Like |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111|
#                                             # = 3 + 7 + 0 + 3 = 13.
# print(count) # return final value of count.

# import math
# n = 49

# ans = math.sqrt(n)
# if ans.is_integer():
#     print(ans)
# else:
#     print(False)

# print(math.sqrt(27**2 + 39**2))
# print(27*2 + 39*2)
# # n = 27
# p = 39

# print(math.sqrt(n**2 + p**2))


# nums = [23, 2, 6, 4, 7]; k = 13

# p = 0
# j = 1

# for _ in range(p, j):
#     ans1 = nums[p] % k
#     ans = nums[p] + nums[j]
#     final = ans%k
#     j+=1
# print(ans1)
# print(final)
    
    
    
    
# print(25%13)


# seats = [3, 1, 5]; students = [2,7,4]

# seats.sort()
# students.sort()

# count = 0

# for i in range(len(students)):
#     count += abs(seats[i] - students[i])
# print(count)


"""
Example 1:

Input: event1 = ["01:15","02:00"]; event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.
Example 2:

Input: event1 = ["01:00","02:00"]; event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
Example 3:

Input: event1 = ["10:00","11:00"]; event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.
"""

# event1 = ["10:00","11:00"]; event2 = ["10:50","15:00"]


# maxu = max(event2)
# store = []

# h1, m1 = event1
# h2, m2 = event2
# print(h2 <= h1 <= m2 or h1 <= h2 <= m1)


#---->
# IPO
#<----

# import heapq
# k = 2; w = 0; profits = [1,2,3]; capital = [0,1,1]

# projects = list(zip(capital, profits)) # [(0,1), (1,2), (1,3)]

# projects.sort(key=lambda x: x[0])

# total_heap = []

# index = 0
# for _ in range(k):
#     while index < len(projects) and projects[index][0] <= w:
#         heapq.heappush(total_heap, -projects[index][1])
#         index +=1
        
#     if not total_heap:
#         break

#     w += -heapq.heappop(total_heap)
    
# print(w)


#---------------------->
# Grumpy Bookstore Owner
#<----------------------

# customers = [1,0,1,2,1,1,7,5]; grumpy = [0,1,0,1,0,1,0,1]; minutes = 3
# # customers = [4,10,10]; grumpy = [1,1,0]; minutes = 2

# n = len(customers)

# count = 0
# for i in range(n):
#     if grumpy[i] == 0:
#         count += customers[i]
#         # print(customers[i])
#         # print(count)
        
# aditional_satisfy = 0
# curr_window_satisfy = 0

# for i in range(minutes):
#     if grumpy[i] == 1:
#         curr_window_satisfy += customers[i] if grumpy[i] == 1 else 0
# aditional_satisfy = curr_window_satisfy
# # print(customers[i])

# for i in range(minutes, n):
#     if grumpy[i] == 1:
#         curr_window_satisfy += customers[i]
#     if grumpy[i-minutes] == 1:
#         curr_window_satisfy -= customers[i-minutes]
        
#     aditional_satisfy = max(aditional_satisfy, curr_window_satisfy)
# # print(aditional_satisfy)
# total = count + aditional_satisfy

# print(total)


#----------------------->
# Don't Know. Very Sorry.
#<-----------------------

# nums = [8,2,4,7]; limit = 4
# # nums = [10,1,2,4,7,2]; limit = 5
# # nums = [4,2,2,2,4,4,2,2]; limit = 0

# i=0

# max_len = 0
# for p in range(len(nums)):
#     while max(nums[i:p+1]) - min(nums[i:p+1]) > limit:
#         i+=1
#         # print(nums[p])
#     current = p - i +1
#     print(current)
#     max_len = max(max_len, current)
# # print(max_len)


#----------------------------------->
# Connect n ropes with minimum costs
#<-----------------------------------

# def heaps(rope) -> int:
#     import heapq
#     heapq.heapify(rope)
#     total = 0
#     while len(rope) >= 2:
#         first_rope, second_rope = heapq.heappop(rope), heapq.heappop(rope)
#         total += first_rope + second_rope
#         heapq.heappush(rope, first_rope + second_rope)
#     return total

# rope = [4,3,2,6]
# print(heaps(rope))


#-------------------------------------------------------------------->
# Minimum Difference Between Largest and Smallest Value in Three Moves
#<--------------------------------------------------------------------

# nums = [5,3,2,4]

# if len(nums) <= 4: print(0)

# nums.sort()
# infi = float("inf")

# infi = min(infi, abs(nums[0] - nums[-4]))
# infi = min(infi, abs(nums[1] - nums[-3]))
# infi = min(infi, abs(nums[2] - nums[-2]))
# infi = min(infi, abs(nums[3] - nums[-1]))
# print(infi)


# n = 1000000000
# counting = 0

# for i in range(n+1):
#     counting += str(i).count('1')
    
# print(counting)


# count = 0
# factor = 1

# while factor <= n:
#     lower_numbers = n - (n // factor) * factor
#     current_digit = (n // factor) % 10
#     higher_numbers = n // (factor * 10)
    
#     if current_digit == 0:
#         count += higher_numbers * factor
#     elif current_digit == 1:
#         count += higher_numbers * factor + lower_numbers + 1
#     else:
#         count += (higher_numbers + 1) * factor
    
#     factor *= 10

# print(count) 


# n = 4
# time = 5

# direction = time // n - 1
# print(direction)

# # if direction % 2 == 0: # 0 Condition is True
# print( 1 + time % (n - 1)) 
# # else:
# print( n - time % (n - 1))


#-------------------->
# Average Waiting Time
#<--------------------

""" # Example Walkthrough :

**Customer 1**:

• Arrival time: 1
• Preparation time: 2
The chef starts preparing the order immediately at time 1.
• Finish time: 1 + 2 = 3
• Waiting time: 3 - 1 = 2

**Customer 2**:

• Arrival time: 2
• Preparation time: 5
The chef is busy until time 3. The chef starts preparing the order at time 3.
• Finish time: 3 + 5 = 8
• Waiting time: 8 - 2 = 6

**Customer 3**:

• Arrival time: 4
• Preparation time: 3
The chef is busy until time 8. The chef starts preparing the order at time 8.
• Finish time: 8 + 3 = 11
• Waiting time: 11 - 4 = 7

**Average Waiting Time Calculation**:

• Total waiting time: 2 + 6 + 7 = 15
• Number of customers: 3
• Average waiting time: 15 / 3 = 5.00000"""

# customers = [[1, 2], [2, 5], [4, 3]]
# time = 0
# waiting = 0

# for arrival, prep in customers:
#     if time < arrival:
#         time = arrival
#     time += prep
#     waiting_time = time - arrival
#     waiting += waiting_time
    
# average = waiting / len(customers)
# print(average)


#------------------>
# Crawler Log Folder
#<------------------

# logs = ["d1/","d2/","../","d21/","./"]
# logs = ["d1/","d2/","./","d3/","../","d31/"]
# logs = ["d1/","../","../","../"]

# count = 0
# for i in logs:
#     if i == "../":
#         if count > 0:
#             count -=1
#     elif i == "./":
#         pass
#     else:
#         count += 1
# print(count)


# 2. Second method with using stack

# stack = []
# for i in logs:
#     if i == "../" and stack:
#         stack.pop()
#     elif i[0] != ".":
#         stack.append(i)
# print(len(stack))


# 3. Third method with using regex.

# import re
# count = 0
# parent_dir = re.compile(r'\.\./')
# same_dir = re.compile(r'\./')
# child_dir = re.compile(r'[^./]+/')

# for i in logs:
#     if parent_dir.match(i):
#         if count > 0:
#             count -=1 
#     elif same_dir.match(i):
#         continue
#     elif child_dir.match(i):
#         count += 1
# print(count)


#------------------------------------>
# Find the Winner of the Circular Game
#<------------------------------------

# n = 5; k = 2
# n = 6; k = 5

# friends = list(range(1, n + 1))
# index = 0

# while len(friends) > 1:
#     index = (index + k -1) % len(friends)
#     friends.pop(index)
# print(friends[0])


# Second Method

# index = 0

# for i in (range(1, n + 1)):
#     index = (index + k) % i
# print(index + 1)


#---------------------------------------------------------->
# Step-By-Step Directions From a Binary Tree Node to Another
#<----------------------------------------------------------

# Definition for a binary tree node.
# from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def getDirections(self, root: Optional[TreeNode], sv: int, dv: int) -> str:
#         def find_path(root: TreeNode, target: int, path: list) -> bool:
#             if not root:
#                 return False
#             if root.val == target:
#                 return True
            
#             path.append("L")
#             if find_path(root.left, target, path):
#                 return True
#             path.pop()

#             path.append("R")
#             if find_path(root.right, target, path):
#                 return True
#             path.pop()
#             return False
        
#         start_path = []
#         dest_path = []
#         find_path(root, sv, start_path)
#         find_path(root, dv, dest_path)
        
#         i = 0
#         # Way to LCA
#         while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
#             i += 1
        
#         start_LCA = "U" * (len(start_path) - i)
#         from_LCA_to_dest_path = "".join(dest_path[i:])
        
#         return start_LCA + from_LCA_to_dest_path
   
# # For Case: 1 
# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(4)

# solution = Solution()
# print(solution.getDirections(root, 3, 6))


# # For Case: 2 
# root = TreeNode(2)
# root.left = TreeNode(1)

# solution = Solution()
# print(solution.getDirections(root, 2, 1))


#------------------------------>
# Delete Nodes And Return Forest
#<------------------------------

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        store = []
        
        def dfs(node, to_root):
            if not node:
                return None
            
            deletes = node.val in to_delete
            
            if to_root and not deletes:
                store.append(node)
            
            node.left = dfs(node.left, deletes)
            node.right = dfs(node.right, deletes)
            
            return None if deletes else node
        
        dfs(root, True)
        return store
    
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
forest = solution.delNodes(root, [3, 5])
# Convert forest to list of lists for easier visualization
def convert_to_list(node):
    if not node:
        return None
    return [node.val, convert_to_list(node.left), convert_to_list(node.right)]

forest_list = [convert_to_list(tree) for tree in forest]
print(forest_list) 