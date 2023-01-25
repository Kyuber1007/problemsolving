int solution(String s1, String s2) {
    int count = 0;
    int i = 0;
    while(i<s1.length()){
        for(int j = 0; j < s2.length(); j++){
            if(s1.charAt(i) == s2.charAt(j)){
                s1 = s1.replaceFirst(String.valueOf(s1.charAt(i)), "");
                s2 = s2.replaceFirst(String.valueOf(s2.charAt(j)), "");
                i--;
                count++;
                break;
            }
        }
        i++;
    }
    return count;
}
