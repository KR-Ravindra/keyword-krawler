import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class StringAlgorithms {

    public static List<Integer> rabinKarp(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        // Implementation of Rabin-Karp algorithm
        int n = text.length();
        int m = pattern.length();
        int patternHash = pattern.hashCode();

        for (int i = 0; i <= n - m; i++) {
            if (text.substring(i, i + m).hashCode() == patternHash && text.substring(i, i + m).equals(pattern)) {
                matches.add(i);
            }
        }
        return matches;
    }

    public static List<Integer> naiveStringMatch(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        // Implementation of Naive String Matching algorithm
        int n = text.length();
        int m = pattern.length();

        for (int i = 0; i <= n - m; i++) {
            boolean match = true;
            for (int j = 0; j < m; j++) {
                if (text.charAt(i + j) != pattern.charAt(j)) {
                    match = false;
                    break;
                }
            }
            if (match) {
                matches.add(i);
            }
        }
        return matches;
    }

    public static class SegmentTree {
        int[] tree;

        public SegmentTree(int[] arr) {
            int n = arr.length;
            int treeSize = 2 * n - 1;
            tree = new int[treeSize];
            buildTree(arr, 0, 0, n - 1);
        }

        private void buildTree(int[] arr, int node, int start, int end) {
            if (start == end) {
                tree[node] = arr[start];
            } else {
                int mid = (start + end) / 2;
                int leftChild = 2 * node + 1;
                int rightChild = 2 * node + 2;
                buildTree(arr, leftChild, start, mid);
                buildTree(arr, rightChild, mid + 1, end);
                tree[node] = tree[leftChild] + tree[rightChild];
            }
        }
    }

    public static List<Integer> kmpStringMatch(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        // Implementation of KMP algorithm
        int n = text.length();
        int m = pattern.length();
        int[] lps = computeLPSArray(pattern);

        int i = 0; // Index for text[]
        int j = 0; // Index for pattern[]

        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }
            if (j == m) {
                matches.add(i - j);
                j = lps[j - 1];
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return matches;
    }

    private static int[] computeLPSArray(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;

        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        return lps;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Select an algorithm to run:");
        System.out.println("1. Rabin-Karp");
        System.out.println("2. Naive String Matching");
        System.out.println("3. Segment Tree");
        System.out.println("4. KMP String Matching");

        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        System.out.print("Enter the text: ");
        String text = scanner.nextLine();
        System.out.print("Enter the pattern: ");
        String pattern = scanner.nextLine();

        long startTime, endTime;
        List<Integer> matches;

        switch (choice) {
            case 1:
                startTime = System.currentTimeMillis();
                matches = rabinKarp(text, pattern);
                endTime = System.currentTimeMillis();
                System.out.println("Rabin-Karp Matches: " + matches);
                break;
            case 2:
                startTime = System.currentTimeMillis();
                matches = naiveStringMatch(text, pattern);
                endTime = System.currentTimeMillis();
                System.out.println("Naive String Matching Matches: " + matches);
                break;
            case 3:
                startTime = System.currentTimeMillis();
                SegmentTree segmentTree = new SegmentTree(new int[]{1, 2, 3, 4, 5});
                // Use Segment Tree methods and measure execution time
                endTime = System.currentTimeMillis();
                break;
            case 4:
                startTime = System.currentTimeMillis();
                matches = kmpStringMatch(text, pattern);
                endTime = System.currentTimeMillis();
                System.out.println("KMP Matches: " + matches);
                break;
            default:
                System.out.println("Invalid choice.");
                return;
        }

        // Count word occurrences
        String[] words = text.split("\\s+");
        Map<String, Integer> wordCounts = new HashMap<>();
        for (String word : words) {
            wordCounts.put(word, wordCounts.getOrDefault(word, 0) + 1);
        }

        System.out.println("Execution time: " + (endTime - startTime) + " ms");

        System.out.println("Word Counts:");
        for (Map.Entry<String, Integer> entry : wordCounts.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
