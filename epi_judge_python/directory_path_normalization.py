from test_framework import generic_test


# time: O(n)
def shortest_equivalent_path(path: str) -> str:
    pack_names = []
    for i, token in enumerate(path.split("/")):
        if (i == 0 and token == "") or token not in ["", "."]:
            if token == ".." and pack_names:
                if pack_names[-1] == "..":
                    pack_names.append(token)
                else:
                    pack_names.pop()
            else:
                pack_names.append(token)
    return "/".join(pack_names) or "/"


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "directory_path_normalization.py",
            "directory_path_normalization.tsv",
            shortest_equivalent_path,
        )
    )
