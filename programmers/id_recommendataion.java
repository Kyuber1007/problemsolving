class Solution {
    public String solution(String new_id) {
        String step1 = new_id.toLowerCase();

        char[] tem = step1.toCharArray();
        String step2 = "";
        for (char c : tem) {
            if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || c == '-' || c == '_' || c == '.') {
                step2 += c;
            }
        }
        System.out.println(step2);

        String step3 = step2;
        while (step3.contains("..")) {
            step3 = step3.replace("..", ".");
        }

        String step4 = step3;
        while (true) {
            if (step4.startsWith("."))
                step4 = step4.substring(1);
            else if (step4.endsWith("."))
                step4 = step4.substring(0, step4.length() - 1);
            else
                break;
        }
        System.out.println(step4);

        String step5 = step4;
        if (step5.isBlank()) {
            step5 = "a";
        }

        String step6 = step5;
        if (step6.length() > 15) {
            step6 = step6.substring(0, 15);
        }
        while (true) {
            if (step6.endsWith("."))
                step6 = step6.substring(0, step6.length() - 1);
            else
                break;
        }

        String step7 = step6;
        if (step7.length() < 3) {
            String temp = step7.substring(step7.length() - 1);
            while (step7.length() < 3) {
                step7 = step7.concat(temp);
            }
        }
        return step7;
    }
}