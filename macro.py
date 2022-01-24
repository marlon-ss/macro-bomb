import pyautogui
import time
import logging
from datetime import datetime

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)

def getPos():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def isWork():
    resp = False
    if pyautogui.locateOnScreen('./buttons/workAll.png', confidence=.7) != None:
        resp = True
    
    return resp

def isRest():
    resp = False
    if pyautogui.locateOnScreen('./buttons/restAll.png', confidence=.7) != None:
        resp = True
    
    return resp

def recarregar(trabalho=True, minRestantes=81):
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('f5')
    pyautogui.keyUp('f5')
    pyautogui.keyUp('ctrl')
    time.sleep(8)
    logging.debug('aba recarregada; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    login(trabalho, minRestantes)

def login(trabalho=True, minRestantes=81):
    logging.debug('entrou no login; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    locateConnect = False
    locateSign = False
    locateHunt = False
    cont = 0

    while locateConnect==False:
        time.sleep(1)
        cont+=1
        if pyautogui.locateOnScreen('./buttons/connect.png', confidence=.5) != None:
            cont = 0
            locateConnect = True
            logging.debug('achou o connect; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            pyautogui.moveTo('./buttons/connect.png', None, 0.5)
            pyautogui.click()
        
        elif cont > 90:
            logging.error('nao achou o connect em 1 min e meio e vai recarregar')
            recarregar()

    while locateSign==False:
        time.sleep(1)
        cont+=1
        if pyautogui.locateOnScreen('./buttons/signMeta.png', confidence=.9) != None:
            cont = 0
            locateSign = True
            logging.debug('achou o sign da metamask; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            pyautogui.moveTo('./buttons/signMeta.png', None, 0.5)
            pyautogui.click()
        
        elif cont > 60:
            logging.error('nao achou o sign da meta em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar()
    
    while locateHunt==False:
        time.sleep(1)
        cont+=1
        if pyautogui.locateOnScreen('./buttons/hunt.png', confidence=.9) != None:
            cont = 0
            locateHunt = True
            logging.debug('finalizou o login; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))  
            if trabalho:
                putWork()
            elif trabalho == False and minRestantes == 81:
                putRest()
            else:
                timeRest(True, minRestantes)
        
        elif cont > 60:
            logging.error('nao carregou a tela inicial em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar()
    

def putWork():
    locateHeroes = False
    locateHunt = False
    cont = 0

    logging.info('colocando pra trabalhar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    while locateHeroes==False:
        time.sleep(1)
        cont += 1
        if pyautogui.locateOnScreen('./buttons/heroes.png', confidence=.8) != None:
            locateHeroes = True
            cont = 0
            logging.debug('encontrou o botão herois; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            pyautogui.moveTo('./buttons/heroes.png', None, 0.5)
            pyautogui.click()
        elif cont > 60:
            logging.error('nao encontrou o botao herois em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar(True)

    time.sleep(1)

    if isWork() == False and isRest == False:
        while isWork() == False and isRest == False:
            cont += 1
            time.sleep(2)
            if cont > 60:
                logging.error('não encontrou o botão work All e rest All em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                recarregar()

    elif isWork() == True:
        logging.debug('encontrou o botão work All e colocara para trabalhar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        cont = 0
        time.sleep(1)
        pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/workAll.png', confidence=.7), None, 0.5)
        pyautogui.click()
        rest = False
        while rest == False:
            cont += 1
            if pyautogui.locateOnScreen('./buttons/restAll.png', confidence=.8) != None:
                rest = True  
                cont = 0
            elif cont > 60:
                logging.error('não encontrou o botão rest All em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                recarregar()
            time.sleep(1)
    
    logging.info('colocou todo mundo pra trabalhar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))

    pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/close.png', confidence=.8), None, 0.5)
    pyautogui.click()
    logging.debug('saiu da tela de herois; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))

    while locateHunt==False:
        time.sleep(1)
        cont += 1
        if pyautogui.locateOnScreen('./buttons/hunt.png', confidence=.8) != None:
            locateHunt = True
            cont = 0
            logging.debug('encontrou o botão pra abrir o mapa; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            time.sleep(1)
            pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/hunt.png', confidence=.8), None, 0.5)
            pyautogui.click()
            logging.debug('entrou pro mapa; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            timeWork()
        elif cont > 60:
            logging.error('nao carregou a tela inicial em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar(True)

def putRest():
    locateHeroes = False
    cont = 0

    logging.info('colocando pra descansar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))

    while locateHeroes==False:
        cont += 1
        time.sleep(1)
        if pyautogui.locateOnScreen('./buttons/heroes.png', confidence=.8) != None:
            locateHeroes = True
            cont = 0
            logging.debug('encontrou o botão herois; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/heroes.png', confidence=.8), None, 0.5)
            pyautogui.click()
        elif cont > 60:
            logging.error('nao encontrou o botão herois em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar(False)

    time.sleep(1)

    if isRest() == False and isWork() == True:
        timeRest()

    elif isRest() == False and isWork() == False:
        while isRest() == False and isWork() == False:
            cont += 1
            time.sleep(1)
            if cont >= 60:
                logging.error('não encontrou o botão rest All e nem o work All em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                recarregar(False)

    logging.debug('encontrou o botão rest All e vai colocar pra descansar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    cont = 0
    time.sleep(1)
    pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/restAll.png', confidence=.7), None, 0.5)
    pyautogui.click()
    work = False
    while work == False:
        cont += 1
        if pyautogui.locateOnScreen('./buttons/workAll.png', confidence=.8) != None:
            work = True  
            cont = 0
        elif cont > 60:
            logging.error('não encontrou o botão work All em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar()
        time.sleep(1)
    
    logging.debug('todo mundo descansando; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    timeRest()
    
def isComplete():
    locateComplete=False
    cont = 0
    while locateComplete==False:
        time.sleep(1)
        cont += 1
        if pyautogui.locateOnScreen('./buttons/complete.png', confidence=.8) != None:
            locateComplete=True
            cont = 0
            pyautogui.moveTo(1300, 750)
            time.sleep(1)
            pyautogui.click()
            logging.debug('mapa completo e clicado; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        elif cont > 60:
            logging.error('nao conseguiu clicar no botao de novo mapa, ira recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar(True)

def isError(trabalho=True, minRestantes=81):
    if trabalho:
        logging.error('detectou algum botao de erro e ira recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        recarregar(trabalho)
    else:
        logging.error('detectou algum botao de erro durante o descanso, ira recarregar e continuar mais '+str(minRestantes)+' minutos descansando; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        recarregar(trabalho, minRestantes)

def timeWork():
    logging.info('tempo de trabalho; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    for x in range(1, 36):
        locateHunt=False
        locateBack=False
        cont = 0
        time.sleep(60)
        logging.info('passou 1 min de trabalho: '+str(x)+' minutos; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        '''if pyautogui.locateOnScreen('./buttons/complete.png', confidence=.8) != None:
            logging.info('deu mapa completo; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            isComplete()
            logging.info('voltou ao trabalho; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))'''
        '''if pyautogui.locateOnScreen('./buttons/unknown.png', confidence=.5) != None:
            logging.error('erro detectado na tela; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            isError()'''
        if x % 5 == 0:
            logging.debug('resetando mapa para evitar hero bugado; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            while locateBack==False:
                time.sleep(1)
                cont += 1
                if pyautogui.locateOnScreen('./buttons/back.png', confidence=.8) != None:
                    locateBack = True
                    pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/back.png', confidence=.8), None, 0.5)
                    pyautogui.click()
                    time.sleep(1)
                    logging.debug('mapa fechado; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                    cont = 0
                    while locateHunt==False:
                        time.sleep(1)
                        cont += 1
                        if pyautogui.locateOnScreen('./buttons/hunt.png', confidence=.8) != None:
                            locateHunt = True
                            pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/hunt.png', confidence=.8), None, 0.5)
                            pyautogui.click()
                            time.sleep(1)
                            logging.debug('voltando ao mapa; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                        elif cont > 60:
                            logging.error('nao encontrou o botão para voltar pro mapa em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                            recarregar(True)
                elif cont > 60:
                    logging.error('nao encontrou o botão para sair do mapa em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                    recarregar(True)

    logging.info('fim do tempo de trabalho; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    locateBack = False
    cont = 0
    while locateBack == False:
        time.sleep(1)
        cont += 1
        if pyautogui.locateOnScreen('./buttons/back.png', confidence=.8) != None:
            locateBack = True
            pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/back.png', confidence=.8), None, 0.5)
            pyautogui.click()
            logging.debug('mapa fechado; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            time.sleep(1)
            putRest()
        elif cont > 60:
            logging.error('nao encontrou o botão para sair do mapa em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar(False)

def timeRest(continua=False, minRestantes=76):
    logging.info('tempo de descanso; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    if continua==True:
        logging.debug('continuando tempo de descanso apos erro; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))

    for x in range(1, minRestantes):
        time.sleep(60)
        logging.debug('passou 1 min de descanso: '+str(x)+' minutos; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        if pyautogui.locateOnScreen('./buttons/unknown.png', confidence=.5) != None:
            logging.error('erro detectado na tela; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            isError(False, (minRestantes-x))
    
    logging.debug('fim do tempo de descanso; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    cont = 0
    close = False
    while close == False:
        time.sleep(1)
        cont += 1
        if pyautogui.locateOnScreen('./buttons/close.png', confidence=.8) != None:
            close = True
            pyautogui.moveTo(pyautogui.locateOnScreen('./buttons/close.png', confidence=.8), None, 0.5)
            pyautogui.click()
            logging.debug('fechou a tela de herois; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            time.sleep(1)
            putWork()
        elif cont > 60:
            logging.error('nao encontrou o botão para fechar a tela de herois em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar(True)
    

def main():
    #recarregar()
    #login(False, 49)
    #logging.debug(pyautogui.pixel(1270, 440))
    #getPos()
    #putWork()
    login()
    #logging.debug(workClicked())
    #pyautogui.click('./buttons/connect.png')

main()

