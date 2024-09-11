def queens_beat(coordinates: list) -> bool:
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            if coordinates[i][0] == coordinates[j][0] or coordinates[i][1] == coordinates[j][1]:
                return True
            elif coordinates[i][0] - coordinates[j][0] == coordinates[i][1] - coordinates[j][1]:
                return True
    return False


if __name__ == '__main__':
    coordinates1 = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)]
    coordinates2 = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 1), (6, 3), (7, 7), (8, 5)]
    print(queens_beat(coordinates1))
    print(queens_beat(coordinates2))

__all__ = ['queens_beat']
