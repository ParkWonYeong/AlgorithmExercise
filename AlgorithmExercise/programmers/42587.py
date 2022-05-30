## 42587

from collections import deque

def solution(priorities, location):
    
    answer = 0
    # (순서, 중요도)
    task = deque(enumerate(priorities))
    
    # checking
    # for task_prio in task:
    #         print(task_prio[0], task_prio[1])
    
    # 모든 인쇄 작업 진행 혹은
    while task:
        order, J = task.popleft()
        
        # J보다 중요도 높은 문서 존재 시
        if any(J < task_prio[1] for task_prio in task):
            task.append((order, J))
        else:
            answer += 1
            # 인쇄한 작업 순서가 location과 같을때
            if order == location:
                break

    return answer