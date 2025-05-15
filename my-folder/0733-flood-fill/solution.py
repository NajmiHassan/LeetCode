class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS SOLTION APPROACH
        original_color = image[sr][sc]
        if original_color == color:
            return image

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(image), len(image[0])

        # Use a queue for BFS
        queue = deque()
        queue.append((sr, sc))

        while queue:
            x, y = queue.popleft()
            image[x][y] = color

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == original_color:
                    queue.append((nx, ny))

        return image
