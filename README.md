# DSA Practice in Python

This repository contains daily Data Structures and Algorithms practice problems solved in Python.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

To run tests for a specific problem:
```bash
python -m pytest problems/day1_two_sum/test_solution.py -v
```

## Problem List

### Day 1: Two Sum
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
``` 