class Solution {
    public int solution(int n, String control) {
        int wc = 0;
        int sc = 0;
        int dc = 0;
        int ac = 0;
        for (String c : control.split("")) {
            if (c.equals("w")){
                wc += 1;
            } else if (c.equals("s")) {
                sc += 1;
            } else if (c.equals("d")) {
                dc += 1;
            } else {
                ac += 1;
            }
        }
        return n + (1 * wc) - (1 * sc) + (10 * dc) - (10 * ac);
    }
}