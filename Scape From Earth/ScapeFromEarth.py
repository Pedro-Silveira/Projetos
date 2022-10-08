from functools import lru_cache
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut
import random
from pygame import mixer
mixer.init()

# VARIÁVEIS DO JOGO
mainMusic = mixer.Sound('sound/main.mp3')
mainWindow = 0
contInimigos = 0
recorde = 0
velocidade = 15
gravidade = 2
somMorte = 0
inimigo = random.randint(0, 1)

# VARIÁVEIS DO CENÁRIO
direita = True
esquerda = False
xArvore = 4.0
rCasa = 0.961
gCasa = 0.961
bCasa = 0.863
xCasa = -2.0
xNuvem1 = 22.0
yNuvem1 = random.randint(0, 8)
xNuvem2 = 12.0
yNuvem2 = random.randint(0, 8)
xFaixa1 = 10.0
xFaixa2 = 7.5
xFaixa3 = 5.0
xFaixa4 = 2.5
xFaixa5 = 0.0
xFaixa6 = -2.5
xFaixa7 = -5.0
xFaixa8 = -7.5
xFaixa9 = -10.0

# VARIÁVEIS DOS INIMIGOS
moverAlien = False
LuzR = 0.133
LuzG = 0.545
LuzB = 0.133
xAlien = 11.5
xNave = 11.5

# VARIÁVEIS DO MAIN CHARACTER
moverMC = False
morte = False
sobe = True
desce = False
animacao = True
yMC = -5.5
rotPD = 0.0
rotPE = 0.0
rotBD = 0.0
rotBE = 15.0
xPupila = -6.25
respiracao = 1.0

def inicializacao():
    glClearColor(0.878, 1.000, 1.000, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def escreverTexto(xPos, yPos, string, tipo):
    glRasterPos2f(xPos,yPos)
    for i in range(len(string)):
        if tipo == "titulo":
             glut.glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(string[i]))
        else:
            glut.glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(string[i]))	

