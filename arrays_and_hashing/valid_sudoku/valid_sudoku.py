class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col_hashmap = {}
        row_hashmap = {}
        grid_hashmap = {}
        for row_idx in range(len(board)):
            for col_idx, value in enumerate(board[row_idx]):
                if value != ".":
                    # can be done in a sorted way
                    if col_idx in col_hashmap:
                        if value in col_hashmap[col_idx]:
                            return False
                        else:
                            col_hashmap[col_idx].add(value)
                    else:
                        col_hashmap[col_idx] = {value}

                    if row_idx in row_hashmap:
                        if value in row_hashmap[row_idx]:
                            return False
                        else:
                            row_hashmap[row_idx].add(value)
                    else:
                        row_hashmap[row_idx] = {value}

                    insert_worked = self.insert(grid_hashmap, row_idx,col_idx, value)
                    if insert_worked is False:
                        return False
        print(grid_hashmap)
        return True

    def insert(self, grid_hashmap, row_idx, col_idx, value):

        counter = 0
        if col_idx > 2 and col_idx <= 5:
            counter += 10
        elif col_idx > 5:
            counter += 20

        if row_idx > 2 and row_idx <= 5:
            counter += 1
        elif row_idx > 5:
            counter += 2


        # print(row_idx, col_idx, counter, "-----", value)
        if counter in grid_hashmap:
            if value in grid_hashmap[counter]:
                return False
            else:
                grid_hashmap[counter].add(value)
        else:
            grid_hashmap[counter] = {value}
        return True




# print(Solution().isValidSudoku(
#     board=
#         [ ["5", "3", ".", ".", "7", ".", ".", ".", "."]
#         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#         , [".", "9", "8", ".", ".", ".", ".", "6", "."]
#         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#         , [".", ".", "", ".", ".", ".", ".", "7", "9"]]
# ))
