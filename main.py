import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cube
import pyramid
import prism

def draw_object(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        draw_object(cube.vertices, cube.edges)
        draw_object(pyramid.vertices, pyramid.edges)
        draw_object(prism.vertices, prism.edges)
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
