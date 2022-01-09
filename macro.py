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

def workClicked():
    resp = False
    if pyautogui.pixel(1220, 760) == (212, 212, 212):
        resp = True
    
    return resp

def restClicked():
    resp = False
    if pyautogui.pixel(1270, 440) == (248, 121, 26):
        resp = True
    
    return resp

def isWork():
    resp = False
    if pyautogui.locateOnScreen('./buttons/workAll.png', confidence=.6) != None:
        resp = True
    
    return resp

def isRest():
    resp = False
    if pyautogui.locateOnScreen('./buttons/restAll.png', confidence=.6) != None:
        resp = True
    
    return resp

def recarregar(trabalho=True, minRestantes=91):
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('f5')
    pyautogui.keyUp('f5')
    pyautogui.keyUp('ctrl')
    time.sleep(5)
    logging.debug('aba recarregada; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    login(trabalho, minRestantes)

def login(trabalho=True, minRestantes=91):
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
            pyautogui.click('./buttons/connect.png')    
        
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
            pyautogui.click('./buttons/signMeta.png')
        
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
            elif trabalho == False and minRestantes == 91:
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
            pyautogui.click('./buttons/heroes.png')
        elif cont > 60:
            logging.error('nao encontrou o botao herois em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar(True)

    time.sleep(2)

    if isWork() == False:
        while isWork() == False:
            cont += 1
            time.sleep(2)
            if cont > 60:
                logging.error('não encontrou o botão work All em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                recarregar()

    logging.debug('encontrou o botão work All e colocara para trabalhar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    cont = 0
    pyautogui.moveTo(1210, 764)
    time.sleep(1)
    pyautogui.dragTo(1210, 70, 2, button='left')
    pyautogui.moveTo(1210, 764)
    time.sleep(1)

    if workClicked() == True:
        logging.info('ja estao todos trabalhando; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    else:
        while workClicked() == False:
            for x in range (1, 17):
                pyautogui.click()
                logging.info('colocou '+str(x)+' para trabalhar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                time.sleep(1.5)
                if workClicked() == True:
                    break
    
    logging.info('colocou todo mundo pra trabalhar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))

    pyautogui.moveTo(1350, 370, 1)
    pyautogui.click()
    logging.debug('saiu da tela de herois; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    time.sleep(1)

    while locateHunt==False:
        time.sleep(1)
        cont += 1
        if pyautogui.locateOnScreen('./buttons/hunt.png', confidence=.8) != None:
            locateHunt = True
            cont = 0
            logging.debug('encontrou o botão pra abrir o mapa; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            time.sleep(1)
            pyautogui.moveTo(1290, 550)
            time.sleep(1)
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
            pyautogui.click('./buttons/heroes.png')
        elif cont > 60:
            logging.error('nao encontrou o botão herois em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            recarregar(False)

    time.sleep(1)

    if isWork() == False:
        while isWork() == False:
            cont += 1
            time.sleep(1)
            if cont >= 60:
                logging.error('não encontrou o botão home em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                recarregar(False)

    logging.debug('encontrou o botão home e vai colocar pra descansar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    cont = 0
    
    pyautogui.moveTo(1270, 440)

    if restClicked() == True:
        logging.info('ja estao todos descansando; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    else:
        while restClicked() == False:
            for x in range (1, 17):
                pyautogui.click()
                logging.debug('colocou '+str(x)+' para descansar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                time.sleep(1.5)
                if restClicked() == True:
                    break
    
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


def isError(trabalho=True, minRestantes=91):
    if trabalho:
        logging.error('detectou algum botao de erro e ira recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        recarregar(trabalho)
    else:
        logging.error('detectou algum botao de erro durante o descanso, ira recarregar e continuar mais '+str(minRestantes)+' minutos descansando; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        recarregar(trabalho, minRestantes)

def timeWork():
    logging.info('tempo de trabalho; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    for x in range(1, 33):
        locateHunt=False
        cont = 0
        time.sleep(60)
        logging.info('passou 1 min de trabalho: '+str(x)+' minutos; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        if pyautogui.locateOnScreen('./buttons/complete.png', confidence=.8) != None:
            logging.info('deu mapa completo; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            isComplete()
            logging.info('voltou ao trabalho; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
        if pyautogui.locateOnScreen('./buttons/unknown.png', confidence=.5) != None:
            logging.error('erro detectado na tela; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            isError()
        if x % 5 == 0:
            logging.debug('resetando mapa para evitar hero bugado; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            pyautogui.moveTo(855, 290)
            time.sleep(1)
            pyautogui.click()
            logging.debug('mapa fechado; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
            while locateHunt==False:
                time.sleep(1)
                cont += 1
                if pyautogui.locateOnScreen('./buttons/hunt.png', confidence=.8) != None:
                    locateHunt = True
                    pyautogui.moveTo(1290, 550)
                    time.sleep(1)
                    pyautogui.click()
                    logging.debug('voltando ao mapa; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                elif cont > 60:
                    logging.error('nao encontrou o botão para voltar pro mapa em 1 min e vai recarregar; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
                    recarregar(True)
    
    logging.info('fim do tempo de trabalho; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    pyautogui.moveTo(855, 290)
    time.sleep(1)
    pyautogui.click()
    logging.debug('mapa fechado; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    time.sleep(2)
    putRest()

def timeRest(continua=False, minRestantes=91):
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
    pyautogui.moveTo(1350, 370)
    time.sleep(1)
    pyautogui.click()
    logging.debug('fechou a tela de herois; '+str(datetime.now().strftime("%H:%M:%S, %d/%m/%Y")))
    time.sleep(2)
    putWork()

def main():
    #recarregar()
    #login(False)
    #logging.debug(pyautogui.pixel(1270, 440))
    #getPos()
    #putWork()
    #login()
    #logging.debug(workClicked())
    #pyautogui.click('./buttons/connect.png')

main()

