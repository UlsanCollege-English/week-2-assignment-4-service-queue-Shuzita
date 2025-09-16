from typing import List, Tuple, Optional

def take_next(queue: List[str]) -> Tuple[Optional[str], List[str]]:
    if not queue:
        return (None, [])
    return (queue[0], queue[1:])

def move_to_back(queue: List[str], name: str) -> List[str]:
    if name not in queue:
        return queue[:]
    index = queue.index(name)
    return queue[:index] + queue[index+1:] + [queue[index]]

def interleave(q1: List[str], q2: List[str]) -> List[str]:
    result = []
    length = max(len(q1), len(q2))
    for i in range(length):
        if i < len(q1):
            result.append(q1[i])
        if i < len(q2):
            result.append(q2[i])
    return result
