class Encuesta:

    def __init__(self):
        pass

    def nuevaencuesta(self, titulo, listado):
        self.titulo = titulo
        self.listado = listado #listado de preguntas con sus respuestas

    def imprimirtitulo(self):
        print(self.titulo)

class PreguntaYrespuestas:

    def __init__(self):
        pass

    def preguntaYrespuestas(self, pregunta, listadoRespuestas):
        self.pregunta = pregunta
        self.listadoRespuestas = listadoRespuestas

    def imprimirtitulo(self):
        print(self.listadoRespuestas)

encuesta = Encuesta()

preguntaYrespuestas = PreguntaYrespuestas()

listadoRespuestas = []

PreguntaYrespuestas.listadoRespuestas = listadoRespuestas

preguntaYrespuestas.pregunta = ""



encuesta.titulo = input("Ingresar titulo:\n")

ingresarPregunta = input("Desesa ingresar una pregunta?:")

while ingresarPregunta == "si":
    pregunta = input("Ingrese pregunta:\n")
    preguntaYrespuestas.pregunta = pregunta
    continuar = "si"
    indice = 1
    
    while indice < 4 and continuar == "si" :                
        respuesta = input("Ingrese respuesta:\n")
        listadoRespuestas.append(respuesta)
        continuar = input("Desea ingresar otra respuesta:\n")
        indice = indice + 1
        
    #continuar = input("Desea ingresar otra respuesta:\n")
    ingresarPregunta = input("Desesa ingresar una pregunta?:")
 
listadoRespuestas.append(respuesta)
preguntaYrespuestas.pregunta = pregunta
    

encuesta.imprimirtitulo()
preguntaYrespuestas.imprimirtitulo()





if __name__ == "__main__":
    print("ok")
    pass