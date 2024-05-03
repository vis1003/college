#include <GL/glut.h>

void draw(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glClearColor(1.0,0.0,1.0,1.0);	
	glColor3d(1.0,1.0,0.0);
	glBegin(GL_LINE_LOOP);
	glVertex2f(-0.2,0.2);
	glVertex2f(0.5,0.2);
	glVertex2f(0.5,0.6);
	glVertex2f(-0.2,0.6);
	glColor3d(1.0,0.0,1.0);
	glEnd();
	glFlush();
}

int main(int argc, char** argv)
{
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE| GLUT_RGB);
	glutInitWindowPosition(50,25);
	glutInitWindowSize(500,500);
	glutCreateWindow("Triangle Window");
	glutDisplayFunc(draw);
	glutMainLoop();
	return 0;
}
