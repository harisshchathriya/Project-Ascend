import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		int a[]=new int[n];
		for(int i=0; i<n; i++) {
			a[i]=s.nextInt();
		}
		hasing(a);
	}
	public static void hasing(int a[]) {
		int n=a.length;
		int max=a[0],min=a[0];
		for(int i=1; i<n; i++) {
			if(max<a[i]) {
				max=a[i];
			}
			else if(min>a[i]) {
				min=a[i];
			}
		}
		int arr[]=new int[max+1];
		for(int i=0; i<n; i++) {
			arr[a[i]]++;
		}
		int k=0;
		while(min<max) {
			while(arr[max]==0) {
				max--;
			}
			while(arr[min]==0) {
				min++;
			}
			if(min<max) {
				a[k++]=max;
				a[k++]=min;
				min++;
				max--;
			}
		}
		if(n%2==1) {
			a[k]=min;
		}
		for(int i=0; i<n; i++) {
			System.out.print(a[i]+" ");
		}
	}
}