def desenha():
    global xAlien, xNave, xArvore, xCasa, rCasa, gCasa, bCasa, respiracao, xPupila, yMC, contInimigos, rotPE, rotPD, rotBE, rotBD, LuzR, LuzG, LuzB, xFaixa1, xFaixa2, xFaixa3, xFaixa4, xFaixa5, xFaixa6, xFaixa7, xFaixa8, xFaixa9, xNuvem1, yNuvem1, xNuvem2, yNuvem2, recorde, velocidade
    glClear(GL_COLOR_BUFFER_BIT)
    
    #Cenário - Chão
    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(0.0, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-10.0, 0.5)
    glVertex2f(10.0, 0.5)
    glVertex2f(10.0, -0.5)
    glVertex2f(-10.0, -0.5)
    glEnd()
    glPopMatrix()
    #Cenário - Casa
    glColor3f(0.545, 0.271, 0.075)
    glPushMatrix()
    glTranslatef(xCasa, -1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-3.0, 0.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(3.0, 0.0)
    glEnd()
    glPopMatrix()
    glColor3f(rCasa, gCasa, bCasa)
    glPushMatrix()
    glTranslatef(xCasa, -5.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-3.0, 4.0)
    glVertex2f(3.0, 4.0)
    glVertex2f(3.0, -4.0)
    glVertex2f(-3.0, -4.0)
    glEnd()
    glPopMatrix()
    glColor3f(0.545, 0.271, 0.075)
    glPushMatrix()
    glTranslatef(xCasa - 1.5, -6.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.75, 2.5)
    glVertex2f(0.75, 2.5)
    glVertex2f(0.75, -2.5)
    glVertex2f(-0.75, -2.5)
    glEnd()
    glPopMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(xCasa - 1.10, -6.5, 0.0)
    glutSolidSphere(0.15, 50, 50)
    glPopMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(xCasa + 1.15, -5.75, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-1.0, 1.75)
    glVertex2f(1.0, 1.75)
    glVertex2f(1.0, -1.75)
    glVertex2f(-1.0, -1.75)
    glEnd()
    glPopMatrix()
    glColor3f(0.545, 0.271, 0.075)
    glPushMatrix()
    glTranslatef(xCasa + 1.15, -5.75, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.10, 1.75)
    glVertex2f(0.10, 1.75)
    glVertex2f(0.10, -1.75)
    glVertex2f(-0.10, -1.75)
    glEnd()
    glPopMatrix()
    glColor3f(0.545, 0.271, 0.075)
    glPushMatrix()
    glTranslatef(xCasa + 1.15, -5.75, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-1.0, 0.20)
    glVertex2f(1.0, 0.20)
    glVertex2f(1.0, -0.20)
    glVertex2f(-1.0, -0.20)
    glEnd()
    glPopMatrix()
    #Cenário - Árvore
    glColor3f(0.545, 0.271, 0.075)
    glPushMatrix()
    glTranslatef(xArvore, -6.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, 3.0)
    glVertex2f(0.5, 3.0)
    glVertex2f(0.5, -3.0)
    glVertex2f(-0.5, -3.0)
    glEnd()
    glPopMatrix()
    glColor3f(0.133, 0.545, 0.133)
    glPushMatrix()
    glTranslatef(xArvore - 1, -3.0, 0.0)
    glutSolidSphere(0.75, 50, 50)
    glPopMatrix()
    glColor3f(0.133, 0.545, 0.133)
    glPushMatrix()
    glTranslatef(xArvore, -3.0, 0.0)
    glutSolidSphere(1.0, 50, 50)
    glPopMatrix()
    glColor3f(0.133, 0.545, 0.133)
    glPushMatrix()
    glTranslatef(xArvore + 1, -3.0, 0.0)
    glutSolidSphere(0.75, 50, 50)
    glPopMatrix()
    glColor3f(0.133, 0.545, 0.133)
    glPushMatrix()
    glTranslatef(xArvore + 0.5, -1.75, 0.0)
    glutSolidSphere(0.75, 50, 50)
    glPopMatrix()
    glColor3f(0.133, 0.545, 0.133)
    glPushMatrix()
    glTranslatef(xArvore - 0.5, -1.75, 0.0)
    glutSolidSphere(0.75, 50, 50)
    glPopMatrix()
    #Cenário - Nuvem 01
    glColor3f(0.863, 0.863, 0.863)
    glPushMatrix()
    glTranslatef(xNuvem1 - 1, yNuvem1, 0.0)
    glutSolidSphere(0.5, 50, 50)
    glPopMatrix()
    glColor3f(0.863, 0.863, 0.863)
    glPushMatrix()
    glTranslatef(xNuvem1, yNuvem1, 0.0)
    glutSolidSphere(0.75, 50, 50)
    glPopMatrix()
    glColor3f(0.863, 0.863, 0.863)
    glPushMatrix()
    glTranslatef(xNuvem1 + 1, yNuvem1, 0.0)
    glutSolidSphere(0.5, 50, 50)
    glPopMatrix()
    #Cenário - Nuvem 01
    glColor3f(0.863, 0.863, 0.863)
    glPushMatrix()
    glTranslatef(xNuvem2 - 1, yNuvem2, 0.0)
    glutSolidSphere(0.5, 50, 50)
    glPopMatrix()
    glColor3f(0.863, 0.863, 0.863)
    glPushMatrix()
    glTranslatef(xNuvem2, yNuvem2, 0.0)
    glutSolidSphere(0.75, 50, 50)
    glPopMatrix()
    glColor3f(0.863, 0.863, 0.863)
    glPushMatrix()
    glTranslatef(xNuvem2 + 1, yNuvem2, 0.0)
    glutSolidSphere(0.5, 50, 50)
    glPopMatrix()
    #Cenário - Faixa
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa1, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa2, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa3, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa4, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa5, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa6, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa7, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa8, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(xFaixa9, -9.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, 0.075)
    glVertex2f(0.2, 0.075)
    glVertex2f(0.2, -0.075)
    glVertex2f(-0.2, -0.075)
    glEnd()
    glPopMatrix()

    #MC - Cabelo
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(-7.15, yMC + 3.25, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(1.2, -0.25)
    glVertex2f(1.2, 0.25)
    glVertex2f(1.0, -0.25)
    glVertex2f(1.0, 0.25)
    glVertex2f(0.8, -0.25)
    glVertex2f(0.8, 0.25)
    glVertex2f(0.6, -0.25)
    glVertex2f(0.6, 0.25)
    glVertex2f(0.4, -0.25)
    glVertex2f(0.4, 0.25)
    glVertex2f(0.2, -0.25)
    glVertex2f(0.2, 0.25)
    glEnd()
    glPopMatrix()
    #MC - Cabeça
    glColor3f(1.000, 0.855, 0.725)
    glPushMatrix()
    glTranslatef(-6.5, yMC + 2.5, 0.0)
    glutSolidSphere(0.75, 50, 50)
    glPopMatrix()
    #MC - Olho
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(-6.25, yMC + 2.75, 0.0)
    glutSolidSphere(0.20, 50, 50)
    glPopMatrix()
    #MC - Pupila
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(xPupila, yMC + 2.75, 0.0)
    glutSolidSphere(0.10, 50, 50)
    glPopMatrix()
    #MC - Boca
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(-6.15, yMC + 2.25, 0.0)
    glRotatef(-25, 0.0, 0.0, 0.5)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 0.05)
    glVertex2f(0.15, 0.05)
    glVertex2f(0.15, -0.05)
    glVertex2f(-0.15, -0.05)
    glEnd()
    glPopMatrix()
    #MC - Pescoço
    glColor3f(1.000, 0.855, 0.725)
    glPushMatrix()
    glTranslatef(-6.5, yMC + 1.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 0.3)
    glVertex2f(0.15, 0.3)
    glVertex2f(0.15, -0.3)
    glVertex2f(-0.15, -0.3)
    glEnd()
    glPopMatrix()
    #MC - Braço Esquerdo
    glColor3f(1.000, 0.855, 0.725)
    glPushMatrix()
    glTranslatef(-6.20, yMC + 0.25, 0.0)
    glRotatef(rotBE, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 1.0)
    glVertex2f(0.15, 1.0)
    glVertex2f(0.15, -1.0)
    glVertex2f(-0.15, -1.0)
    glEnd()
    glPopMatrix()
    #MC - Perna Esquerda
    glColor3f(0.098, 0.098, 0.439)
    glPushMatrix()
    glTranslatef(-6.5, yMC - 1.5, 0.0)
    glRotatef(rotPE, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 2.0)
    glVertex2f(0.15, 2.0)
    glVertex2f(0.15, -2.0)
    glVertex2f(-0.15, -2.0)
    glEnd()
    glPopMatrix()
    #MC - Perna Direita
    glColor3f(0.282, 0.239, 0.545)
    glPushMatrix()
    glTranslatef(-6.5, yMC - 1.5, 0.0)
    glRotatef(rotPD, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 2.0)
    glVertex2f(0.15, 2.0)
    glVertex2f(0.15, -2.0)
    glVertex2f(-0.15, -2.0)
    glEnd()
    glPopMatrix()
    #MC - Tronco
    glColor3f(0.502, 0.000, 0.000)
    glPushMatrix()
    glTranslatef(-6.5, yMC, 0.0)
    glScalef(respiracao, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, 1.5)
    glVertex2f(0.5, 1.5)
    glVertex2f(0.5, -1.5)
    glVertex2f(-0.5, -1.5)
    glEnd()
    glPopMatrix()
    #MC - Braço Direito
    glColor3f(1.000, 0.855, 0.725)
    glPushMatrix()
    glTranslatef(-6.5, yMC + 0.25, 0.0)
    glRotatef(rotBD, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 1.0)
    glVertex2f(0.15, 1.0)
    glVertex2f(0.15, -1.0)
    glVertex2f(-0.15, -1.0)
    glEnd()
    glPopMatrix()

    #Alien - Cabeça
    glColor3f(0.663, 0.663, 0.663)
    glPushMatrix()
    glTranslatef(xAlien, -3.0, 0.0)
    glutSolidSphere(0.75, 50, 50)
    glPopMatrix()
    #Alien - Olho
    glColor3f(0.412, 0.412, 0.412)
    glPushMatrix()
    glTranslatef(xAlien - 0.25, -2.75, 0.0)
    glutSolidSphere(0.20, 50, 50)
    glPopMatrix()
    #Alien - Pupila
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(xAlien - 0.25, -2.75, 0.0)
    glutSolidSphere(0.10, 50, 50)
    glPopMatrix()
    #Alien - Boca
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(xAlien - 0.35, -3.25, 0.0)
    glRotatef(25, 0.0, 0.0, 0.5)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 0.05)
    glVertex2f(0.15, 0.05)
    glVertex2f(0.15, -0.05)
    glVertex2f(-0.15, -0.05)
    glEnd()
    glPopMatrix()
    #Alien - Pescoço
    glColor3f(0.502, 0.502, 0.502)
    glPushMatrix()
    glTranslatef(xAlien, -4, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 0.3)
    glVertex2f(0.15, 0.3)
    glVertex2f(0.15, -0.3)
    glVertex2f(-0.15, -0.3)
    glEnd()
    glPopMatrix()
    #Alien - Braço Esquerdo
    glColor3f(0.412, 0.412, 0.412)
    glPushMatrix()
    glTranslatef(xAlien - 0.5 , -5.0, 0.0)
    glRotatef(rotBE, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.75, 0.25)
    glVertex2f(0.75, 0.25)
    glVertex2f(0.75, -0.25)
    glVertex2f(-0.75, -0.25)
    glEnd()
    glPopMatrix()
    #Alien - Perna Esquerda
    glColor3f(0.412, 0.412, 0.412)
    glPushMatrix()
    glTranslatef(xAlien, -7.0, 0.0)
    glRotatef(rotPE, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 2.0)
    glVertex2f(0.15, 2.0)
    glVertex2f(0.15, -2.0)
    glVertex2f(-0.15, -2.0)
    glEnd()
    glPopMatrix()
    #Alien - Perna Direita
    glColor3f(0.502, 0.502, 0.502)
    glPushMatrix()
    glTranslatef(xAlien, -7.0, 0.0)
    glRotatef(rotPD, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.15, 2.0)
    glVertex2f(0.15, 2.0)
    glVertex2f(0.15, -2.0)
    glVertex2f(-0.15, -2.0)
    glEnd()
    glPopMatrix()
    #Alien - Tronco
    glColor3f(0.663, 0.663, 0.663)
    glPushMatrix()
    glTranslatef(xAlien, -5.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, 1.5)
    glVertex2f(0.5, 1.5)
    glVertex2f(0.5, -1.5)
    glVertex2f(-0.5, -1.5)
    glEnd()
    glPopMatrix()
    #Alien - Braço Direito
    glColor3f(0.502, 0.502, 0.502)
    glPushMatrix()
    glTranslatef(xAlien - 0.5 , -5.0, 0.0)
    glRotatef(rotBD, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.75, 0.25)
    glVertex2f(0.75, 0.25)
    glVertex2f(0.75, -0.25)
    glVertex2f(-0.75, -0.25)
    glEnd()
    glPopMatrix()

    #Nave - Cabine
    glColor3f(0.502, 0.502, 0.502)
    glPushMatrix()
    glTranslatef(xNave, 3.0, 0.0)
    glutSolidSphere(1.0, 50, 50)
    glPopMatrix()
    #Nave - Lataria
    glColor3f(0.412, 0.412, 0.412)
    glPushMatrix()
    glTranslatef(xNave, 2.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-1.5, 0.5)
    glVertex2f(1.5, 0.5)
    glVertex2f(1.5, -0.5)
    glVertex2f(-1.5, -0.5)
    glEnd()
    glPopMatrix()
    #Nave - Luz 01
    glColor3f(LuzR, LuzG, LuzB)
    glPushMatrix()
    glTranslatef(xNave - 1.0, 2.5, 0.0)
    glutSolidSphere(0.15, 50, 50)
    glPopMatrix()
    #Nave - Luz 02
    glColor3f(LuzR, LuzG, LuzB)
    glPushMatrix()
    glTranslatef(xNave - 0.5, 2.5, 0.0)
    glutSolidSphere(0.15, 50, 50)
    glPopMatrix()
    #Nave - Luz 03
    glColor3f(LuzR, LuzG, LuzB)
    glPushMatrix()
    glTranslatef(xNave, 2.5, 0.0)
    glutSolidSphere(0.15, 50, 50)
    glPopMatrix()
    #Nave - Luz 04
    glColor3f(LuzR, LuzG, LuzB)
    glPushMatrix()
    glTranslatef(xNave + 0.5, 2.5, 0.0)
    glutSolidSphere(0.15, 50, 50)
    glPopMatrix()
    #Nave - Luz 05
    glColor3f(LuzR, LuzG, LuzB)
    glPushMatrix()
    glTranslatef(xNave + 1.0, 2.5, 0.0)
    glutSolidSphere(0.15, 50, 50)
    glPopMatrix()

    if moverAlien == False and morte == False:
        glColor3f(0.0, 0.0, 0.0)
        escreverTexto(-2.25, 6.0, "SCAPE FROM EARTH", "titulo")
        escreverTexto(-3.25, 3.5, "PRESS \"SPACEBAR\" TO START THE GAME!", "normal")
    elif moverAlien == False and morte == True:
        glColor3f(0.5, 0.0, 0.0)
        escreverTexto(-2.0, 2.5, "YOU'VE BEEN ABDUCED!", "normal")
        glColor3f(0.0, 0.0, 0.0)
        escreverTexto(-3.25, 0, "PRESS \"SPACEBAR\" TO RESTART THE GAME!", "normal")
    else:
        glColor3f(0.0, 0.0, 0.0)
        escreverTexto(-9.0, 8.0, "ENEMIES OVERCOME: " + str(contInimigos), "normal")
        escreverTexto(-9.0, 7.0, "YOUR RECORD: " + str(recorde), "normal")

    glutSwapBuffers()

