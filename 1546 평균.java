import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		double max = 0;
		double sum = 0;
		int N = sc.nextInt();
		int[] score = new int[N];
		
		for(int i = 0; i < N; i++) {
			score[i] = sc.nextInt();
			sum += score[i];
			if(max <= score[i])
				max = score[i];
		}
		double average = (sum/N)/max*100;
		System.out.println(average);
	}
}
