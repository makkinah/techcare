# Definir respuestas predeterminadas
respuestas = {
    "hola": "¡Hola! ¿En qué puedo ayudarte hoy?",
    "pedidos": "Para realizar un pedido, contáctanos a través del correo electrónico techcaresolutions2@gmail.com.",
    "envío": "El tiempo de envío depende de tu ubicación. Normalmente, los envíos se entregan en 3-5 días hábiles.",
    "pago": "Aceptamos transferencia bancaria y pagos en efectivo.",
    "despedida": "¡Gracias por contactarnos! Que tengas un buen día."
}

# Función para procesar la consulta del cliente y generar una respuesta
def procesar_consulta(consulta):
    consulta = consulta.lower()
    respuesta = respuestas.get(consulta, "Lo siento, no puedo responder a eso en este momento.")
    return respuesta

# Función principal del servicio al cliente
def servicio_al_cliente():
    print("Bienvenido al servicio al cliente. Por favor, ingresa tus consultas o escribe 'despedida' para salir.")

    while True:
        # Obtener la consulta del cliente
        consulta = input("> ")

        # Procesar la consulta y generar una respuesta
        respuesta = procesar_consulta(consulta)

        # Mostrar la respuesta al cliente
        print(respuesta)

        # Salir si el cliente escribe 'despedida'
        if consulta.lower() == "despedida":
            break

# Iniciar el servicio al cliente
if __name__ == '__main__':
    servicio_al_cliente()
