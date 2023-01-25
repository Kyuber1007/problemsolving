boolean solution(int n) {
    
    int tem = n;
    int count = 0;
    while(tem > 0){
        count++;
        tem /= 10;
    }
    if (count %2 == 1)
        return false;
    
    int sum1 = 0, sum2 = 0;
    int i = 0;
    while(n > 0){
        if(i < count/2){
            sum1 += n % 10; 
        }
        else{
            sum2 += n % 10;
        }
        i++;
        n = n/10;
    }

    if(sum1 == sum2)
        return true;
    
    return false;
}
