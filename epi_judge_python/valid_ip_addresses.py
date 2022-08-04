from typing import List

from test_framework import generic_test


# time: O(1), number of valid IP addresses is constant (2^32)
# space: O(1)
def get_valid_ip_address(s: str) -> List[str]:
    def is_valid_part(part: str) -> bool:
        return len(part) == 1 or (part[0] != "0" and int(part) <= 255)

    valid = []
    parts = [""] * 4
    for a in range(1, min(4, len(s))):
        parts[0] = s[:a]
        if is_valid_part(parts[0]):
            for b in range(a + 1, min(a + 4, len(s))):
                parts[1] = s[a:b]
                if is_valid_part(parts[1]):
                    for c in range(b + 1, min(b + 4, len(s))):
                        parts[2] = s[b:c]
                        parts[3] = s[c:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            valid.append(".".join(parts))
    return valid


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            "valid_ip_addresses.tsv",
            get_valid_ip_address,
            comparator=comp,
        )
    )
