String[] solution(String[] inputArray) {
    int max = 0;
    ArrayList<String> result = new ArrayList<String>();
    
    for(int i = 0; i < inputArray.length; i++){
        int stringLength = inputArray[i].length();
        
        if(stringLength > max){
            result.clear();
            max = stringLength;
        }
        if(stringLength == max){
            result.add(inputArray[i]);
        }
    }    
    
    return result.toArray(String[]::new);
}