def Teclado(tecla, x, y):
    global moverMC, yMC, mainWindow, somMorte, mainMusic, moverAlien, contInimigos, xAlien, xNave, velocidade, sobe, desce, direita, esquerda, inimigo, morte, gravidade

    if tecla == b'\x1b':
        glutDestroyWindow(mainWindow)
    else:
        if tecla == b' ':
            if yMC == -5.5:
                moverMC = not(moverMC)
                jump = mixer.Sound('sound/jump.mp3')
                jump.play()
            if moverAlien == False and morte != True:
                moverAlien = True
            if moverAlien == False and morte == True:
                mainMusic.play()
                moverAlien = True
                morte = False
                gravidade = 2
                somMorte = 0
                contInimigos = 0
                xAlien = 11.5
                xNave = 11.5
                yMC = -5.5
                velocidade = 15
                moverMC = True
                sobe = True
                desce = False
                direita = True
                esquerda = False
                inimigo = random.randint(0, 1)
    
        glutPostRedisplay()

def animaAlien(ligar):
    global xAlien, xNave, velocidade, moverAlien, inimigo, contInimigos
    
    if ligar:
        if inimigo == 0:
            if xAlien > -15.00:
                xAlien -= 0.1
            else:
                if contInimigos % 2 == 0 and velocidade > 3:
                    velocidade -= 1
                xAlien = 11.5
                contInimigos += 1
                inimigo = random.randint(0, 1)
        else:
            if xNave > -15.00:
                xNave -= 0.1
            else:
                if contInimigos % 2 == 0 and velocidade > 3:
                    velocidade -= 1
                xNave = 11.5
                contInimigos += 1
                inimigo = random.randint(0, 1)

    glutPostRedisplay()
    glutTimerFunc(velocidade, animaAlien, moverAlien)

