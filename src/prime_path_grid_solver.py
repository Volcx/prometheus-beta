def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_path(grid):
    """
    Find a continuous path of cells that form a prime number sequence.
    
    Args:
        grid (List[List[int]]): 2D grid of numbers
    
    Returns:
        List[tuple]: A list of (row, col) coordinates forming a prime number path, 
                     or an empty list if no such path exists
    """
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def dfs(x, y, current_path, current_number):
        # If current path number is not prime, return None
        if not is_prime(current_number):
            return None
        
        # Check if this is a valid solution (at least 2 steps long)
        if len(current_path) > 1:
            return current_path
        
        # Possible move directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            
            # Check if next move is valid
            if is_valid_move(next_x, next_y) and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                
                # Try finding a path from the next cell
                result = dfs(next_x, next_y, 
                             current_path + [(next_x, next_y)], 
                             current_number * 10 + grid[next_x][next_y])
                
                if result:
                    return result
                
                # Backtrack
                visited.remove((next_x, next_y))
        
        return None
    
    # Try starting from each cell
    for r in range(rows):
        for c in range(cols):
            visited.clear()
            visited.add((r, c))
            
            path = dfs(r, c, [(r, c)], grid[r][c])
            
            if path:
                return path
    
    return []