#include <GL/glut.h>
# include <stdlib.h>
# include <stdio.h>
typedef float point[3];
point v[]={{0.0,0.0,1.0},
{0.0,1.0,0.0},
{-1.0,-1.0,0.0},
{1.0,-1.0,0.0}};

int n;
void triangle(point a, point b, point c)
{
	glBegin(GL_TRIANGLES);
	glVertex3fv(a);
	glVertex3fv(b);
	glVertex3fv(c);
	glEnd();
}

void divide_tri(point a, point b, point c, int m)
{
	point v1,v2,v3;
	int j;
	if(m>0)
	{
		for(j=0;j<3;j++)
			v1[j]=(a[j]+b[j])/2;
		for(j=0;j<3;j++)
			v2[j]=(a[j]+c[j])/2;
		for(j=0;j<3;j++)
			v3[j]=(b[j]+c[j])/2;
		divide_tri(a,v1,v2,m-1);
		divide_tri(c,v2,v3,m-1);
		divide_tri(b,v3,v1,m-1);
	}
	else
		triangle(a,b,c);
}

void tetrahedron(int m)
{
	glColor3f(1.0,0.0,0.0);
	divide_tri(v[0],v[1],v[2],m);
	glColor3f(0.0,1.0,0.0);
	divide_tri(v[0],v[3],v[1],m);
	glColor3f(0.0,0.0,1.0);
	divide_tri(v[0],v[2],v[3],m);
	glColor3f(0.0,0.0,0.0);
	divide_tri(v[3],v[2],v[1],m);
}

void display()
{
	tetrahedron(n);
	glFlush();
}

void init()
{
	glClearColor(1.0,1.0,1.0,1.0);
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
	glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0);
}

int main(int argc, char **argv)
{
	printf("\nEnter the number of recursive steps you want:");
	scanf("%d",&n);
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH);
	glutInitWindowSize(500,500);
	glutCreateWindow("3d Sierpinski's Gasket");
	glutDisplayFunc(display);
	init();
	glEnable(GL_DEPTH_TEST);
	glutMainLoop();
	return 0;
}
