class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(p,s) for p,s in zip(position,speed)]
        position_speed.sort(reverse=True)
        stack=[]
        print(position_speed)
        for p,s in position_speed:
            time = (target-p)/s
            stack.append(time)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)