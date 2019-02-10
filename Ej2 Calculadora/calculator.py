import subprocess
subprocess.call('', shell=True)

import screen

#Pantalla inicial
def printScreen():
    screen.Print("Sol..:",2,1)    
    screen.Print("OP1:",2,28)    
    screen.Print("OP2:",3,28)
    screen.Print("f:",4,30)
    input=screen.Input("INPUT ", 5, 1)
    valor=input.replace(',','.')
    return valor

#Pantalla tras realizar cada operación
def printScreen2():
    screen.Print("Sol..:",2,1,True)
    screen.Print("OP1:",2,28,True)
    screen.Print("OP2:",3,28,True)
    screen.Print("f:",4,30,True)

def validarinput(valor):
    try:
        float(valor)
        return True
    except:
        return False #o pass

def main(input,file):
    
    banderaop1=False
    banderaop2=False
    banderaf=False
    
    while input!="fin": 
        #mientras tenga las casillas vacías, las voy llenando. Las casillas se llenan en cualquier orden
        if not banderaop1 or not banderaop2 or not banderaf:
            if validarinput(input) and not banderaop1:
                inputop1=float(input)
                screen.Print('{:.2f}'.format(inputop1),2,33)
                banderaop1=True
                
            elif validarinput(input) and not banderaop2 and banderaop1:
                inputop2=float(input)
                screen.Print('{:.2f}'.format(inputop2),3,33)
                banderaop2=True
                
            elif validarinput(input) and banderaop2 and banderaop1:
                screen.Print('Introduzca un operador',10,1)
                
            elif not validarinput(input) and input in operaciones:                 
                if not banderaf: 
                    screen.Print(input,4,33)
                    inputoperacion=input
                    screen.clearLine(10,1)
                    banderaf=True
                        
    
        #cuando tengo las tres casillas llenas, hago la operación     
                    
        if banderaop1 and banderaop2 and banderaf:
            banderaop1=False
            banderaop2=False
            banderaf=False
            if inputoperacion=='+':
                operacion=inputop1+inputop2
            elif inputoperacion=='-':
                operacion=inputop1-inputop2
            elif inputoperacion=='x':
                operacion=inputop1*inputop2
            elif inputoperacion=='d':    #no puedo hacer /
                operacion=inputop1/inputop2
            elif inputoperacion=='%':
                operacion=inputop1%inputop2
            elif inputoperacion=='//':
                operacion=inputop1//inputop2
            elif inputoperacion=='^':
                operacion=inputop1**inputop2
            
            screen.Print(operacion,2,8)
            
            #Escribo las operaciones en el fichero calculos.txt y borro datos sin el input
            #Si no se termina una operación completa, no se imprime nada en el fichero
            file.write("Sol..:{:3.2f}".format(operacion))
            file.write("          op1..:{:3.2f}\n\n".format(inputop1))
            file.write("                    op2..:{:3.2f}\n\n".format(inputop2))
            file.write("Input:")
            file.write("              f..:{:3s}".format(inputoperacion))         
            file.write("\n\n-------------------------------------------\n\n")
            
            printScreen2()
    
        
        input=screen.Input("INPUT ", 5, 1)
        input=input.replace(',','.')
        

f=open("calculos.txt","w+")
f.write("Calculadora:\n\n")
screen.locate(12,1)                   
screen.clear()
res=printScreen()
operaciones=["+","-","x","d","%","//","^"]
main(res,f)
f.close()
       
        
    
    
    
    
    
        
        





    

