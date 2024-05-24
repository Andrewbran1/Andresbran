from os import system

def menu1():
    print('1. Convertir entre Km y Millas')
    print('2. Convertir entre m3 y pie3')
    print('3. Convertir entre pies, mts y yardas')
    print('10. Salir')
    opcion=int(input('Ingrese su opción: '))
    return opcion

def conversion_Km_millas(conversion,distancia):
    if conversion=='a':
        return distancia*0.62
    elif conversion=='b':
        return distancia*1.64
    
def conversion_m3_pie3(conversion,distancia):
    if conversion=='a':
        return distancia*35.3147
    elif conversion=='b':
        return distancia*0.0283168
    
def conversion_pie_m(conversion,distancia):
    if conversion==1:
        return distancia*0.3048
    elif conversion==2:
        return distancia*3.281

def conversion_m_yarda(conversion,distancia):
    if conversion==1:
        return distancia*1.09361
    elif conversion==2:
        return distancia*0.94

def conversion_pie_yarda(conversion,distancia):
    if conversion==1:
        return distancia*3
    elif conversion==2:
        return distancia/3


while True:
    system('cls')
    op=menu1()
    if op==1:
        conv=input('Escriba a para km a millas, y b para millas a km: ')
        conv=conv.lower()
        if conv!='a' and conv!='b':
            print('Debe elegir una opcion valida')
        else:
            if conv=='a':
                cant=float(input('Ingrese la cantidad de Kms: '))
                de_a=conversion_Km_millas(conv,cant)
                print(f'{cant} km son {de_a} millas')
                system('pause')
            else:
                cant=float(input('Ingrese la cantidad de Millas: '))
                de_a=conversion_Km_millas(conv,cant)
                print(f'{cant} millas son {de_a} km')
                system('pause')
    elif op==2:
        conv=input('Escriba a para M3 a Pies3, y b para Pie3 a M3: ')
        conv=conv.lower()
        if conv!='a' and conv!='b':
            print('Debe elegir una opcion valida')
        else:
            if conv=='a':
                cant=float(input('Ingrese la cantidad de M3: '))
                de_a=conversion_m3_pie3(conv,cant)
                print(f'{cant} M3 son {de_a} Pies3')
                system('pause')
            else:
                cant=float(input('Ingrese la cantidad de Pie3: '))
                de_a=conversion_m3_pie3(conv,cant)
                print(f'{cant} Pie3 son {de_a} M3')
                system('pause')
    elif op==3:
        conv=input('Escriba a para m a pies, b de m a yardas y c para yarda a pies: ')
        conv=conv.lower()
        if conv!='a' and conv!='b' and conv!= 'c':
            print('Debe elegir una opcion valida')
        else:
            if conv=='a':
                des=int(input('Desea convertir de pies a m escriba 1 de lo contrario 2: '))
                if des==1:
                    cant=float(input('Ingrese la cantidad de Pies: '))
                    de_a=conversion_pie_m(des,cant)
                    print(f'{cant} Pies son {de_a} Metros')
                    system('pause')
                elif des==2:
                    cant=float(input('Ingrese la cantidad de Metros: '))
                    de_a=conversion_pie_m(des,cant)
                    print(f'{cant} Metros son {de_a} Pies')
                    system('pause')
                else:
                    break
            elif conv=='b':
                des=int(input('Desea convertir de M a Yardas escriba 1 de lo contrario 2: '))
                if des==1:
                    cant=float(input('Ingrese la cantidad de Metros: '))
                    de_a=conversion_m_yarda(des,cant)
                    print(f'{cant} Metros son {de_a} Yardas')
                    system('pause')
                else:
                    cant=float(input('Ingrese la cantidad de Yardas: '))
                    de_a=conversion_m_yarda(des,cant)
                    print(f'{cant} Yardas son {de_a} Metros')
                    system('pause')
            else:
                des=int(input('Desea convertir de Yardas a Pies escriba 1 de lo contrario 2: '))
                if des==1:
                    cant=float(input('Ingrese la cantidad de Yardas: '))
                    de_a=conversion_pie_yarda(des,cant)
                    print(f'{cant} Metros son {de_a} Yardas')
                    system('pause')
                else:
                    cant=float(input('Ingrese la cantidad de Pies: '))
                    de_a=conversion_pie_yarda(des,cant)
                    print(f'{cant} Yardas son {de_a} Metros')
                    system('pause')
    elif op==10:
        break