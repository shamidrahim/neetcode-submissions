class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enter, exit = deque(), deque()
        ans = [0]* len(arrival)
        prev_state = 1
        cur_time = 0
        i = 0
        while i < len(arrival) or enter or exit:
            while i < len(arrival) and arrival[i] <= cur_time:
                if state[i] == 0:
                    enter.append(i)
                else:
                    exit.append(i)
                i += 1

            if not (enter or exit) and prev_state == 1:
                cur_time = arrival[i]
                continue
            if prev_state == 1:
                if exit:
                    ans[exit.popleft()] = cur_time
                elif enter:
                    ans[enter.popleft()] = cur_time
                    prev_state = 0
            else:
                if enter:
                    ans[enter.popleft()] = cur_time
                elif exit:
                    ans[exit.popleft()] = cur_time
                    prev_state = 1
                else:
                    prev_state = 1
            
            cur_time += 1
        return ans
        