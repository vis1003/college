#include <GL/glut.h>

void displayMe()
{
	glClearColor(1.0,1.0,0.0,1.0); //Background
	glClear(GL_COLOR_BUFFER_BIT);
	
	glFlush();
	
}
int main(int argc, char** argv)
{
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE);
	glutInitWindowSize(500,500);
	glutInitWindowPosition(150,100);
	
	glutCreateWindow("Hello world");
	glutDisplayFunc(displayMe); //Call back
	glutMainLoop();
	return 0;
}
