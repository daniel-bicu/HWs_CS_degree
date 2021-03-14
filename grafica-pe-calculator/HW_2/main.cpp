#include <GL/glut.h>

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <cfloat>

// dimensiunea ferestrei in pixeli
#define dim 300

unsigned char prevKey;

// concoida lui Nicomede (concoida dreptei)
// $x = a + b \cdot cos(t), y = a \cdot tg(t) + b \cdot sin(t)$. sau
// $x = a - b \cdot cos(t), y = a \cdot tg(t) - b \cdot sin(t)$. unde
// $t \in (-\pi / 2, \pi / 2)$
void DisplayQ() {
    double xmax, ymax, xmin, ymin;
    double a = 1, b = 2;
    double pi = 4 * atan(1);
    double ratia = 0.05;

    // calculul valorilor maxime/minime ptr. x si y
    // aceste valori vor fi folosite ulterior la scalare
    xmax = a - b - 1;
    xmin = a + b + 1;
    ymax = ymin = 0;
    for (double t = - pi/2 + ratia; t < pi / 2; t += ratia) {
        double x1, y1, x2, y2;
        x1 = a + b * cos(t);
        xmax = (xmax < x1) ? x1 : xmax;
        xmin = (xmin > x1) ? x1 : xmin;

        x2 = a - b * cos(t);
        xmax = (xmax < x2) ? x2 : xmax;
        xmin = (xmin > x2) ? x2 : xmin;

        y1 = a * tan(t) + b * sin(t);
        ymax = (ymax < y1) ? y1 : ymax;
        ymin = (ymin > y1) ? y1 : ymin;

        y2 = a * tan(t) - b * sin(t);
        ymax = (ymax < y2) ? y2 : ymax;
        ymin = (ymin > y2) ? y2 : ymin;
    }

    xmax = (fabs(xmax) > fabs(xmin)) ? fabs(xmax) : fabs(xmin);
    ymax = (fabs(ymax) > fabs(ymin)) ? fabs(ymax) : fabs(ymin);

    // afisarea punctelor propriu-zise precedata de scalare
    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double t = - pi/2 + ratia; t < pi / 2; t += ratia) {
        double x1, y1, x2, y2;
        x1 = (a + b * cos(t)) / xmax;
        x2 = (a - b * cos(t)) / xmax;
        y1 = (a * tan(t) + b * sin(t)) / ymax;
        y2 = (a * tan(t) - b * sin(t)) / ymax;

        glVertex2f(x1,y1);
    }
    glEnd();

    glBegin(GL_LINE_STRIP);
    for (double t = - pi/2 + ratia; t < pi / 2; t += ratia) {
        double x1, y1, x2, y2;
        x1 = (a + b * cos(t)) / xmax;
        x2 = (a - b * cos(t)) / xmax;
        y1 = (a * tan(t) + b * sin(t)) / ymax;
        y2 = (a * tan(t) - b * sin(t)) / ymax;

        glVertex2f(x2,y2);
    }
    glEnd();
}

// graficul functiei
// $f(x) = \bar sin(x) \bar \cdot e^{-sin(x)}, x \in \langle 0, 8 \cdot \pi \rangle$,
void DisplayW() {
    double pi = 4 * atan(1);
    double xmax = 8 * pi;
    double ymax = exp(1.1);
    double ratia = 0.05;

    // afisarea punctelor propriu-zise precedata de scalare
    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double x = 0; x < xmax; x += ratia) {
        double x1, y1;
        x1 = x / xmax;
        y1 = (fabs(sin(x)) * exp(-sin(x))) / ymax;

        glVertex2f(x1,y1);
    }
    glEnd();
}

void Display1() {
    /*
      f(x) =        1, x = 0
             d(x) / x, 0 < x <= 100
      d(x) = dist(x, y), y e Z
    */
    double xmax = 100;
    double ymax = 1.5;
    double ratia = 0.1;

    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);

    glVertex2f(0, 1);
    for (double x = 1; x <= 100; x += ratia) {
        int x_integer = round(x);
        double dist = fabs(x - x_integer);
        double y = dist / x;
        glVertex2f(x / (xmax * 0.3), y / (ymax * 0.65));
    }
    glEnd();
}

void Display2() {
    double xmax, ymax, xmin, ymin;
    double a = 0.3, b = 0.2;
    double pi = 4 * atan(1.0);
    double ratia = 0.01;

    xmax = -FLT_MAX;
    xmin = FLT_MAX;
    ymax = -FLT_MAX;
    ymin = FLT_MAX;

    for (double t = -pi + ratia; t < pi; t += ratia) {
        double x, y;

        x = 2 * (a * cos(t) + b) * cos(t);
        xmax = (xmax < x) ? x : xmax;
        xmin = (xmin > x) ? x : xmin;

        y = 2 * (a * cos(t) + b) * sin(t);
        ymax = (ymax < y) ? y : ymax;
        ymin = (ymin > y) ? y : ymin;
    }

    xmax = (fabs(xmax) > fabs(xmin)) ? fabs(xmax) : fabs(xmin);
    ymax = (fabs(ymax) > fabs(ymin)) ? fabs(ymax) : fabs(ymin);

    glColor3f(1, 0.1, 0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double t = -pi + ratia; t < pi; t += ratia) {
        double x, y;

        x = (2 * (a * cos(t) + b) * cos(t)) / (xmax * 1.05);
        y = (2 * (a * cos(t) + b) * sin(t)) / (ymax * 1.7);

        glVertex2f(x, y);
    }
    glEnd();
}

void Display3() {}

void Display4() {
    double xmax, ymax, xmin, ymin;
    double a = 0.1, b = 0.2;
    double pi = 4 * atan(1);
    double ratia = 0.0005;

    xmin = FLT_MAX;
    xmax = -FLT_MAX;
    ymin = FLT_MAX;
    ymax = -FLT_MAX;

    for (double t = -3 * pi + ratia; t < 3 * pi; t += ratia) {
        double x, y;
        x = a * t - b * sin(t);
        xmin = x < xmin ? x : xmin;
        xmax = x > xmax ? x : xmax;

        y = a - b * cos(t);
        ymin = y < ymin ? y : ymin;
        ymax = y > ymax ? y : ymax;
    }

    xmax = (fabs(xmax) > fabs(xmin)) ? fabs(xmax) : fabs(xmin);
    ymax = (fabs(ymax) > fabs(ymin)) ? fabs(ymax) : fabs(ymin);

    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double t = -3 * pi + ratia; t < 3 * pi; t += ratia) {
        double x, y;
        x = a * t - b * sin(t);
        y = a - b * cos(t);

        x = x / xmax; y = y / (ymax * 3);
        glVertex2f(x, y);
    }
    glEnd();
}

void Display5() {
    double xmax, ymax, xmin, ymin;
    double R = 0.1, r = 0.3;
    double pi = 4 * atan(1);
    double ratia = 0.05;

    xmin = FLT_MAX;
    xmax = -FLT_MAX;
    ymin = FLT_MAX;
    ymax = -FLT_MAX;

    for (double t = 0; t <= 2 * pi; t += ratia) {
        double x, y;
        double arg1 = (r / R) * t;
        double arg2 = t + arg1;

        x = (R + r) * cos(arg1) - r * cos(arg2);
        xmin = x < xmin ? x : xmin;
        xmax = x > xmax ? x : xmax;

        y = (R + r) * sin(arg1) - r * sin(arg2);
        ymin = y < ymin ? y : ymin;
        ymax = y > ymax ? y : ymax;
    }

    xmax = (fabs(xmax) > fabs(xmin)) ? fabs(xmax) : fabs(xmin);
    ymax = (fabs(ymax) > fabs(ymin)) ? fabs(ymax) : fabs(ymin);

    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double t = 0; t <= 2 * pi; t += ratia) {
        double x, y;
        double arg1 = (r / R) * t;
        double arg2 = t + arg1;

        x = (R + r) * cos(arg1) - r * cos(arg2);
        y = (R + r) * sin(arg1) - r * sin(arg2);

        x = x / (xmax * 1.3), y = y / (ymax * 1.3);
        glVertex2f(x, y);
    }
    glEnd();
}

void Display6() {
    double xmax, ymax, xmin, ymin;
    double R = 0.1, r = 0.3;
    double pi = 4 * atan(1);
    double ratia = 0.05;

    xmin = FLT_MAX;
    xmax = -FLT_MAX;
    ymin = FLT_MAX;
    ymax = -FLT_MAX;

    for (double t = 0; t <= 2 * pi; t += ratia) {
        double x, y;
        double arg1 = (r / R) * t;
        double arg2 = t - arg1;

        x = (R - r) * cos(arg1) - r * cos(arg2);
        xmin = x < xmin ? x : xmin;
        xmax = x > xmax ? x : xmax;

        y = (R - r) * sin(arg1) - r * sin(arg2);
        ymin = y < ymin ? y : ymin;
        ymax = y > ymax ? y : ymax;
    }

    xmax = (fabs(xmax) > fabs(xmin)) ? fabs(xmax) : fabs(xmin);
    ymax = (fabs(ymax) > fabs(ymin)) ? fabs(ymax) : fabs(ymin);

    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double t = 0; t <= 2 * pi; t += ratia) {
        double x, y;
        double arg1 = (r / R) * t;
        double arg2 = t - arg1;

        x = (R - r) * cos(arg1) - r * cos(arg2);
        y = (R - r) * sin(arg1) - r * sin(arg2);

        x = x / (xmax * 1.3), y = y / (ymax * 1.3);
        glVertex2f(x, y);
    }
    glEnd();
}

void Display7() {
    double xmax, ymax, xmin, ymin;
    double a = 0.4;
    double pi = 4 * atan(1);
    double ratia = 0.00001;

    xmin = FLT_MAX;
    xmax = -FLT_MAX;
    ymin = FLT_MAX;
    ymax = -FLT_MAX;

    for (double t = -1 * (pi / 4) + ratia; t < pi / 4; t += ratia) {
        double x1, y1, x2, y2;
        double r1 = a * sqrt(2 * cos(2 * t));
        double r2 = -1 * a * sqrt(2 * cos(2 * t));

        x1 = r1 * cos(t);
        xmin = x1 < xmin ? x1 : xmin;
        xmax = x1 > xmax ? x1 : xmax;

        y1 = r1 * sin(t);
        ymin = y1 < ymin ? y1 : ymin;
        ymax = y1 > ymax ? y1 : ymax;

        x2 = r2 * cos(t);
        xmin = x2 < xmin ? x2 : xmin;
        xmax = x2 > xmax ? x2 : xmax;

        y2 = r2 * sin(t);
        ymin = y2 < ymin ? y2 : ymin;
        ymax = y2 > ymax ? y2 : ymax;
    }

    xmax = (fabs(xmax) > fabs(xmin)) ? fabs(xmax) : fabs(xmin);
    ymax = (fabs(ymax) > fabs(ymin)) ? fabs(ymax) : fabs(ymin);

    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double t = -1 * (pi / 4) + ratia; t < (pi / 4) - (ratia * 100); t += ratia) {
        double x1, y1, x2, y2;
        double r1 = a * sqrt(2 * cos(2 * t));
        double r2 = -1 * a * sqrt(2 * cos(2 * t));

        x1 = r1 * cos(t);
        y1 = r1 * sin(t);
        x2 = r2 * cos(t);
        y2 = r2 * sin(t);

        x1 = x1 / (xmax * 1.3), y1 = y1 / (ymax * 3.1);
        glVertex2f(x1, y1);
    }
    glEnd();

    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double t = -1 * (pi / 4) + ratia; t < (pi / 4) - (ratia * 100); t += ratia) {
        double x1, y1, x2, y2;
        double r1 = a * sqrt(2 * cos(2 * t));
        double r2 = -1 * a * sqrt(2 * cos(2 * t));

        x1 = r1 * cos(t);
        y1 = r1 * sin(t);
        x2 = r2 * cos(t);
        y2 = r2 * sin(t);

        x2 = x2 / (xmax * 1.3), y2 = y2 / (ymax * 3.1);
        glVertex2f(x2, y2);
    }
    glEnd();
}

void Display8() {
    double xmax, ymax, xmin, ymin;
    double a = 0.02;
    double pi = 4 * atan(1);
    double ratia = 0.05;

    xmin = FLT_MAX;
    xmax = -FLT_MAX;
    ymin = FLT_MAX;
    ymax = -FLT_MAX;

    for (double t = ratia; t < pi; t += ratia) {
        double x, y;
        double r = a * exp(1 + t);

        x = r * cos(t);
        xmin = x < xmin ? x : xmin;
        xmax = x > xmax ? x : xmax;

        y = r * sin(t);
        ymin = y < ymin ? y : ymin;
        ymax = y > ymax ? y : ymax;
    }

    xmax = (fabs(xmax) > fabs(xmin)) ? fabs(xmax) : fabs(xmin);
    ymax = (fabs(ymax) > fabs(ymin)) ? fabs(ymax) : fabs(ymin);

    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINE_STRIP);
    for (double t = -3 * pi + ratia; t < 3 * pi; t += ratia) {
        double x, y;
        double r = a * exp(1 + t);

        x = r * cos(t);
        y = r * sin(t);

        x = x / xmax, y = y / (ymax * 2.8);
        glVertex2f(x, y);
    }
    glEnd();
}

void Init(void) {

    glClearColor(1.0,1.0,1.0,1.0);

    glLineWidth(1);

//   glPointSize(4);

    glPolygonMode(GL_FRONT, GL_LINE);
}

void Display(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    switch(prevKey) {
        case 'q':
            DisplayQ();
            break;
        case 'w':
            DisplayW();
            break;
        case '1':
            Display1();
            break;
        case '2':
            Display2();
            break;
        case '3':
            Display3();
            break;
        case '4':
            Display4();
            break;
        case '5':
            Display5();
            break;
        case '6':
            Display6();
            break;
        case '7':
            Display7();
            break;
        case '8':
            Display8();
            break;
        default:
            break;
    }

    glFlush();
}

void Reshape(int w, int h) {
    glViewport(0, 0, (GLsizei) w, (GLsizei) h);
}

void KeyboardFunc(unsigned char key, int x, int y) {
    prevKey = key;
    if (key == 27) // escape
        exit(0);
    glutPostRedisplay();
}

void MouseFunc(int button, int state, int x, int y) {
}

int main(int argc, char** argv) {

    glutInit(&argc, argv);

    glutInitWindowSize(dim, dim);

    glutInitWindowPosition(100, 100);

    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);

    glutCreateWindow (argv[0]);

    Init();

    glutReshapeFunc(Reshape);

    glutKeyboardFunc(KeyboardFunc);

    glutMouseFunc(MouseFunc);

    glutDisplayFunc(Display);

    glutMainLoop();

    return 0;
}