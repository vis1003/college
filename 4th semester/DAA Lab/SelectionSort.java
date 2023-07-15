import java.util.Scanner;
import java.util.Random;
public class SelectionSort {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		ssort obj=new ssort();
		int n;
		long t1,t2,t;
		System.out.println("Enter length of array:");
		n=sc.nextInt();
		obj.create(n, 2);
		t1=System.nanoTime();
		obj.sort();
		t2=System.nanoTime();
		t=(t2-t1)/1000000;
		System.out.println("Time taken:"+t+" ms");
	}

}

class ssort{
	int n;
	int A[];
	
	void create(int n,int choice)
	{
		this.n=n;
		A=new int[n];
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
			{
				A[i]=rand.nextInt(1000000);
			}
		}
	}
	
	void display()
	{
		for(int i=0;i<n;i++)
			System.out.print(A[i]+", ");
		System.out.println();
	}
	
	void swap(int i, int j)
	{
		int temp;
		temp=A[i];
		A[i]=A[j];
		A[j]=temp;
	}
	
	void sort()
	{
		int min;
		for(int i=0;i<n-1;i++)
		{
			min=i;
			for(int j=i+1;j<n;j++)
			{
				if(A[j]<A[min])
					min=j;
			}
			swap(i,min);
		}
	}
}
