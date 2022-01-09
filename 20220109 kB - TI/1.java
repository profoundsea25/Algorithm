class Solution {
    // 기본료 계산
    public int base(int[][] fees, int usage) {
        for (int i = 0; i < fees.length; i++) {
            if (fees[i][0] >= usage) return fees[i][1];
        }
        return fees[fees.length-1][1];
    }

    // 기본료 제외 전기세 계산
    public int cal(int[][] fees, int usage) {
        int cost = 0;

        if (fees[0][0] <= usage) {
            cost += fees[0][2] * fees[0][0];
            usage -= fees[0][0];
        } else {
            cost += fees[0][2] * usage;
            return cost;
        }

        for (int i = 1; i < fees.length; i++) {
            if (i == fees.length-1) {
                cost += (usage) * fees[i][2];
                break;
            }

            if (fees[i][0]-fees[i-1][0] <= usage) {
                cost += (fees[i][0]-fees[i-1][0]) * fees[i][2];
                usage -= fees[i][0]-fees[i-1][0];
            } else {
                cost += fees[i][2] * usage;
                break;
            }
        }
        return cost;
    }

    public int solution(int[][] fees, int usage) {
        int answer = 0;
        
        // 기본료 책정
        answer += base(fees, usage);
        answer += cal(fees, usage);

        return answer;
    }
}