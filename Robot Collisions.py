class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        # Step 1: Combine data
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        
        # Step 2: Sort by position
        robots.sort()
        
        stack = []
        
        # Step 3: Process collisions
        for robot in robots:
            pos, health, direction, idx = robot
            
            if direction == 'R':
                stack.append(robot)
            else:
                # moving left
                while stack and stack[-1][2] == 'R':
                    top = stack[-1]
                    
                    if top[1] > health:
                        top[1] -= 1
                        health = 0
                        break
                    elif top[1] < health:
                        health -= 1
                        stack.pop()
                    else:
                        stack.pop()
                        health = 0
                        break
                
                if health > 0:
                    stack.append([pos, health, direction, idx])
        
        # Step 4: Sort survivors by original index
        stack.sort(key=lambda x: x[3])
        
        # Step 5: Return healths
        return [robot[1] for robot in stack]