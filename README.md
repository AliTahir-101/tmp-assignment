# Print All Unique Pairs With Equal Sum

This repository contains a Python function `print_all_unique_pairs_with_equal_sum` that, given an array of integers, prints all unique pairs that share the same sum when there are at least two distinct pairs for that sum.

## Task Description

**Problem Statement:**

Given an **unsorted array `arr` of unique integers**, the goal is to find and print all unique pairs that form the same sum. We only print sums where more than one unique pair produces that same sum. Each sum should be listed along with its pairs.

**Key points:**

1. **Input:** An unsorted list of integers.
2. **Output:** Lines indicating pairs of integers that share the same sum. Only sums that appear for multiple pairs should be printed.
3. **Pairs Format:** `( x, y)` with consistent spacing.
4. **Sorting Pairs Internally:** Each pair should be stored in sorted order (e.g., `(4, 12)` not `(12, 4)`). This ensures uniqueness and consistency.
5. **When and What to Print:**  
   - Print all pairs that produce the same sum if and only if there is more than one pair for that sum.
   - Print sums in ascending order.
   - If there's a maximum sum with multiple pairs, that line may print pairs in a bracketed list format as shown in the examples.

**Example:**

For input:
