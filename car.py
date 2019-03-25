from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective( 60, 1, 0.1, 50)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(0.6,0.6,0.5,1)
    glClear(GL_COLOR_BUFFER_BIT)

def Draw_view():
    glBegin(GL_POLYGON)     #TheRoad
    glColor3f(0.2, 0.3, 0.4)
    glVertex(15, -1, -3)
    glVertex(15, -1, 3)
    glVertex(-15, -1, 3)
    glVertex(-30, -1, -3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(2.5, -1, -0.3)
    glVertex(2.5, -1, 0.3)
    glVertex(-2.5, -1, 0.3)
    glVertex(-2.5, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(5, -1, -0.3)
    glVertex(5, -1, 0.3)
    glVertex(10, -1, 0.3)
    glVertex(10, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-5, -1, -0.3)
    glVertex(-5, -1, 0.3)
    glVertex(-10, -1, 0.3)
    glVertex(-10, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-15, -1, -0.3)
    glVertex(-15, -1, 0.3)
    glVertex(-25, -1, 0.3)
    glVertex(-25, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)  #The tree
    glColor3f(0.3,0.1,0)
    glVertex(-15, -1, -3)
    glVertex(-14.2, -1, -3)
    glVertex(-14.2, 1.5, -3)
    glVertex(-15, 1.5, -3)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.7, 0)
    glVertex(-16, 1.5, -3)
    glVertex(-13.2, 1.5, -3)
    glVertex(-14.6, 3.5, -3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.1, 0)
    glVertex(-7, -1, -3)
    glVertex(-6.2, -1, -3)
    glVertex(-6.2, 1.5, -3)
    glVertex(-7, 1.5, -3)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.7, 0)
    glVertex(-8, 1.5, -3)
    glVertex(-5.2, 1.5, -3)
    glVertex(-6.6, 3.5, -3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.1, 0)
    glVertex(1, -1, -3)
    glVertex(1.8, -1, -3)
    glVertex(1.8, 1.5, -3)
    glVertex(1, 1.5, -3)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.7, 0)
    glVertex(0, 1.5, -3)
    glVertex(2.8, 1.5, -3)
    glVertex(1.4, 3.5, -3)
    glEnd()

angle = 0
x = 0
forward = True
def display():
    global angle
    global x
    global forward
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    Draw_view()

    glLoadIdentity()
    glTranslate(2.5 + x, -2.5 * 0.25, - 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glColor3f(0, 0, 0.1)
    glutSolidTorus(0.2, 0.55, 20, 15)

    glLoadIdentity()
    glTranslate(-2.5 + x, -2.5 * 0.25, - 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glColor3f(0, 0, 0.1)
    glutSolidTorus(0.2, 0.55, 20, 15)

    glLoadIdentity()
    glTranslate(x,0,0)
    glColor3f(1,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glColor3f(1, 1, 0)
    glLoadIdentity()
    glTranslate(0+x,1.25,0)
    glScale(0.5,0.2,0.45)
    glutSolidCube(5)

    glColor3f(1, 0, 0)
    glLoadIdentity()
    glTranslate(0 + x, 1.25, 0)
    glScale(0.5, 0.2, 0.45)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(2.5 + x, -2.5 * 0.25, 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glColor3f(0, 0, 0.1)
    glutSolidTorus(0.2, 0.55, 20, 15)

    glLoadIdentity()
    glTranslate(-2.5+x, -2.5 * 0.25, 2.5 * 0.5)
    glRotate(angle,0,0,1)
    glColor3f(0, 0, 0.1)
    glutSolidTorus(0.2, 0.55, 20, 15)

    glLoadIdentity()
    glColor3f(1,1,0)
    glTranslate(2.5+x,0,0.6)
    glutWireSphere(0.3,10,10)

    glLoadIdentity()
    glColor3f(1, 1, 0)
    glTranslate(2.5 + x, 0,- 0.6)
    glutWireSphere(0.3, 10, 10)

    if forward:
        x += 0.025
        angle -= 0.1
        if x > 5:
                forward = False
    else:
        x -= 0.025
        angle += 0.1
        if x < -13:
            forward = True

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700,700)
glutCreateWindow(b"Moving car")
glutDisplayFunc(display)
glutIdleFunc(display)
myInit()
glutMainLoop()
