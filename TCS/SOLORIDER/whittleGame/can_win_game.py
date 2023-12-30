def can_win_game(nails, m):
    nails.sort(key=lambda nail: (nail[1], nail[0]))
    picked_nails = []

    for _ in range(m):
        if not nails:
            break

        picked_nail = nails.pop(0)
        picked_nails.append(picked_nail)

        # Remove nails with the same area
        nails = [nail for nail in nails if picked_nail[0] * nail[1] != picked_nail[1] * nail[0]]

    return picked_nails, "YES" if not nails else "NO"

if __name__ == "__main__":
    N = int(input())
    nails = [tuple(map(int, input().split())) for _ in range(N)]
    m = int(input())

    picked_nails, result = can_win_game(nails, m)

    for nail in picked_nails:
        print(f"{nail[0]} {nail[1]}")

    print(result)
