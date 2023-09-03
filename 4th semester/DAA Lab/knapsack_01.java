import java.util.*;
class ks_01{
	int N;
	int weights[];
	int values[];
	int table[][];
	int W;
	
	public void read_data()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter no of items and sack capacity:");
		N=sc.nextInt();
		W=sc.nextInt();
		weights=new int[N+1];
		values=new int[N+1];
		table=new int[N+1][W+1];
		System.out.println("Read item data");
		for(int i=1;i<=N;i++)
		{
			System.out.println("Enter weight and value of item "+i);
			weights[i]=sc.nextInt();
			values[i]=sc.nextInt();
		}
	}
	
	public void find_value()
	{
		int i,j;
		for(i=1;i<N+1;i++)
			for(j=1;j<W+1;j++)
			{
				if(weights[i]<=j && (table[i-1][j])<(table[i-1][j-weights[i]]+values[i]))
					table[i][j]=table[i-1][j-weights[i]]+values[i];
				else
					table[i][j]=table[i-1][j];
			}
		System.out.println("Total value of items taken="+table[N][W]);
		
		System.out.println("Selected items are:");
		j=W;
		for(i=N;i>0;i--)
			if(table[i][j]!=table[i-1][j])
			{
				System.out.println(i);
				j=j-weights[i];
			}
	}
}
public class knapsack_01 {
	public static void main(String[] args)
	{
		ks_01 obj=new ks_01();
		obj.read_data();
		obj.find_value();
	}
}
