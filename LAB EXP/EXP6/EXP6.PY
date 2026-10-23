
def vacuum_cleaner():
    room = {'A': 1, 'B': 1}
    position = 'A'

    while 1 in room.values():
        if room[position] == 1:
            print("Room", position, "is Dirty. Cleaning...")
            room[position] = 0
        else:
            print("Room", position, "is Clean.")

        position = 'B' if position == 'A' else 'A'

    print("All rooms are clean!")

vacuum_cleaner()
