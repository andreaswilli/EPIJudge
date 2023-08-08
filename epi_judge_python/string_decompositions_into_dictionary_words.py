from typing import Counter, List

from test_framework import generic_test


# time: O(n^2)
# space: O(n)
# def find_all_substrings(s: str, words: List[str]) -> List[int]:
#     result = []
#     word_size = len(words[0])
#
#     for i in range(len(s)):
#         word_count = Counter(words)
#         for j in range(i, len(s), word_size):
#             word = s[j:j+word_size]
#             if word in word_count:
#                 word_count[word] -= 1
#                 if word_count[word] == 0:
#                     del word_count[word]
#             else:
#                 break
#         if not word_count:
#             result.append(i)
#
#     return result

# def find_all_substrings(s: str, words: List[str]) -> List[int]:
#     result = []
#     word_size = len(words[0])
#
#     for offset in range(word_size):
#         word_count = Counter(words)
#         start = end = offset
#         while start <= end < len(s):
#             word = s[end:end+word_size]
#             if word in word_count:
#                 word_count[word] -= 1
#                 if word_count[word] == 0:
#                     del word_count[word]
#                 if not word_count:
#                     result.append(start)
#                     word_count.update([s[start:start+word_size]])
#                     start += word_size
#                 end += word_size
#             else:
#                 if start == end:
#                     start += word_size
#                     end += word_size
#                     word_count = Counter(words)
#                 else:
#                     word_count.update([s[start:start+word_size]])
#                     start += word_size
#
#     return sorted(result)


# time: O(Nnm), where N is the length of s, n is the length of each word and
#               m is the number of words
# space: O(n)
def find_all_substrings(s: str, words: List[str]) -> List[int]:
    def match_all_words_in_dict(start):
        curr_string_to_freq = Counter()
        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i:i+unit_size]
            it = word_to_freq[curr_word]
            if it == 0:
                return False
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                return False
        return True

    word_to_freq = Counter(words)
    unit_size = len(words[0])
    return [
        i for i in range(len(s) - unit_size * len(words) + 1)
        if match_all_words_in_dict(i)
    ]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
