def min_vehicles_needed(weights, max_limit):
    weights.sort(reverse=True)
    vehicles_needed = 0
    current_load = 0

    for weight in weights:
        if current_load + weight <= max_limit:
            current_load += weight
        else:
            vehicles_needed += 1
            current_load = weight

    if current_load > 0:
        vehicles_needed += 1

    return vehicles_needed

if __name__ == "__main__":
    weights = list(map(int, input().split()))
    max_limit = int(input())

    result = min_vehicles_needed(weights, max_limit)
    print(result)
