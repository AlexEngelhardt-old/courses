from edit_distance import edit_distance


word_pairs = [('ab', 'ab'), ('short', 'ports'), ('editing', 'distance')]

for w1, w2 in word_pairs:
    print(f"ED({w1}, {w2}) = {edit_distance(w1, w2)}")