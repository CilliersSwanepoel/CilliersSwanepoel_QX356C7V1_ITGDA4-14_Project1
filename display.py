import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cube
import pyramid
import prism

class Display:
    def __init__(self):
        #Initialise 3d objects for use
        self.objects = [
            {'data': (cube.vertices, cube.edges), 'position': [0, 0, 0], 'rotation': [0, 0, 0], 'scale': [1, 1, 1]},
            {'data': (pyramid.vertices, pyramid.edges), 'position': [0, 0, 0], 'rotation': [0, 0, 0], 'scale': [1, 1, 1]},
            {'data': (prism.vertices, prism.edges), 'position': [0, 0, 0], 'rotation': [0, 0, 0], 'scale': [1, 1, 1]}
        ]
        self.current_object = 0 #Track current displayed object

    def draw_object(self, vertices, edges, position, rotation, scale):
        # Apply transformations and draw object based on vertices and edges
        glPushMatrix()
        glTranslate(*position)
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)
        glRotatef(rotation[2], 0, 0, 1)
        glScalef(scale[0], scale[1], scale[2])
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
        glPopMatrix()

    def handle_key_events(self, event):

        #key events handled here 
        
        obj = self.objects[self.current_object]
        if event.key == pygame.K_KP1:
            obj['position'][0] += 1.0
        elif event.key == pygame.K_KP2:
            obj['position'][0] -= 1.0
        elif event.key == pygame.K_KP3:
            obj['position'][1] += 1.0
        elif event.key == pygame.K_KP4:
            obj['position'][1] -= 1.0
        elif event.key == pygame.K_KP5:
            obj['position'][2] += 1.0
        elif event.key == pygame.K_KP6:
            obj['position'][2] -= 1.0

        elif event.key == pygame.K_q:
            obj['rotation'][0] += 10
        elif event.key == pygame.K_w:
            obj['rotation'][1] += 10
        elif event.key == pygame.K_e:
            obj['rotation'][2] += 10
        elif event.key == pygame.K_a:
            obj['rotation'][0] -= 10
        elif event.key == pygame.K_s:
            obj['rotation'][1] -= 10
        elif event.key == pygame.K_d:
            obj['rotation'][2] -= 10

        elif event.key in [pygame.K_KP_PLUS, pygame.K_EQUALS]:
            obj['scale'] = [s + 0.1 for s in obj['scale']]
        elif event.key in [pygame.K_KP_MINUS, pygame.K_MINUS]:
            obj['scale'] = [max(s - 0.1, 0.1) for s in obj['scale']]

        elif event.key == pygame.K_SPACE:
            self.current_object = (self.current_object + 1) % len(self.objects)
            print(f"Switched to object {self.current_object}")

    def run(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        while True:
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    self.handle_key_events(event)
            obj = self.objects[self.current_object]
            self.draw_object(*obj['data'], obj['position'], obj['rotation'], obj['scale'])
            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    Display().run()
