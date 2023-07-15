import java.util.Scanner;
import java.util.Random;

public class QuickSort {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n;
		long t1,t2,t;
		qsort obj=new qsort();
		System.out.println("Enter length of array:");
		n=sc.nextInt();
		obj.create(n, 0);
		t1=System.nanoTime();
		obj.sort(0,n);
		t2=System.nanoTime();
		t=(t2-t1)/1000000;
		System.out.println("Time taken:"+t+" ms");
	}

}

class qsort{
	int n;
	int A[];
	void create(int n, int choice)
	{
		this.n=n;
		A=new int[n+1];
		if(choice==0)
		{
			for(int i=0;i<n;i++)
				A[i]=i;
		}
		else if(choice==1)
		{
			for(int i=0,j=n-1;i<n&&j>=0;i++,j--)
				A[i]=j;
		}
		else
		{
			Random rand=new Random();
			for(int i=0;i<n;i++)
				A[i]=rand.nextInt(1000000);
		}
		A[n]=1000001;
	}
	
	void display()
	{
		for(int i=0;i<n;i++)
			System.out.print(A[i]+", ");
		System.out.println();
	}
	
	void swap(int i,int j)
	{
		int temp;
		temp=A[i];
		A[i]=A[j];
		A[j]=temp;
	}
	
	int partition(int l, int h)
	{
		int i=l+1, j=h, p = A[l];
		while(i<=j)
		{
			while(i<=j && p >= A[i])
				i++;
			while(i<=j && p <= A[j])
				j--;
			if(i<j)
				swap(i,j);
		}
		swap(l,j);
		return j;
	}
	
	void sort(int l, int h)
	{
		int s;
		if(l<h)
		{
			s = partition(l,h);
			sort(l,s-1);
			sort(s+1,h);
		}
	}
}
