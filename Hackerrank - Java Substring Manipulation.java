public static String getSmallestAndLargest(String s, int k) {
        if (s.length()<k){
            return null;
        }
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        
        for (int i = 1; i <= s.length()-k; i++){
            String ngram = s.substring(i, i+k);
            if (ngram.compareTo(smallest)<0){
                smallest = ngram;
            }
            if (ngram.compareTo(largest)>0){
                largest = ngram;
            }
        }
        return smallest + "\n" + largest;
        
    }