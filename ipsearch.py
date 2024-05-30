from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuración del servidor SMTP con la contraseña de aplicación
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'orchackermaster@gmail.com'
APP_PASSWORD = 'bobbrdewhluttdnx'
EMAIL_TO = 'orchackermaster@gmail.com'
EMAIL_SUBJECT = 'Dirección IP registrada'

def send_email(ip_address):
    body = f"El dispositivo con la IP {ip_address} ha hecho clic en el enlace."
    msg = MIMEText(body)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = SMTP_USERNAME
    msg['To'] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, APP_PASSWORD)
            server.sendmail(SMTP_USERNAME, EMAIL_TO, msg.as_string())
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

@app.route('/track')
def track():
    if request.headers.getlist("X-Forwarded-For"):
        ip_address = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip_address = request.remote_addr
    send_email(ip_address)
    return "Tu IP ha sido registrada."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
