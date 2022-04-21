
class calc:

    @classmethod
    def suma(cls, x, y):
        #argumentos de entrada: dos listas, cada una con un polinomio
        #retorna: la suma de los dos polinomios
        may = x
        men = y
        suma = [0]*len(may)
        if len(x) < len(y):
            men = x
            may = y
        suma = [men[i] + may[i] for i in range(len(men))]
        aux = [may[i] for i in range(len(men),len(may))]
        suma = suma + aux

        print("--------------------------------------------------------------")
        print("El resultado de sumar ", str(x), "+", str(y), " es: ", str(suma))
        print("--------------------------------------------------------------")

    @classmethod
    def resta(cls, x, y):
        #argumentos de entrada: dos listas, cada una con un polinomio
        #retorna: la resta de los dos polinomios
        may = x
        men = [y[i]*(-1) for i in range(len(y))]
        suma = [0]*len(may)
        if len(x) < len(y):
            men = x
            may = [y[i]*(-1) for i in range(len(y))]
        suma = [men[i] + may[i] for i in range(len(men))]
        aux = [may[i] for i in range(len(men),len(may))]
        res = suma + aux

        print("--------------------------------------------------------------")
        print("El resultado de restar ", str(x), "-", str(y), " es: ", str(res))
        print("--------------------------------------------------------------")