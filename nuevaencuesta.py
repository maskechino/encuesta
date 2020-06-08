class Encuesta:

    def __init__(self):
        pass

    def nuevaencuesta(self, titulo, listado):
        self.titulo = titulo
        self.listado = listadoDEpreguntas #listado de preguntas con sus respuestas

    def imprimirtitulo(self):
        print(self.titulo, "\n", self.listado)

class PreguntaYrespuestas:

    def __init__(self):
        pass

    def preguntaYrespuestas(self, pregunta, listadoRespuestas):
        self.pregunta = pregunta
        self.listadoRespuestas = listadoRespuestas

    def imprimirtitulo(self):
        print(self.listadoRespuestas)

##############################################################

encuesta = Encuesta()


###############################################################

listadoDEpreguntas = []

Encuesta.listado = listadoDEpreguntas

###############################################################

preguntaYrespuestas = {}

preguntaYrespuestas = PreguntaYrespuestas()

##############################################################

listadoRespuestas = []

PreguntaYrespuestas.listadoRespuestas = listadoRespuestas

preguntaYrespuestas.pregunta = ""

###############################################################

encuesta.titulo = input("Ingresar titulo:\n")

ingresarPregunta = input("Desesa ingresar una pregunta?:")

################################################################

while ingresarPregunta == "si":
    pregunta = input("Ingrese pregunta:\n")
    preguntaYrespuestas.pregunta = pregunta
    listadoDEpreguntas.append(preguntaYrespuestas.pregunta)
    continuar = "si"
    indice = 1
    nuevalista = []
    
    while indice < 4 and continuar == "si" :                   
        respuesta = input("Ingrese respuesta:\n")
        nuevalista.append(respuesta)
        continuar = input("Desea ingresar otra respuesta:\n")
        indice = indice + 1
        
    #continuar = input("Desea ingresar otra respuesta:\n")
    listadoRespuestas.append(nuevalista)
    ingresarPregunta = input("Desesa ingresar una pregunta?:")

listadoDEpreguntas.append(preguntaYrespuestas)


    

encuesta.imprimirtitulo()
preguntaYrespuestas.imprimirtitulo()


################################################################


if __name__ == "__main__":
    print("ok")
    pass