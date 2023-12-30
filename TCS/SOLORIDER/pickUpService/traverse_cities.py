from collections import defaultdict

def traverse_cities(city_graph, current_city, visited):
    visited[current_city] = True
    route_map = [current_city]

    for neighbor, goods, tax in city_graph[current_city]:
        if not visited[neighbor]:
            route, total_tax = traverse_cities(city_graph, neighbor, visited)
            route_map.extend(route)
            route_map.append(current_city)
            total_tax += tax * goods
            return route_map, total_tax
    return route_map, 0

def james_journey(N, city_info):
    city_graph = defaultdict(list)

    for _ in range(N-1):
        city1, city2, goods, tax = city_info[_]
        city_graph[city1].append((city2, goods, tax))
        city_graph[city2].append((city1, goods, tax))

    visited = {city: False for city in city_graph}
    route_map, total_tax = traverse_cities(city_graph, list(city_graph.keys())[0], visited)
    return '-'.join(route_map[::-1]), total_tax

if __name__ == "__main__":
    N = int(input())
    city_info = [input().split() for _ in range(N-1)]
    result_route, result_tax = james_journey(N, city_info)
print(result_route)
print(result_tax)