def animaMC(ligar):
    global gravidade, somMorte, sobe, desce, direita, esquerda, moverMC, moverAlien, yMC, xAlien, xNave, morte, rotPE, rotPD, rotBE, rotBD, recorde, contInimigos, mainMusic

    if (yMC >= 0.5 and yMC <= 4.5) and (xNave >= -8.5 and xNave <= -4.5):
        moverAlien = False
        if contInimigos > recorde:
            recorde = contInimigos
        if somMorte == 0:
            mainMusic.stop()
            death = mixer.Sound('sound/death.mp3')
            death.play()
            somMorte = 1
        morte = True
    elif (yMC >= -8.5 and yMC <= -2.5) and (xAlien >= -7.5 and xAlien <= -5.5):
        moverAlien = False
        if contInimigos > recorde:
            recorde = contInimigos
        if somMorte == 0:
            mainMusic.stop()
            death = mixer.Sound('sound/death.mp3')
            death.play()
            somMorte = 1
        morte = True

    if (ligar or yMC != -5.5) and morte != True:
        if sobe:
            if yMC >= 2.5:
                sobe = False
                desce = True
            else:
                yMC += 0.1

                if yMC >= 1.0:
                    gravidade += 1
        if desce:
            if yMC <= -5.5:
                sobe = True
                desce = False
                moverMC = False
            else:
                yMC -= 0.1

                if yMC >= 0.9:
                    gravidade -= 1

    glutPostRedisplay()
    glutTimerFunc(gravidade, animaMC, moverMC)

