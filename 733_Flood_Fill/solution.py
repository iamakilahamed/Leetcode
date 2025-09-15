class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        self.fill(image, sr, sc, color, image[sr][sc])
        return image
    
    def fill(self, image, sr, sc, color, current):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if current != image[sr][sc]:
            return
        image[sr][sc] = color
        self.fill(image, sr - 1, sc, color, current)
        self.fill(image, sr + 1, sc, color, current)
        self.fill(image, sr, sc - 1, color, current)
        self.fill(image, sr, sc + 1, color, current)