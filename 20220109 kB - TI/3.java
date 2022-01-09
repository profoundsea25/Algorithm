import java.util.*;

class Solution {

    // 강의를 설명하는 클래스
    class Lecture {
        private String day;
        private int startTime;
        private int endTime;
        
        public Lecture(String day, int startTime, int endTime) {
            this.day = day;
            this.startTime = startTime;
            this.endTime = endTime;
        }

        public String getDay() {
            return this.day;
        }
        public int getStartTime() {
            return this.startTime;
        }
        public int getEndTime() {
            return this.endTime;
        }
    }

    // 경우의 수 세기
    public int countTrue(String[] scheduleCase) {
        ArrayList<Lecture> result = convert(scheduleCase);
        // result에서 먼저 요일이 곂치는지 확인하고,
        for (int i = 0; i < result.size(); i++) {
            for (int j = i+1; j < result.size()-1; j++) {
                if (result.get(i).getDay().equals(result.get(j).getDay())) {
                    if (result.get(i).getStartTime() < result.get(j).getStartTime() && result.get(i).getEndTime() < result.get(j).getStartTime()) return 0;
                    else if result.get(i).getEndTime() > result.get(j).getStartTime() && result.get(i).getEndTime() < result.get(j).getEndTime()
                }
            }
        }

        // 곂치는 요일의 startTime과 endTime이 서로 교차하는지 비교해서
        // 교차하는 시간이 없으면 return 1;
        // 교차하는 시간이 있으면(가능하지 않은 시간표면) return 0;
    } 

    // 스케쥴 데이터 처리
    public ArrayList<Lecture> convert(String[] scheduleCase) {
        ArrayList<Lecture> result = new ArrayList<Lecture>();
        for (int i = 0; i < scheduleCase.length; i++) {
            if (scheduleCase.length == 8) {
                String day = scheduleCase[i].split(" ")[0];
                String time = scheduleCase[i].split(" ")[4];
                int startTime = Integer.parseInt(time.split(":")[0]) * 60 + Integer.parseInt(time.split(":")[1]);
                int endTime = startTime + 180;
                Lecture lecture = new Lecture(day, startTime, endTime);
                result.add(lecture);
            }
        }
        return result;
    }

    public int solution(String[][] schedule) {
        int answer = 0;
        for (int i = 0; i < schedule[0].length; i++) {
            for (int j = 0; j < schedule[1].length; j++) {
                for (int k = 0; j < schedule[2].length; j++) {
                    for (int l = 0; j < schedule[3].length; j++) {
                        for (int m = 0; j < schedule[4].length; j++) {
                            String[] scheduleCase = {schedule[0][i], schedule[1][j], schedule[2][k], schedule[3][l], schedule[4][m]};
                            answer += countTrue(scheduleCase);
                        }
                    }
                }
            }
        }
        return answer;
    }
}