def animacaoGlobal(ligar):
    global xNuvem1, yNuvem1, xNuvem2, yNuvem2, velocidade, respiracao, xPupila, animacao

    if animacao:
        if xPupila < -6.18:
            xPupila += 0.001
            respiracao += 0.001
        else:
            animacao = False
    else:
        if xPupila != -6.25:
            xPupila -= 0.001
            respiracao -= 0.001
        else:
            animacao = True

    if xNuvem1 > -13.00:
        xNuvem1 -= 0.1
    else:
        xNuvem1 = 15.0
        yNuvem1 = random.randint(0, 8)

    if xNuvem2 > -13.00:
        xNuvem2 -= 0.1
    else:
        xNuvem2 = 15.0
        yNuvem2 = random.randint(0, 8)

    glutPostRedisplay()
    glutTimerFunc(velocidade + 10, animacaoGlobal, ligar)

def animacaoMovimento(ligar):
    global direita, esquerda, moverAlien, morte, rotPE, rotPD, rotBE, rotBD, velocidade, LuzR, LuzG, LuzB, xArvore, xFaixa1, xFaixa2, xFaixa3, xFaixa4, xFaixa5, xFaixa6, xFaixa7, xFaixa8, xFaixa9, xCasa, rCasa, gCasa, bCasa

    if (ligar or yMC != -5.5) and morte != True:
        if xFaixa1 <= -10.6:
            xFaixa1 = 10.6
        else:
            xFaixa1 -= 0.1
        if xFaixa2 <= -10.6:
            xFaixa2 = 10.6
        else:
            xFaixa2 -= 0.1
        if xFaixa3 <= -10.6:
            xFaixa3 = 10.6
        else:
            xFaixa3 -= 0.1
        if xFaixa4 <= -10.6:
            xFaixa4 = 10.6
        else:
            xFaixa4 -= 0.1
        if xFaixa5 <= -10.6:
            xFaixa5 = 10.6
        else:
            xFaixa5 -= 0.1
        if xFaixa6 <= -10.6:
            xFaixa6 = 10.6
        else:
            xFaixa6 -= 0.1
        if xFaixa7 <= -10.6:
            xFaixa7 = 10.6
        else:
            xFaixa7 -= 0.1
        if xFaixa8 <= -10.6:
            xFaixa8 = 10.6
        else:
            xFaixa8 -= 0.1
        if xFaixa9 <= -10.6:
            xFaixa9 = 10.6
        else:
            xFaixa9 -= 0.1

        if xArvore <= -50.0:
            xArvore = 13.0
        else:
            xArvore -= 0.1

        if xCasa <= -100.0:
            rCasa = random.random()
            gCasa = random.random()
            bCasa = random.random()
            xCasa = 20.0
        else:
            xCasa -= 0.1

        if direita:
            LuzR += 0.005
            LuzG += 0.005
            LuzB += 0.005

            if rotBD >= 20:
                direita = False
                esquerda = True
            else:
                rotBD += 1
                rotPE += 0.5
                rotBE -= 1
                rotPD -= 0.5
        if esquerda:
            LuzR -= 0.005
            LuzG -= 0.005
            LuzB -= 0.005

            if rotBD <= -20:
                direita = True
                esquerda = False
            else:
                rotBD -= 1
                rotPE -= 0.5
                rotBE += 1
                rotPD += 0.5

    glutPostRedisplay()
    glutTimerFunc(velocidade, animacaoMovimento, moverAlien)

def main():
    global mainWindow, mainMusic

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    mainWindow = glutCreateWindow ("Escape From Earth")
    glutFullScreen()
    mainMusic.play(-1)
    animacaoGlobal(True)
    animaMC(moverMC)
    animacaoMovimento(moverAlien)
    animaAlien(moverAlien)
    glutDisplayFunc(desenha)
    glutSpecialFunc(Teclado)
    glutKeyboardFunc(Teclado)
    inicializacao()
    glutMainLoop()
    
main()