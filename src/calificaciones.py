"""Primer apartado"""

def calcular_nota(aciertos,errores,total_correctas):
    nota=(aciertos*10/total_correctas)-(errores*10/(50-total_correctas))
    if nota < 0:
        nota=0    
    return nota

"""Segundo apartado"""
def solicitar_resultados(num_aciertos,num_errores,num_total_respuestas):
    return print("Los numeros de acierrtos son:", num_aciertos,"Los numeros de erroreson:",num_errores,"Los numeros de respuestas totales sn:",num_total_respuestas)

"""EJERCICIO 2"""

def calcula_nota_cuatrimestre(cuestionarios,parcial,proyecto):
    nota=()