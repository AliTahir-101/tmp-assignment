def print_all_unique_pairs_with_equal_sum(arr: list) -> None:
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