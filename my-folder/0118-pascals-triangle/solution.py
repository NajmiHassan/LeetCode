class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []

        for i in range(numRows):

            row = [0] * (i + 1)

            row[0], row[-1] = 1, 1

            if i > 1 :

                for j in range(1, i):

                    row[j] = arr[i - 1][j - 1] + arr[i - 1][j]  
            
            arr.append(row)

        return arr
