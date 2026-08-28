#presedencia de operadores en python

#1.parentesis():primero se evalua
#2.exponente **:calcula la potencia de cada numero
#3.unarios +,-:operadores de unarios de psitivo y negativo
#4.multiplicacion *, division /, divion entera //, modulo %
#5.operadores de comparacion(==,!=,>,<,>=,<=)
#7.operadores logicos not, and, or
#8.asignacion(=, +=, -=, *=, /=)
#-------------------------------------------------------------------------------------------------------------------------------------------------

resultado = 12 // 3 + 2 * 3 - 1
print(f'resultado: {resultado}')

#-----------------------------------------
#12 // 3 se evalua la division entera (//)
#2*3 se multiplica

#4 + 6 se suma

#finalmente se resta
#10-1

#resualtado 9 

resultado = 12 // (3 + 2) * 3 - 1
print(f'resultado: {resultado}')
