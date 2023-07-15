import java.util.Random;
import java.util.Scanner;

public class merge_sort{
	 public static void main(String[] args) {
	        Scanner sc = new Scanner(System.in);
	        msort obj=new msort();
	        System.out.println("Enter length: ");
	        int n = sc.nextInt();
	        obj.create(n, 2);
	        long t1,t2,t;
	        t1=System.nanoTime();
	        obj.sort(0, n - 1);
	        t2=System.nanoTime();
	        t=(t2-t1)/1000000;
	        System.out.println("Time taken:"+t+" ms");
	 }
}

class msort {
	int n; 
	int A[];
	int temp[];
	
	void create(int n, int choice)
	 {
		 this.n=n;
		 A=new int[n];
		 temp=new int[n];
		 if (choice==0)
		 {
			 for(int i=0;i<n;i++)
				 A[i]=i;
				 
		}
		 else if (choice==1)
		 {
			 for(int i=0;i<n;i++)
				 A[i]=n-i;
			
		 }
		 else
		 {
			 Random rand=new Random();
					 for (int i=0;i<n;i++)
						 A[i]=rand.nextInt(1000000);
		 }
	}
	
	void display()
	{
		for(int i=0;i<n;i++)
			System.out.print(A[i]+", ");
		System.out.println();
	}
	
	void mergesort(int low, int mid, int high)
	{
			int i = low, j = mid + 1, k = low;
	        while (i <= mid && j <= high) {
	            if (A[i] <= A[j])
	                temp[k++] = A[i++];
	            else 
	                temp[k++] = A[j++];
	        }

	        while (i <= mid)
	            temp[k++] = A[i++];

	        while (j <= high)
	            temp[k++] = A[j++];

	        for(int l=low;l<=high;l++)
	        	A[l]=temp[l];
	}
	
	void sort(int low, int high) {
        if (low < high) {
            int mid = (low + high) / 2;
            sort(low, mid);
            sort(mid + 1, high);
            mergesort(low, mid, high);
        }
    }
}

