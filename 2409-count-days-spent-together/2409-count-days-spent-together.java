class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int startA = getDayOfYear(arriveAlice, days);
        int endA = getDayOfYear(leaveAlice, days);
        int startB = getDayOfYear(arriveBob, days);
        int endB = getDayOfYear(leaveBob, days);
        int start = Math.max(startA, startB);
        int end = Math.min(endA, endB);
        return Math.max(0, end - start + 1);
    }
    private int getDayOfYear(String date, int[] days) {
        int m = Integer.parseInt(date.substring(0, 2));
        int d = Integer.parseInt(date.substring(3, 5));
        int total = d;
        for (int i = 0; i < m - 1; i++) {
            total += days[i];
        }
        return total;
    }
}