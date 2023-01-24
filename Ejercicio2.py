#1. Importar librerias necesarias
#2. Definir ruta de los logs y ruta para los logs de error
#3. Recorrer todos los archivos en el directorio de logs
#4. Abrir el archivo
#5. Leer el contenido del archivo
#6. Verificar si el archivo contiene la palabra "error"
#7. Si contiene "error"
#8. Copiar el archivo al directorio de errores
#9. Crear un mensaje de correo
#10. Establecer campos del correo (asunto, de, para)
#11. Enviar el correo al administrador
#12. Si no contiene "error"
#13. Eliminar el archivo

import os
import smtplib
from email.mime.text import MIMEText

# ruta de los logs
log_path = "/path/to/logs"
# ruta para los logs de error
error_path = "/path/to/Errores"

# Recorrer todos los archivos en el directorio de logs
for filename in os.listdir(log_path):
    # Abrir el archivo
    with open(os.path.join(log_path, filename), 'r') as log_file:
        log_contents = log_file.read()
        # Verificar si el archivo contiene la palabra "error"
        if "error" in log_contents:
            # copiar el archivo al directorio de errores
            os.rename(os.path.join(log_path, filename), os.path.join(error_path, filename))
            # enviar un correo al administrador
            msg = MIMEText("Error en el archivo: " + filename)
            msg['Subject'] = 'Error en el servidor'
            msg['From'] = 'server@example.com'
            msg['To'] = 'admin@example.com'

            # Enviar el correo
            s = smtplib.SMTP('localhost')
            s.sendmail(msg['From'], msg['To'], msg.as_string())
            s.quit()
        else:
            os.remove(os.path.join(log_path, filename))