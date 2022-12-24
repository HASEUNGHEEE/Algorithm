class Solution {
    public double solution(int[] arr) {
        double sum = 0;
        int count = 0;
        for (int i : arr) {
            sum += i;
            count++;
        }
        return sum / count;
    }
}