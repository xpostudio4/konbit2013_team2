 Detalle aplicacion de SMS

Mensaje a Voz
1.- Se utiliza el celular como gateway para recibir los mensajes (SMS) con ushahidi   (http://smssync.ushahidi.com/).
2.- Se envia el mensaje a una url definida con cualquier framework (Django, Flask o Falco me vienen a la mente). 
3.- Del mensaje se extrae el numero, proposito (voice, Email), texto y numero a enviarlo, junto con la fecha.
4.- Se transforma el texto a audio con el API de Twilio (http://www.twilio.com/docs/api/twiml), twilio no posee un api para traducir creol. Solo nos queda Espanol, Frances e Ingles (http://www.twilio.com/docs/api/twiml/say).
5.- Con el app de twilio colocamos la grabacion del texto en el numero que nos solicitaron.
6.- Confirmamos la entrega con un mensaje a la persona en audio diciendo que la persona recibio el email.
7.- Manejo potenciales errores.

Voz a mensaje?

def message_processing(request, message, send_to, send_from, purpose):
	"""The purpose of this function is to process the information of the message
