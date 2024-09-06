class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = j = 0
  
        for s in commands:
            if s == "UP":
                i -= 1
            elif s == "DOWN":
                i += 1
            elif s == "LEFT":
                j -= 1
            else:
                j += 1
        return i * n + j