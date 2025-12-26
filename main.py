import heapq

cables = [4, 6, 2, 2, 1, 1]


def find_optimal_sequence(cables):
    if not cables:
        return [], 0

    heapq.heapify(cables)
    combined_cable = 0
    sequence = []

    while len(cables) > 1:
        second_cable = heapq.heappop(cables)
        combined_cable += second_cable
        sequence.append(second_cable)

    return sequence, combined_cable


if __name__ == "__main__":
    sequence, total_length = find_optimal_sequence(cables)
    print("Optimal sequence of cable lengths:", sequence)
    print("Total combined cable length:", total_length)
