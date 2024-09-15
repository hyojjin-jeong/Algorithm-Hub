import java.util.*;
class Solution {
    public int solution(int[] num_list) {
        String even = "";
        String odd = "";
        for (int n : num_list) {
            if (n % 2 == 0) {
                even += n;
            } else {
                odd += n;
            }
        }
        int ans1 = even.length() > 0 ? Integer.valueOf(even) : 0;
        int ans2 = odd.length() > 0 ? Integer.valueOf(odd) : 0;
        return ans1 + ans2;
    }
}