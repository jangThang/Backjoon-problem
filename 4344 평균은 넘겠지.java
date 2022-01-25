import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int c = sc.nextInt();
		for(int i = 0; i < c; i++) {
			int n = sc.nextInt();
			int[] arr = new int[n];
			double sum = 0.0;
			
			for(int j = 0; j < n; j++) {
				arr[j] = sc.nextInt();
				sum += arr[j];
			}
			double average = sum/(double)n;
			int high = 0;
			for(int j = 0; j < n; j++) {
				if(arr[j] > average)
					high++;
			}
			double average2 = ((double)high/(double)n) * 100.0;
			System.out.println(String.format("%.3f", average2) + "%");
		}
	}
}
