"""
Given a string, find the longest palindromic substring.
Examples:
"babad" -> "bab" or "aba"
"cbbd" -> "bb"
Problem provided by: https://leetcode.com/problems/longest-palindromic-substring/
"""

def longest_palindromic_substring(string):
  start = 0
  end = 0
  for i in range(len(string)):
    left, right = helper(string, i, i)
    if right - left > end - start:
      start = left
      end = right
    left, right = helper(string, i, i + 1)
    if right - left > end - start:
      start = left
      end = right
  return string[start:end + 1]

def helper(string, left, right):
  while left >= 0 and right < len(string) and string[left] == string[right]:
    left -= 1
    right += 1
  return (left + 1, right - 1)


print(longest_palindromic_substring('abcddsaaaaaa'))