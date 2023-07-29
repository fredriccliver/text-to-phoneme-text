import difflib


# def levenshtein(seq1, seq2):
#     size_x = len(seq1) + 1
#     size_y = len(seq2) + 1
#     matrix = [[0 for _ in range(size_y)] for _ in range(size_x)]
#     for x in range(size_x):
#         matrix [x][0] = x
#     for y in range(size_y):
#         matrix [0][y] = y

#     for x in range(1, size_x):
#         for y in range(1, size_y):
#             if seq1[x-1] == seq2[y-1]:
#                 matrix [x][y] = min(
#                     matrix[x-1][y] + 1,
#                     matrix[x-1][y-1],
#                     matrix[x][y-1] + 1
#                 )
#             else:
#                 matrix [x][y] = min(
#                     matrix[x-1][y] + 1,
#                     matrix[x-1][y-1] + 1,
#                     matrix[x][y-1] + 1
#                 )
#     return matrix[size_x - 1][size_y - 1]


seq1 = "ɔl idealization* meɪks laɪf ˈpurər."
seq2 = "ɔ l d ə l ɪ z eɪ ʃ ə n m eɪ k s l aɪ f p ʊ ɹ"


def clean_sequence(seq):
    return ''.join(char for char in seq if char.isalpha())
# Remove non-alphabet characters
seq1 = clean_sequence(seq1)
seq2 = clean_sequence(seq2)


# print (seq1)
# print (seq2)
# print(levenshtein(seq1, seq2))


def visualize_difference(seq1, seq2):
    matcher = difflib.SequenceMatcher(None, seq1, seq2)
    print (matcher.get_opcodes())
    result = []
    for opcode in matcher.get_opcodes():
        tag, i1, i2, j1, j2 = opcode
        if tag == 'equal':
            result.append(seq1[i1:i2])
        elif tag == 'delete':
            result.append(f"Delete '{seq1[i1:i2]}' from seq1")
        elif tag == 'insert':
            result.append(f"Insert '{seq2[j1:j2]}' into seq1")
        elif tag == 'replace':
            result.append(f"Replace '{seq1[i1:i2]}' in seq1 with '{seq2[j1:j2]}'")
    return result

difference = visualize_difference(seq1, seq2)

# for action in difference:
#     print(action)