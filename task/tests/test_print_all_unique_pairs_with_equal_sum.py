import pytest

from task.problem import print_all_unique_pairs_with_equal_sum


class TestPrintAllUniquePairsWithEqualSum:

    @pytest.mark.parametrize("arr, expected_substrings", [
        (
            [6, 4, 12, 10, 22, 54, 32, 42, 21, 11],
            [
                "Pairs : ( 4, 12) ( 6, 10) have sum : 16",
                "Pairs : ( 10, 22) ( 11, 21) have sum : 32",
                "Pairs : ( 12, 21) ( 11, 22) have sum : 33",
                "Pairs : ( 11, 32) ( 21, 22) have sum : 43",
                "Pairs : ( 21, 32) ( 11, 42) have sum : 53",
                "Pairs : ( 22, 32) ( 12, 42) have sum : 54",
                "Pairs : [( 10, 54),( 22, 42)] have sum : 64"
            ]
        ),
        (
            [4, 23, 65, 67, 24, 12, 86],
            [
                "Pairs : ( 23, 67) ( 4, 86) have sum : 90"
            ]
        )
    ])
    def test_multiple_scenarios(self, capfd, arr, expected_substrings):
        # Tests multiple known scenarios.
        print_all_unique_pairs_with_equal_sum(arr)
        captured = capfd.readouterr()
        output = captured.out.strip()
        for substring in expected_substrings:
            assert substring in output

    @pytest.mark.parametrize("arr, expected_output", [
        ([10, 20, 30], ""),  # No repeated sums, so no output expected
        ([5], ""),           # Single element, no pairs, no output
    ])
    def test_no_output_cases(self, capfd, arr, expected_output):
        print_all_unique_pairs_with_equal_sum(arr)
        captured = capfd.readouterr()
        output = captured.out.strip()
        assert output == expected_output

    @pytest.mark.parametrize("arr, sums_and_substrings", [
        (
            [2, 4, 6, 8, 10],
            [
                "Pairs : ( 4, 6) ( 2, 8) have sum : 10",
                "Pairs : ( 2, 10) ( 4, 8) have sum : 12",
                "Pairs : [( 4, 10),( 6, 8)] have sum : 14"
            ]
        )
    ])
    def test_repeated_sums_scenario(self, capfd, arr, sums_and_substrings):
        # Tests a scenario with multiple repeated sums.
        print_all_unique_pairs_with_equal_sum(arr)
        captured = capfd.readouterr()
        output = captured.out.strip()
        for substring in sums_and_substrings:
            assert substring in output
