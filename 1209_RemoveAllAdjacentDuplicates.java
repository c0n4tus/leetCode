class Solution {
    public String removeDuplicates(String word, int k) {
        
        Stack<Pair> st = new Stack<>();
        int i = 0;
        int n = word.length();
        while(i < n){
            char curr = word.charAt(i);
            int count = 1;
            int j = i+1;
            while(j < n && curr == word.charAt(j)){
                count++;
                j++;
            }
            i = j;
            if(count % k == 0){
                continue;
            }
            // System.out.println(curr+" "+count%k);
            Pair currPair = new Pair(curr,count%k);
            while(!st.isEmpty() && currPair.character == st.peek().character){
                currPair.freq += st.peek().freq;
                st.pop();
            }
            currPair.freq %= k;
            if(currPair.freq != 0)
                st.push(currPair);
        }
        
        StringBuilder sb = new StringBuilder();
        Iterator<Pair> it = st.iterator();
        while(it.hasNext()){
            Pair p = it.next();
            int count = p.freq;
            while(count-- > 0){
                sb.append(p.character);
            }
        }
        return new String(sb);
    }
    
    static class Pair{
        char character;
        int freq;
        
        Pair(char character, int freq){
            this.character = character;
            this.freq = freq;
        }

    }
}