def print_all_unique_pairs_with_equal_sum(arr: list) -> None:
    """
    Finds and prints all unique pairs in the input array that share the same sum.

    This function processes an unsorted list of integers to identify unique pairs of numbers 
    whose sums are equal. Only sums with at least two distinct pairs are printed. The output
    is formatted in ascending order of sums, and pairs are printed in ascending order within 
    each sum.

    Args:
        arr (list): A list of integers to be processed.

    Returns:
        None: The function prints the results directly to the standard output.

    Output Format:
        - If multiple pairs share the same sum, all such pairs are printed in the format:
          "Pairs : (x1, y1) (x2, y2) ... have sum : S"
        - Sums are printed in ascending order.
        - If the maximum sum has multiple pairs, they are displayed in a list-like format:
          "Pairs : [(x1, y1),(x2, y2)] have sum : S"

    Example:
        Input:
            arr = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
        Output:
            Pairs : ( 4, 12) ( 6, 10) have sum : 16
            Pairs : ( 10, 22) ( 21, 11) have sum : 32
            Pairs : ( 12, 21) ( 22, 11) have sum : 33
            Pairs : ( 22, 21) ( 32, 11) have sum : 43
            Pairs : ( 32, 21) ( 42, 11) have sum : 53
            Pairs : ( 12, 42) ( 22, 32) have sum : 54
            Pairs : [( 10, 54),( 22, 42)] have sum : 64

    Notes:
        - If the input list has no repeated sums with multiple pairs, the function prints nothing.
        - Pairs are always printed in ascending order of their elements (e.g., (x, y) where x < y).

    Limitations:
        - The function assumes the input list consists of unique integers. Duplicate elements 
          may cause undefined behavior or inaccurate outputs.

    """

    output = {}
    max_sum = 0
    min_sum = max(arr)*2
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i]+arr[j] in output:
                if len(output[arr[i]+arr[j]]) > 0:
                    if max_sum < arr[i]+arr[j]:
                        max_sum = arr[i]+arr[j]
                    if min_sum > arr[i]+arr[j]:
                        min_sum = arr[i]+arr[j]
                if (arr[i], arr[j]) not in output[arr[i]+arr[j]]:
                    output[arr[i]+arr[j]].add(tuple((arr[j], arr[i]) if arr[i] > arr[j] else (arr[i], arr[j])))
            else:
                output[arr[i]+arr[j]] = {(arr[j], arr[i]) if arr[i] > arr[j] else (arr[i], arr[j])}


    for key in sorted(output):
        if len(output[key]) > 1:
            if key == min_sum:
                print("\nOutput:\n")
            if max_sum == key and max_sum != min_sum:
                formatted_pairs = ",".join(f"( {p[0]}, {p[1]})" for p in output[key])
                formatted_pairs = f"[{formatted_pairs}]"
            else:
                formatted_pairs = " ".join(f"( {p[0]}, {p[1]})" for p in output[key])
            print("Pairs :", formatted_pairs if max_sum == key and max_sum != min_sum else formatted_pairs, "have sum :", key, "\n")


if __name__ == "__main__":
    arr = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    # arr = [4, 23, 65, 67, 24, 12, 86]
    # arr = [10, 20, 30]
    # arr = [2, 4, 6, 8, 10]
    print_all_unique_pairs_with_equal_sum(arr)