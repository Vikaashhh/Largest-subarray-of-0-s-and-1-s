# 📅 Day 63 – GFG 160 Days DSA Challenge
### 🔢 Problem: Largest Subarray with Equal Number of 0’s and 1’s
### 🧠 Difficulty: Medium
### 📌 Tags: #Day63 #gfg160 #geekstreak2025
### ✅ Status: Solved on First Attempt

## 📘 Problem Statement:
You're given a binary array (comprising only 0s and 1s). The task is to determine the length of the largest subarray where the number of 0s and 1s are equal.

## 💡 Approach:
- We transform the array using a simple trick:

- Replace each 0 with -1.

- Now, finding the largest subarray with equal 0s and 1s becomes equivalent to finding the largest subarray with sum = 0 — a classic prefix sum problem.

## ⚙️ Efficient Strategy:
- Maintain a prefix sum.

- Use a hash map (prefix_map) to store the first index where each cumulative sum occurs.

- If the same cumulative sum appears again, it means the elements in between sum up to zero — indicating equal 0s and 1s.

- Keep updating the maximum length encountered.

## 📊 Performance Metrics:
- ✅ Test Cases Passed: 1111 / 1111

- 🎯 Accuracy: 100%

- ⚡ Execution Time: 0.94 sec

- 🧠 Attempts: 1 / 1

- 🏆 Points: 2 / 2


## 🧠 Complexity:
- Time Complexity: O(n)

- Space Complexity: O(n)

## 💬 Reflection:
This problem reinforces how a simple transformation (0 ➝ -1) can unlock optimized solutions to seemingly complex subarray problems. Logical problem reduction is a critical skill in both algorithm design and frontend optimization patterns.


## 📢 Hashtags:
#Day63 #gfg160 #geekstreak2025
#prefixsum #subarray #hashmap #python
#dsaeveryday #problemsolving #frontendmindset
#framesbyvikash #100daysofcode #codechronicles
