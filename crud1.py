import os
import shutil
#import sys

menu = """
1. ELIMINAR
2. RENOMBRAR
3. MOVER
4. MODIFICAR CONTENIDO FICHERO
5. VER CONTENIDO DE UNA CARPETA
6. VISUALIZAR NOMBRE Y RUTA DE UN FICHERO
9. SALIR
"""

#print(os.getcwd()) # devuelve directorio del trabajo actual
direct_Actual = os.getcwd()

#Leer ruta y definir si es carpeta o fichero:
#      ! modos disponibles

nombre = input("\nEscriba su nombre: \n")
print('----------------------------------------------------------------')
print("Bienvenido/a", nombre)
print(f'Te encuentras en el directorio de trabajo: {direct_Actual}\n')

while True:
    busqueda = input('¿Deseas buscar un archivo o directorio? (archivo/directorio/no): ') 
    busqueda = busqueda.lower()
    
    if busqueda == 'no':
        break
    #nomArchivo = input("Titulo del archivo: (agregar extension)")
    # existe fichero?
    if busqueda == 'archivo':
        try:
            nomArchivo = input("Titulo del archivo: (agregar extension)")
            
            #with open(nomArchivo, "r") as archivo:
            archivo = open(nomArchivo, 'r')
            print()
            print(f'Contenido:\n {archivo.read()}\n')
            archivo.close()

            print("-------------------------------------",menu, "-------------------------------------")
            opcion = input("Elige una opcion: ")
            
        
            match opcion:
                #eliminar archivo:
                case '1':
                    os.remove(nomArchivo)
                    print('\nEl archivo', nomArchivo, 'ha sido eliminado exitosamente.')

                # renombrar archivo:
                case '2':
                    try: 
                        nuevo_name = input("Escribe el nuevo nombre del archivo (incluye extension): ")
                        os.rename(nomArchivo, nuevo_name)
                        print(f'\nEl archivo {nomArchivo} ha sido renombrado exitosamente a {nuevo_name}.')

                    except FileExistsError:
                        print('El archivo ya existe. No se puede renombrar.')

                #mover archivo:
                #shutil
                case '3':
                    rutaOriginal = os.path.join(direct_Actual,nomArchivo)
                    carpetaDestino = input('Escribe el nombre de la carpeta destino:')
                    rutaDestino = os.path.join(direct_Actual,carpetaDestino, nomArchivo)
                    
                    try:
                        shutil.move(rutaOriginal, rutaDestino)
                        print(f"El archivo se ha movido exitosamente a {rutaDestino}")
                    
                    except Exception as e:
                        print(f"Error al mover el archivo: {e}")
                    
                # visualizar y modificar contenido 
                case '4':
                    datos = input('Escribe los datos para el fichero: ')
                    try:
                        with open(nomArchivo, 'a') as archivo:
                            archivo.write(f'\n{datos}')
                        with open(nomArchivo, 'r') as archivo:
                            print(f'Contenido:\n {archivo.read()}')
                    
                    except Exception as e:
                        print(f"Error al escribir el archivo: {e}")
                                   
            #VISUALIZAR NOMBRE Y RUTA DE UN FICHERO
                case '6':
                    print(f'Nombre del fichero: {nomArchivo} ')
                    rutaOriginal = os.path.join(direct_Actual,nomArchivo)
                    print(f'Se encuentra en la ruta: {rutaOriginal}')
    
                
                case '9':
                    break

                case _:
                    print('\nOpcion No Disponible.')
        
            
    # a. crear archivo:
        except FileNotFoundError: #fichero o directorio
            print(f'El archivo {nomArchivo} no existe.')
            with open(nomArchivo, 'x') as archivo:
                print('\nEl archivo', nomArchivo, 'se ha creado existosamente*')

            print(menu, "\n-------------------------------------")
            opcion = input("Elige una opcion: ")
            
            #eliminar archivo
            match opcion:
                case '1':
                    os.remove(nomArchivo)
                    print('\nEl archivo', nomArchivo, 'ha sido eliminado exitosamente.')
            
            #renombrar archivo
                case '2':
                    try: 
                        nuevo_name = input("Escribe el nuevo nombre del archivo(incluye .extension): ")
                        os.rename(nomArchivo, nuevo_name)
                        print(f'\nEl archivo {nomArchivo} ha sido renombrado exitosamente a {nuevo_name}.')

                    except FileExistsError:
                        print('El archivo ya existe. No se puede renombrar.')

            #mover archivo
                case '3':
                    rutaOriginal = os.path.join(direct_Actual,nomArchivo)
                    carpetaDestino = input('Escribe el nombre de la carpeta destino:')
                    rutaDestino = os.path.join(direct_Actual,carpetaDestino, nomArchivo)
                    
                    try:
                        shutil.move(rutaOriginal, rutaDestino)
                        print(f"El archivo se ha movido exitosamente a {rutaDestino}")
                    
                    except Exception as e:
                        print(f"Error al mover el archivo: {e}")
                        
                # visualizar y modificar contenido 
                case '4':
                    datos = input('Escribe los datos para el fichero: ')
                    try:
                        with open(nomArchivo, 'a') as archivo:
                            archivo.write(datos)
                        with open(nomArchivo, 'r') as archivo:
                            print(f'Contenido:\n {archivo.read()}\n')
                            
                    except Exception as e:
                        print(f"Error al escribir el archivo: {e}")
                        
                #VISUALIZAR NOMBRE Y RUTA DE UN FICHERO
                case '6':
                    print(f'Nombre del fichero: {nomArchivo} ')
                    rutaOriginal = os.path.join(direct_Actual,nomArchivo)
                    print(f'Se encuentra en la ruta: {rutaOriginal}')

                case '9':
                    break

                case _:
                    print('\nOpcion No Disponible.')
                
        except Exception as eR:
            print("Ha ocurrido una ", eR)
            


