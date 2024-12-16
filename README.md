
# Print All Unique Pairs With Equal Sum

## Problem Description

Given an unsorted array `A[]`, the task is to print all unique pairs of numbers from the array that share the same sum, but only print these pairs for sums that occur with more than one unique pair.

**Key Points:**

- Only display lines for sums that have at least two distinct pairs.
- Each pair should be in ascending order (e.g., `( 4, 12)`, not `( 12, 4)`).
- The sums should be listed in ascending order.
- Follow the output format shown in the examples.

**Example:**

**Input:**
```
A[] = { 6, 4, 12, 10, 22, 54, 32, 42, 21, 11}
```

**Expected Output:**
```
Pairs : ( 4, 12) ( 6, 10) have sum : 16
Pairs : ( 10, 22) ( 21, 11) have sum : 32
Pairs : ( 12, 21) ( 22, 11) have sum : 33
Pairs : ( 22, 21) ( 32, 11) have sum : 43
Pairs : ( 32, 21) ( 42, 11) have sum : 53
Pairs : ( 12, 42) ( 22, 32) have sum : 54
Pairs : [( 10, 54),( 22, 42)] have sum : 64
```

**Another Example:**

**Input:**
```
A[] = { 4, 23, 65, 67, 24, 12, 86}
```

**Expected Output:**
```
Pairs : ( 4, 86) ( 23, 67) have sum : 90
```

## Usage

1. Import the `print_all_unique_pairs_with_equal_sum` function in your Python environment.
2. Call the function with your array:
   ```python
   arr = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
   print_all_unique_pairs_with_equal_sum(arr)
   ```
   This will print the results to standard output in the specified format.

## Running Tests

This repository includes `pytest` test cases to ensure that the function works correctly for various scenarios:

- Correct results for the given examples.
- Handling arrays that yield no repeated sums (no output).
- Testing arrays with multiple pairs sharing the same sums.
- Parametrized tests to cover multiple input scenarios in a single test function.

**To run the tests:**
```bash
pytest -v
```

**Sample Test Results:**
```
C:\Users\ali\workspace\interview\tmp-assignment>pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.11.7, pytest-8.3.4, pluggy-1.5.0 -- C:\Users\ali\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\ali\workspace\interview\tmp-assignment
collected 5 items

task/tests/test_print_all_unique_pairs_with_equal_sum.py::TestPrintAllUniquePairsWithEqualSum::test_multiple_scenarios[arr0-expected_substrings0] PASSED [ 20%]
task/tests/test_print_all_unique_pairs_with_equal_sum.py::TestPrintAllUniquePairsWithEqualSum::test_multiple_scenarios[arr1-expected_substrings1] PASSED [ 40%]
task/tests/test_print_all_unique_pairs_with_equal_sum.py::TestPrintAllUniquePairsWithEqualSum::test_no_output_cases[arr0-] PASSED [ 60%]
task/tests/test_print_all_unique_pairs_with_equal_sum.py::TestPrintAllUniquePairsWithEqualSum::test_no_output_cases[arr1-] PASSED [ 80%]
task/tests/test_print_all_unique_pairs_with_equal_sum.py::TestPrintAllUniquePairsWithEqualSum::test_repeated_sums_scenario[arr0-sums_and_substrings0] PASSED [100%]

================================================== 5 passed in 0.05s ==================================================
```

All tests pass, confirming that the function adheres to the problem specifications.
