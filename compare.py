import sys
import numpy as np
import ast


def m(ch1, ch2):
    return 0 if ch1 == ch2 else 1


def lev(str1, str2):
    N1 = len(str1)
    N2 = len(str2)
    D = np.zeros((N2 + 1, N1 + 1))

    for j in range(1, N1 + 1):
        D[0][j] = j
    for i in range(1, N2 + 1):
        D[i][0] = i

    for i in range(1, N2 + 1):
        for j in range(1, N1 + 1):
            D[i][j] = min(
                D[i - 1][j - 1] + m(str1[j - 1], str2[i - 1]),
                D[i - 1][j] + 1,
                D[i][j - 1] + 1
            )

            # print(f"S1 = {str1[j-1]}; S2 = {str2[i-1]}; m(S1, S2) = {m(str1[j-1], str2[i-1])}")

    return D[-1][-1]


def scoring_plagiat(filename_origin, filename_plagiat):
    with open(filename_plagiat, 'r', encoding='utf-8') as f_plagiat:
        with open(filename_origin, 'r', encoding='utf-8') as f_origin:
            source_text_origin = f_origin.read()
            source_text_plagiat = f_plagiat.read()

            tree_origin = ast.parse(source_text_origin)
            tree_plagiat = ast.parse(source_text_plagiat)

            unparsed_tree_origin = ast.unparse(tree_origin)
            unparsed_tree_plagiat = ast.unparse(tree_plagiat)

            res = lev(unparsed_tree_origin, unparsed_tree_plagiat)

    return "{acc:.2f}".format(acc=res / max(len(unparsed_tree_origin), len(unparsed_tree_plagiat)))


def main():
    input_f = sys.argv[1]
    output_f = sys.argv[2]

    files_for_scoring = []
    res = []

    with open(input_f, 'r') as file_input:
        files_for_scoring = file_input.readlines()
        for line in files_for_scoring:
            filename_origin, filename_plagiat = line.split(" ")

            filename_plagiat = filename_plagiat.rstrip()
            res.append(scoring_plagiat(filename_origin, filename_plagiat))

    with open(output_f, 'w') as file_output:
        for val in res:
            file_output.write(f"{str(val)}\n")


if __name__ == "__main__":
    main()
