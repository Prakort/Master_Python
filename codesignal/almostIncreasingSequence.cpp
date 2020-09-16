bool almostIncreasingSequence(std::vector<int> sequence) {
    int count = 0;
    int prev = INT_MIN;
    int prevprev = INT_MIN;
   

    for (auto i = 0;  i < sequence.size() ; i++) {
        int n = sequence[i];
        if (n <= prev){
            count++;
            // [4 5 2 2 2]
            // keep prevprev = 4 , prev = 5 for the rest until n < prev & n > 4 
            // this mean we skip n not 4 and 5
            
            
            // [0 1 5 2 2 2]
            // skip 5, preprev = 0, prev = 2 , n = 2
            // keep moving prev = n 
            // 
            if(n > prevprev){
                // this mean we skip 5, => 1 2
                prev = n;
            }
            
        } else {
            prevprev = prev;
            prev = n;
          
        }
            
    }
    return count <= 1;
    
}

