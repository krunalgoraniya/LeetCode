class Solution {
    public boolean checkIfPangram(String sentence) {
         for(char ch = 'a'; ch <= 'z'; ch++) {
            boolean found = false;

            for(int i = 0; i < sentence.length(); i++) {
                if(ch == sentence.charAt(i)) {
                    found = true;
                    break;
                }
            }
            if(found == false)
                return false;
        }
        return true;
    }
}