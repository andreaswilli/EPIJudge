from test_framework import generic_test

# time: O(n)
# space: O(n)
# def is_palindrome(s: str) -> bool:
#     alpha_num = []
#     for c in s:
#         if c.isalnum():
#             alpha_num.append(c)
#     for i in range(len(alpha_num) // 2):
#         if alpha_num[i].lower() != alpha_num[~i].lower():
#             return False
#     return True


# time: O(n)
# space: O(1)
def is_palindrome(s: str) -> bool:
    low = 0
    high = len(s) - 1
    while low < high:
        while not s[low].isalnum() and low < high:
            low += 1
        while not s[high].isalnum() and low < high:
            high -= 1
        if s[low].lower() != s[high].lower():
            return False
        low += 1
        high -= 1
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic_punctuation.py",
            "is_string_palindromic_punctuation.tsv",
            is_palindrome,
        )
    )
