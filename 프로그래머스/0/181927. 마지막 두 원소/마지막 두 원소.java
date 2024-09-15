import java.util.*;
class Solution {
    public int[] solution(int[] num_list) {
        int size = num_list.length;
        int last = num_list[size - 1];
        int second = num_list[size - 2];
        int[] answer = Arrays.copyOf(num_list, size + 1);
        answer[size] = last > second ? last - second : last * 2;
        return answer;
    }
}