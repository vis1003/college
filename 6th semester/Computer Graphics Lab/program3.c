#include <GL/glut.h>
#include <stdio.h>

void init()
{
	glClearColor(1,1,1,0);
	gluOrtho2D(-500,500,-500,500);
}

void drawTriangle()
{
	glBegin(GL_POLYGON);
	glVertex2f(100,100);
	glVertex2f(200,100);
	glVertex2f(150,150);
	glEnd();
}

void translate()
{
	glPushMatrix();
	glTranslated(100,0,0);
	drawTriangle();
	glPopMatrix();
}

void rotate()
{
	glPushMatrix();
	glRotated(45,0,0,1);
	drawTriangle();
	glPopMatrix();
}

void fixed_point_rotate()
{
	glColor3f(1,1,0);	//yellow
	glPushMatrix();
	glTranslated(100,100,0);	//translate back to original position
	glRotated(45,0,0,1);		//rotate
	glTranslated(-100,-100,0);	//translate to origin
	drawTriangle();
	glPopMatrix();
}

void scale()
{
	glPushMatrix();
	glScaled(2,2,1);
	drawTriangle();
	glPopMatrix();
}

void fixed_point_scale()
{
	glColor3f(1,1,0);	//yellow
	glPushMatrix();
	glTranslated(100,100,0);	//translate back to original position
	glScaled(2,2,1);		//scale
	glTranslated(-100,-100,0);	//translate to origin
	drawTriangle();
	glPopMatrix();
}

void menu_function(int ch)
{
	switch(ch)
		{
			case 1:
				translate();
				break;
			case 2:
				rotate();
				break;
			case 3:
				fixed_point_rotate();
				break;
			case 4:
				scale();
				break;
			case 5:
				fixed_point_scale();
				break;
			default:
				exit(0);
		}	
}

void display()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glClearColor(1,1,1,0);	
	glColor3f(1,0,0);
	drawTriangle();
	glFlush();
}

int main(int argc, char** argv)
{
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE);
	glutInitWindowSize(500,500);
	glutCreateWindow("2D transformation");
	init();
	glutCreateMenu(menu_function);
	glutAddMenuEntry("Translate",1);
	glutAddMenuEntry("Rotate about origin",2);
	glutAddMenuEntry("Rotate about fixed point",3);
	glutAddMenuEntry("Scale about origin",4);
	glutAddMenuEntry("Scale about fixed point",5);
	glutAddMenuEntry("Exit",6);
	glutAttachMenu(GLUT_RIGHT_BUTTON);
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}
