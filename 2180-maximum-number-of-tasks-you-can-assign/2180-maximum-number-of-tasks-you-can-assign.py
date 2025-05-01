from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(k):
            task_ptr = k - 1
            available_workers = SortedList(workers[-k:])
            pills_left = pills

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                if available_workers and available_workers[-1] >= task:
                    available_workers.pop(-1)
                elif pills_left > 0:
                    idx = available_workers.bisect_left(task - strength)
                    if idx == len(available_workers):
                        return False
                    available_workers.pop(idx)
                    pills_left -= 1
                else:
                    return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
