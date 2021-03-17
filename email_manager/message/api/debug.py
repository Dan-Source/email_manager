from django.core.mail import send_mail


def send_email_message():
        subject = "Testando Envio de E-mail Com Django"
        body = "Que coisas não podermos enviar isso. "
        sender = 'webmaster@teste.com'
        to = ['dan.dluis.dl@gmail.com'] #request.POST.get('email_list', None)
        send_mail(
            subject,
            body,
            sender,
            to,
            fail_silently=False,
        )

send_email_message()
