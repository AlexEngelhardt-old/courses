# Uses python3
import sys

# I think we can sort by segment end, and then successively visit those timepoints:
# The earliest segment end (which automatically contains the most number of other available
# neighbors for this earliest person)


def optimal_points(segments):
    # Determine the x axis min and max:
    time_start = segments[0]['start']
    time_end = segments[0]['end']
    for s in segments:
        if s['start'] < time_start:
            time_start = s['start']
        if s['end'] > time_end:
            time_end = s['end']

    points = []
    # This is O(n) in the x-axis length and O(n^2) in the number of segments:
    # for x_i in range(time_start, time_end+1):
    # But we can just check all segment ends instead of all x_i:
    segment_ends = sorted(list(set([s['end'] for s in segments])))
    for x_i in segment_ends:
        for s in segments:
            if s['visited'] is False and s['end'] == x_i:
                # We'll visit this guy now
                points.append(s['end'])
                s['visited'] = True
                # Now visit all other dudes that are home:
                for s2 in segments:
                    if s2['visited'] is False and s2['start'] <= x_i <= s2['end']:
                        s2['visited'] = True
                break

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: {'start': x[0], 'end': x[1], 'visited': False}, zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
