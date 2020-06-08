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

encuesta = Encuesta()

preguntas = encuesta.n_encuesta['preguntas']

def ingresar_pregunta():
    continuar = 'si'
    if continuar == 'si':
        pregunta_respuestas = []            
       
        for nueva_respuesta in range(4):
            nueva_respuesta = 'si'
            pregunta  = input("Ingrese Pregunta:\n")
            respuestas = []
            while nueva_respuesta == 'si':
                respuestas.append(input("ingrese su respuesta:\n"))                            
                nueva_respuesta = input("Desea ingresar otra respuesta?:")
                nueva_pregunta = {}
                nueva_pregunta[pregunta] = respuestas
                print(pregunta_respuestas)
            
            pregunta_respuestas.append(nueva_pregunta)
            continuar = input("ingrear nueva pregunta?")
            if continuar == "no":
                encuesta.n_encuesta['preguntas'] = pregunta_respuestas
                print(nueva_pregunta)
                break
            
            
            
    

encuesta.n_encuesta['titulo'] = input("Ingrese un titulo:\n")
encuesta.n_encuesta['grupo'] = input("Ingrese un grupo:\n")
encuesta.n_encuesta['vencimiento'] = input("Ingrese un vencimiento:\n")

ingresar_pregunta()





print(encuesta.n_encuesta)