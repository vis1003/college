
import java.util.Scanner; 
class Knapsack 
{ 
	public static void main(String[] args) 
	{
		Scanner sc=new Scanner(System.in); 
		int object,m;
		System.out.println("Enter the Total Objects");
		object=sc.nextInt();
		int weight[]=new int[object]; 
		int profit[]=new int[object]; 
		System.out.println("Enter the Profits:"); 
		for(int i=0;i<object;i++) 
			profit[i]=sc.nextInt();
		System.out.println("Enter the weights:"); 
		for(int i=0;i<object;i++)
			weight[i]=sc.nextInt();
		System.out.println("Enter the Knapsack capacity");
		m=sc.nextInt();
		double p_w[]=new double[object];
		for(int i=0;i<object;i++)
		{
			p_w[i]=(double)profit[i]/(double)weight[i];
		}
		System.out.println("");
		System.out.println("-------------------");
		System.out.println("-----Data-Set------");
		System.out.print("-------------------");
		System.out.println("");
		System.out.print("Objects\t");
		for(int i=1;i<=object;i++)
		{
			System.out.print(i+"\t");
		}
		System.out.println();
		System.out.print("Profit\t");
		for(int i=0;i<object;i++)
		{
			System.out.print(profit[i]+"\t");
		}
		System.out.println();
		System.out.print("Weight\t");
		for(int i=0;i<object;i++)
		{
			System.out.print(weight[i]+"\t");
		}
		System.out.println();
		System.out.print("P/W\t");
		for(int i=0;i<object;i++)
		{
			System.out.print(p_w[i]+"\t");
		}
		for(int i=0;i<object-1;i++)
		{
			for(int j=i+1;j<object;j++)
			{
				if(p_w[i]<p_w[j])
				{
					double temp=p_w[j];
					p_w[j]=p_w[i];
					p_w[i]=temp;
					
					int temp1=profit[j];
					profit[j]=profit[i];
					profit[i]=temp1;
					
					int temp2=weight[j];
					weight[j]=weight[i];
					weight[i]=temp2;
			}
			}
		}
		System.out.println("");
		System.out.println("-------------------");
		System.out.println("--After Arranging--");
		System.out.print("-------------------");
		System.out.println("");
		System.out.print("Objects\t");
		for(int i=1;i<=object;i++)
		{
			System.out.print(i+"\t");
		}
		System.out.println();
		System.out.print("Profit\t");
		for(int i=0;i<object;i++)
		{
			System.out.print(profit[i]+"\t");
		}
		System.out.println();
		System.out.print("Weight\t");
		for(int i=0;i<object;i++)
		{
			System.out.print(weight[i]+"\t");
		}
		System.out.println();
		System.out.print("P/W\t");
		for(int i=0;i<object;i++)
		{
			System.out.print(p_w[i]+"\t");
		}
		int k=0;
		double sum=0;
		System.out.println();
		while(m>0)
		{
			if(weight[k]<m)
			{
				
				sum+=1*profit[k];
				m=m-weight[k];
				k++;
			}
			else
			{
				double x=m*profit[k]/weight[k];
				sum=sum+x;
				m=0;
			}
		
		}
		System.out.println("Final Profit is="+sum);
	}
}