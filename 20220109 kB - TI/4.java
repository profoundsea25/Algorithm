import java.util.*;

class Solution {
    // 위치와 높이 정보를 담을 ArrayList 초기화
    public static ArrayList<ArrayList<Integer>> map = new ArrayList<ArrayList<Integer>>();
    
    // 그룹이 몇개인지 세는 함수
    public int countGroup(ArrayList<Integer> map, int k) {
        if (map.isEmpty()) return 0;

        int count = 0;

        for (int j = 1; j < map.size(); j++) {
            if (map.get(j) - map.get(j-1) > k) {
                count += 1;
            }
        }
        return count+1;
    }

    public int solution(int[][] tower, int k) {
        
        int answer = 0;

        // 높이와 위치 정보를 담을 ArrayList 초기화 (높이가 1~10이므로 0을 제외하기 위해 11개를 추가)
        for (int i = 0; i <= 10; i++) {
            map.add(new ArrayList<Integer>());
        }

        // 송전탑의 위치를 높이에 해당하는 ArrayList 인덱스 번호에 저장
        for (int i = 0; i < tower.length; i++) {
            map.get(tower[i][1]).add(tower[i][0]);
        }

        // 몇 개의 그룹인지 카운트
        for (int i = 1; i < map.size(); i++) {
            answer += countGroup(map.get(i), k);
        }
        
        return answer;
    }
}