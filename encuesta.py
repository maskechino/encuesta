import datetime

listadoEncuestas = [] #almacena las nuevas encuestas

class Encuesta:
    def __init__(self):
        self.n_encuesta = {
            'titulo' : '',
            'grupo' : None,
            'creacion' :  datetime.datetime.now().date(),
            'vencimiento' : '',
            'preguntas' : [],
        }

    def ingresar_pregunta(self):
        continuar = 'si'
        while continuar == 'si':
            pregunta_respuestas = []
            pregunta  = input("Ingrese Pregunta:\n")
            nueva_respuesta = "si"
            respuestas = []       
            indice = 1     
            while nueva_respuesta == 'si' and indice < 4:
                respuestas.append(input("ingrese su respuesta:\n"))                            
                nueva_respuesta = input("Desea ingresar otra respuesta?:\n")
                nueva_pregunta = {}
                nueva_pregunta[pregunta] = respuestas
                indice = indice + 1           
            pregunta_respuestas.append(nueva_pregunta)
            continuar = input("ingresar nueva pregunta?\n")
            encuesta.n_encuesta['preguntas'] = pregunta_respuestas


encuesta = Encuesta()

preguntas = encuesta.n_encuesta['preguntas']



def nueva_encuesta():
    encuesta.n_encuesta['titulo'] = input("Ingrese un titulo:\n")
    encuesta.n_encuesta['grupo'] = input("Ingrese un grupo:\n")
    encuesta.n_encuesta['vencimiento'] = input("Ingrese un vencimiento:\n")
    encuesta.ingresar_pregunta()

agregar_encuesta = input("Desea crear una nueva encuesta?\n")

while agregar_encuesta == "si":    
    nueva_encuesta()
    agregar_encuesta = input("Desea crear una nueva encuesta?\n")
    listadoEncuestas.append(encuesta.n_encuesta)
else:
    print("\nGracias por crear una nueva encuesta\n")



listadoEncuestas.append(encuesta.n_encuesta)

print(listadoEncuestas)