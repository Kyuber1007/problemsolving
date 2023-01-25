int solution(int[][] matrix) {
    int sum = 0;
    int[] below = new int[matrix[0].length];

    for(int i = 0; i < matrix.length; i++){
        for(int j = 0; j < matrix[i].length; j++){
            if(matrix[i][j] == 0){
                below[j] = -1;
            }
            if(below[j] != -1){
                sum += matrix[i][j];
            }
        }
    }
    return sum;
}
