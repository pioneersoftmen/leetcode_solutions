class Solution:
    def adder(self, count, j, i, res, matrix, first, second, third, fourth, row_len, n):
        if len(res) >= row_len * n:
                return res
        while j <= first:
            if len(res) < row_len * n:
                element = matrix[i][j]
                res.append(element)
                # print(element)
                # print(res)
                count += 1
                j += 1
            elif len(res) == row_len * n:
                return res
        first -= 1    
        i += 1
        j -= 1
        # print(i, j, 'f', first)

        while i <= second:
            if len(res) < row_len * n:
                element = matrix[i][j]
                res.append(element)
                i += 1
                count += 1
                # print(element)
                # print(res)
            elif len(res) == row_len * n:
                return res
        second -= 1
        i -= 1
        j -= 1
        # print(i, j, 's', second)
        while j >= third:
            if len(res) < row_len * n:
                element = matrix[i][j]
                res.append(element)
                j -= 1
                count += 1
                # print(element)
                # print(res)
            elif len(res) == row_len * n:
                return res
        third += 1
        j += 1
        i -= 1
        # print(i, j, third, 'th')
        while i >= fourth:
            if len(res) < row_len * n:
                element = matrix[i][j]
                res.append(element)
                i -= 1
                count += 1
                # print(element)
                # print(res)
            elif len(res) == row_len * n:
                return res
        fourth += 1
        i += 1
        j += 1
        # print(i, j, 'f',fourth)
        # print(res)
        return self.adder(count, j, i, res, matrix, first, second, third, fourth, row_len, n)

    def spiralOrder(self, matrix):
        res = []
        element = matrix[0][0]
        n = len(matrix)
        row_len = len(matrix[0])
        count = 0
        i, j = 0, 0
        first = len(matrix[0]) - 1
        second = n - 1
        third = 0
        fourth = 1
        self.adder(count, j, i, res, matrix, first, second, third, fourth, row_len, n)

        return res


matrix = [[1,2,3],[4,5,6],[7,8,9]] 
# print(matrix)
test = Solution()
print(test.spiralOrder(matrix))
# real answer = [1,2,3,4,8,12,11,10,9,5,6,7]
# my answer = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 8, 5, 6, 7, 6]