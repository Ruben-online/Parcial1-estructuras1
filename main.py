from circular_list import CircularList

polinomios = CircularList()



while True:
    print("Menu polinomios\n")
    print("1. Ingresar componentes del polinomio")
    print("2. Adicion y sustraccion")
    print("3. Evaluar Polinomios")
    print("4. Salir")

    option_menu = input("Ingrese una opcion: ")

    if option_menu == "1":
        print("\nMenu de ingreso de polinomios")
        print("1. Ingresar polinomios")
        print("2. Editar polinomios")
        print('3. Regresar al menu principal')

        ingreso_menu = input("Ingrese una opcion: ")

        if ingreso_menu == "1":
            print("Ingresar polinomios\n")
            coeficiente_a= input("Ingrese el polinomio 'A': ")
            grado_a = int(input("Ingrese el grado de 'A': "))
            coeficiente_b= input("Ingrese el polinomio 'B': ")
            grado_b = int(input("Ingrese el grado de 'B': "))

            polinomios.add_polinomio(coeficiente_a, grado_a)
            polinomios.add_polinomio(coeficiente_b, grado_b)

            print("Los polinomios actuales son: ")
            polinomios.print_list()

        elif ingreso_menu == "2":
            print("Editar polinomios\n")
            pass


    elif option_menu == "2":
        while True:
            print("\nMenu adicion y sustraccion")
            print("1. Sumar polinomios")
            print("2. Restar polinomios")
            print("3. Regresar al menu principal")

            addsus_menu = input("Ingrese una opcion: ")

            if addsus_menu == "1":
                add_result = coeficiente_a, grado_a + coeficiente_b, grado_b
                print(f"La suma de los polinomios {coeficiente_a, grado_a} y {coeficiente_b, grado_b} "
                      f" es {add_result}")

            elif addsus_menu == "2":
                sus_result = coeficiente_a, grado_a - coeficiente_b, grado_b
                print(f"La resta de los polinomios {coeficiente_a, grado_a} y {coeficiente_b, grado_b} "
                      f"es {sus_result}")

            elif addsus_menu == "3":
                break
            else:
                print("Seleccione una opcion valida")

    elif option_menu == "3":
        print("Evaluar polonimios")
        print("1. ", coeficiente_a, grado_a )
        print("2. ", coeficiente_b, grado_b)

        resolver_polinomio = input("Ingrese el polinomio que desea resolver: ")

        if resolver_polinomio == "1":
            print(f"El polinomio que desea resolver es {coeficiente_a, grado_a}")
            variable = float(input("Ingrese el valor que desea asignar a la variable: "))
            pass

        elif resolver_polinomio == "2":
            print(f"El polinomio que desea resolver es {coeficiente_b, grado_b}")
            variableb = float(input("Ingrese el valor que desea asignar a la variable: "))
            pass

        else:
            print("Ingrese una opcion valida")



    elif option_menu == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo, opcion incorrecta")