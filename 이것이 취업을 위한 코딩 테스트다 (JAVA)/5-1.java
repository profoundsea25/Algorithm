import java.util.*;

public class Main {

    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();

        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop();
        s.push(1);
        s.push(4);
        s.pop();
        // 최상단 원소부터 출력
        while(!s.empty()) {
            System.out.println(s.peek());
            s.pop();
        }
        // 출력값(최상단) 1 3 2 5
    }
    
}
