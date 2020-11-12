from points_and_segments import naive_count_segments, fast_count_segments

starts = [0, 7]
ends = [5, 10]
points = [1, 6, 11]

print(naive_count_segments(starts, ends, points))