#----------------------------------------------------------------
    # b. crear carpeta: 
    elif busqueda == 'directorio':
        try:
            nomCarpeta = input('Escribe el nombre de la carpeta (nombreCarpeta): ')
            os.mkdir(nomCarpeta)
            print(f"\nSe creó la carpeta en {direct_Actual}")
            
            print(menu, "\n-------------------------------------")
            opcion = input("Elige una opcion: ")
            
            #eliminar carpeta
            match opcion:
                case '1':
                    shutil.rmtree(nomCarpeta)
                    print('\nLa carpeta>', nomCarpeta, '<ha sido eliminado exitosamente.')
            
            #renombrar carpeta ********************************
                case '2':
                    try:
                        nuevo_name = input("Escribe el nuevo nombre de la carpeta: ")
                        os.rename(nomCarpeta, nuevo_name)
                        print(f'\nLa carpeta {nomCarpeta} ha sido renombrado exitosamente a {nuevo_name}.')

                    except FileExistsError:
                         print('Nombre invalido. Existe una carpeta con ese nombre.')
            
            #mover archivo
                case '3':
                    rutaOriginal = os.path.join(direct_Actual,nomCarpeta)
                    carpetaDestino = input('Escribe el nombre de la carpeta destino:')
                    rutaDestino = os.path.join(direct_Actual,carpetaDestino, nomCarpeta)
                    
                    try:
                        shutil.move(rutaOriginal, rutaDestino)
                        print(f"La carpeta se ha movido exitosamente a {rutaDestino}")
                    
                    except Exception as e:
                        print(f"Error al mover el archivo: {e}")
                
                # ver contenido de una carpeta
                case '5':
                    ruta = os.path.join(direct_Actual,nomCarpeta)
                    contenidoCarpeta = os.listdir(ruta)
                    print("Contenido de la carpeta:")
                    for info in contenidoCarpeta:
                        print(info)
                    
                case '9':
                    break
                        

                case _:
                    print('\nOpcion No Disponible.')
                          

    # b. verificar carpeta
        # La carpeta existe!
        except FileExistsError:
            print('\nLa carpeta en', direct_Actual, 'ya existe!')
            print(menu, "\n-------------------------------------")
            opcion = input("Elige una opcion: ")
            
            #eliminar carpeta
            match opcion:
                case '1':
                    shutil.rmtree(nomCarpeta)
                    print('\nLa carpeta>', nomCarpeta, '<ha sido eliminado exitosamente.')
            
            #renombrar carpeta ********************************
                case '2':
                    try:
                        nuevo_name = input("Escribe el nuevo nombre de la carpeta: ")
                        os.rename(nomCarpeta, nuevo_name)
                        print(f'\nLa carpeta {nomCarpeta} ha sido renombrado exitosamente a {nuevo_name}.')

                    except FileExistsError:
                        print('Nombre invalido. Existe una carpeta con ese nombre.')
            
            #mover archivo
                case '3':
                    rutaOriginal = os.path.join(direct_Actual,nomCarpeta)
                    carpetaDestino = input('Escribe el nombre de la carpeta destino:')
                    rutaDestino = os.path.join(direct_Actual,carpetaDestino, nomCarpeta)
                    
                    try:
                        shutil.move(rutaOriginal, rutaDestino)
                        print(f"La carpeta se ha movido exitosamente a {rutaDestino}")
                    
                    except Exception as e:
                        print(f"Error al mover el archivo: {e}")
                        
                # ver contenido de una carpeta
                case '5':
                    ruta = os.path.join(direct_Actual,nomCarpeta)
                    contenidoCarpeta = os.listdir(ruta)
                    print("Contenido de la carpeta:")
                    for info in contenidoCarpeta:
                        print(info)
                    
                    
                case '9':
                    break
                        

                case _:
                    print('\nOpcion No Disponible.')
