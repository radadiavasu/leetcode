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