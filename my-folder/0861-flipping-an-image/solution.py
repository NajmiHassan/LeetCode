class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[x ^ 1 for x in reversed(row)] for row in image]
       
       
        # for row in image:
        #     row.reverse()
        #     for index in range(len(image)):
        #         row[index] ^= 1
        # return image

