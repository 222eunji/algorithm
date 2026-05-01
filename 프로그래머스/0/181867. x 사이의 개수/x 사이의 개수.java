import java.util.ArrayList;


class Solution {
    public int[] solution(String myString) {
        myString += "x";
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0, cnt = 0; i < myString.length(); i++){
            if (myString.charAt(i) != 'x'){
                cnt++;
            } else {
                arr.add(cnt);
                cnt = 0;
            }
        }

        return arr.stream().mapToInt(Integer::intValue).toArray();
    }
}