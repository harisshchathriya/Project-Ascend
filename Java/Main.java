import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	     Scanner s=new Scanner(System.in);
	     int n=s.nextInt();
	     int a[]=new int[n];
	     for(int i=0;i<n;i++){
	         a[i]=s.nextInt();
	     }
	     int key=s.nextInt();
	     hasing(a,key);
	}
	public static void hasing(int a[],int k){
	    int n=a.length;
	    int max=a[0],min=a[0];
	    for(int i=1;i<n;i++){
	        if(max<a[i]){
	            max=a[i];
	        }
	        else if(min>a[i]){
	            min=a[i];
	        }
	    }
	    int arr[]=new int[max+1];
	    for(int i=0;i<n;i++){
	        arr[a[i]]++;
	    }
	    int c=0;
	    for(int i=max;i>=0;i--){
	        if(arr[i]>0){
	             c++;
	            if(c==k){
	                 System.out.print(i);
	                 return;
	             }
	        }
	    }
	    System.out.print("-1");
	}
}