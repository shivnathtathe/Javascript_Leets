class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = "1234567890"
        
      
        for row in board:
            non_empty_elements = [element for element in row if element in numbers]
            if len(non_empty_elements) != len(set(non_empty_elements)):
                return False
        
       
        for col in range(9):
            non_empty_elements = [board[row][col] for row in range(9) if board[row][col] in numbers]
            if len(non_empty_elements) != len(set(non_empty_elements)):
                return False
        
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                non_empty_elements = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3) if board[x][y] in numbers]
                if len(non_empty_elements) != len(set(non_empty_elements)):
                    return False
        
        return True

        
                
            
        
        

