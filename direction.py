def direction(facing, turn):
    directions = {"N":{45:"NE",-45:"NW"}, "NE":{45:"E",-45:"N"}, "E":{45:"SE",-45:"NE"},
                 "SE":{45:"S",-45:"E"}, "S":{45:"SW",-45:"SE"}, "SW":{45:"W",-45:"S"},
                 "W":{45:"NW",-45:"SW"}, "NW":{45:"N",-45:"W"}}
    if turn < -1080 or turn > 1080 or turn%45 != 0:
        raise ValueError("Turn value is out of [-1080;1080] range or not divided on 45")
    if facing not in ["N", "NE", "NW", "E", "SE", "SW", "W", "S"]:
        raise ValueError("Compass have only 8 directions allowed")
    if turn == 0:
        return facing
    while turn != 0:
        if turn < 0:
            to_turn = -45
        else:
            to_turn = 45
        curr_dir=directions[facing][to_turn]
        turn -=to_turn
        facing = curr_dir        
    return curr_dir
