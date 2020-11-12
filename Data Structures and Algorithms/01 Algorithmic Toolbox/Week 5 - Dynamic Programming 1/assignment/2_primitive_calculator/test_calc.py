from primitive_calculator import optimal_sequence_greedy, optimal_sequence_dp


for n in [1, 5, 96234]:
    grd_seq = optimal_sequence_greedy(n)
    print(f"n: {n}, greedy length: {len(grd_seq)}, greedy sequence: {grd_seq}")

    dp_seq = optimal_sequence_dp(n)
    print(f"n: {n}, dp     length: { len(dp_seq)}, dp     sequence: {dp_seq}")
    print("-" * 30)
