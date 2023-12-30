import heapq

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_vehicles(passengers, vehicles):
    assigned_vehicles = {}
    total_distance = 0

    idle_vehicles = [(vid, pos) for vid, pos in vehicles.items()]
    heapq.heapify(idle_vehicles)

    for passenger in sorted(passengers):
        passenger_name, passenger_pos = passenger
        nearest_vehicle = None
        min_distance = float('inf')

        for vid, vehicle_pos in idle_vehicles:
            distance = manhattan_distance(passenger_pos, vehicle_pos)
            if distance < min_distance or (distance == min_distance and vid < nearest_vehicle):
                nearest_vehicle = vid
                min_distance = distance


        total_distance += min_distance
        assigned_vehicles[passenger_name] = nearest_vehicle


        idle_vehicles.remove((nearest_vehicle, vehicles[nearest_vehicle]))

    return total_distance

if __name__ == "__main__":
    N, M = map(int, input().split())
    passengers = [input().split() for _ in range(N)]
    vehicles = {input().split()[0]: tuple(map(int, input().split())) for _ in range(M)}

    result = assign_vehicles(passengers, vehicles)
    print(result)