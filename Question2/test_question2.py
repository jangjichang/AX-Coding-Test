def find_open_door(N, n):
    door = [0 for _ in range(N+1)]
    for person in range(1, n+1):
        multiple_index = 1
        while person * multiple_index <= N:
            number = person * multiple_index
            multiple_index += 1
            if door[number] == 0:
                door[number] = 1
            else:
                door[number] = 0
    return sum(door)

"""
1o
2x
3x
4o
5x
6o
7o
8o
9x
10o
"""

def test_find_open_door():
    assert find_open_door(50, 1) == 50
    assert find_open_door(10, 3) == 4
    assert find_open_door(10, 4) == 6
    assert find_open_door(10, 5) == 6

