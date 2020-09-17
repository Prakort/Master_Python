bool boundary(int row, int col, int r, int c){
    return r >= 0 && r < row && c >=0 && c < col;
}
void dfs(int row, int col, int r, int c, std::vector<std::vector<int>> &matrix, std::vector<std::vector<int>> &visited){
    
    if (r < 0 || r >= row || c < 0 || c >= col || visited[r][c]) {
        return;
    }

    visited[r][c] = true;
    dfs(row, col, r+1, c, matrix, visited);
    
}
int matrixElementsSum(std::vector<std::vector<int>> matrix) {
    
    int row = matrix.size();
    int col = matrix[0].size();
    std::vector<std::vector<int>> visited(row,std::vector<int>(col, false));
    
    for ( int i = 0 ; i < row ; i++){
        for ( int j = 0; j < col ; j++){
            if (matrix[i][j] == 0 && !visited[i][j]) {
                dfs(row, col, i, j, matrix, visited);
            }
        }
    }
    int count = 0;
    for ( int i = 0 ; i < row ; i++){
        for ( int j = 0; j < col ; j++){
            if (!visited[i][j]) {
                count += matrix[i][j];
            }
        }
    }
    
    return count;
    
}

int matrixElementsSum(std::vector<std::vector<int>> matrix) {
    
    int row = matrix.size();
    int col = matrix[0].size();
    int count = 0;
    
    for ( int c = 0 ; c < col ; c++){
        for ( int r = 0; r < row ; r++){
            if (matrix[r][c] > 0) {
                count += matrix[r][c];
                
            } else {
                break;
            }
        }
    }

    return count;
    