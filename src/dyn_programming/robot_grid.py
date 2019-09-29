class pos:
    def __init__(self, r, c, is_blocked):
        self.r = r
        self.c = c
        self.is_blocked = is_blocked

def robot_find_path(matrix, cur_pos, end):
    ''' Start at 0,0'''
    memo_path = dict
    memo_path[ (0,0) ] = (0,0)
    if (cur_pos == end):
        return pos
    if cur_pos.is_blocked:
        memo_path[cur_pos] = -1

    while len(stack) > 0:
        cur_pos = stack.pop(len(stack))

        # recursive relation:
        cur_pos = [ cur_pos, path]
