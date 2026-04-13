class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        current_row = set()
        cols = [set() for _ in range(9)]

        for row in range(len(board)):
            for num in range(len(board[row])):
                # add to boxes
                box_index = (row // 3) * 3 + (num//3)
                if board[row][num] != "." and board[row][num] in boxes[box_index]:
                    return False
                boxes[box_index].add(board[row][num])

                # add to cols
                if board[row][num] != "." and board[row][num] in cols[num]:
                    return False # Number already in the column

                cols[num].add(board[row][num])

                # add to rows
                if board[row][num] != "." and board[row][num] in current_row:
                    return False # There is a duplicate in the rows

                # increment rows
                current_row.add(board[row][num])

            # reset rows
            current_row = set()
        return True
            
            