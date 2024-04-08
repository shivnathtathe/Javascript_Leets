class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 0 --- n-1
        # 0 = open others are locked
    # visit all the rooms using the key
    # each  node as a array of keys and each key has it no. on it no on key == room no. unlock
        num_rooms_to_visit = len(rooms)
        visited_rooms = set()

        # Start with the first room (room 0)
        stack = [0]

        while stack:
            current_room = stack.pop()
            visited_rooms.add(current_room)
            keys_in_current_room = rooms[current_room]

            for key in keys_in_current_room:
                if key not in visited_rooms:
                    stack.append(key)

        return len(visited_rooms) == num_rooms_to_visit
        