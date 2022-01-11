import java.util.*;

class Solution {
    // 중복되는 괄호 문자열을 처리하기 위한 HashSet
    public static HashSet<String> o = new HashSet<>();
    public static HashSet<String> x = new HashSet<>();

    // 옳은 괄호인지 판별
    public int isCorrect(String str) {
        
        int check = 0;
        
        // ) 로 시작하면 옳지 않은 괄호열
        char checkFirstChar = str.charAt(0);
        if (checkFirstChar == ')') return 0;

        // ( 이 나오면 +1, ) 이 나오면 -1 로 계산. 중간에 음수가 나오면 )이 더 있음을 나타내므로 옳지 않은 괄호
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '(') check += 1;
            else if (c == ')') check -= 1;

            if (check < 0) return 0;
        }
        // 결과가 0이면 옳은 괄호, 그 외일 경우 옳지 않은 괄호
        if (check == 0) return 1;
        else return 0;
    }

    public long solution(String[] arr1, String[] arr2) {
        long answer = 0;

        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr2.length; j++) {
                // 두 괄호를 합쳐서,
                String str = arr1[i] + arr2[j];
                // 이미 옳다고 판별했으면 +1
                if (o.contains(str)) {
                    answer += 1;
                    continue;
                }
                // 이미 옳지 않다고 판별했다면 0
                else if (x.contains(str)) {
                    continue;
                }
                // 이미 판별한 것이 아닐 경우, isCorrect를 실행. 옳으면 +1, 아니면 +0
                if (isCorrect(str) == 1) {
                    answer += 1;
                    o.add(str);
                }
                else if (isCorrect(str) == 0) {
                    x.add(str);
                }
            }
        }

        return answer;
    }
}