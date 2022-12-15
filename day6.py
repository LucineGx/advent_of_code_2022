signal = open("day6_input.txt").read()


def find_marker(length: int) -> int:
    for i in range(length, len(signal)):
        segment = signal[i-length:i]
        marker = True
        for c in segment:
            if segment.count(c) > 1:
                marker = False
                break
        if marker:
            return i


print(find_marker(4))
print(find_marker(14))
