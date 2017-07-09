def sender_email(form=None, subject=None, temp_html=None, temp_text=None):
    '''
    Email send
    
    :param form: form instance
    :param subject: form name
    :param temp_html: 'example.html'
    :param temp_text: 'example.txt'
    :return: 
    '''
    from vedansha import settings
    from django.core.mail import send_mail
    from django.template.loader import render_to_string
    data = form.cleaned_data if form else {}
    data.update({'subject': subject})
    msg_html = render_to_string('email/%s' % temp_html, data) if temp_html else None
    msg_plain = render_to_string('email/%s' % temp_text, data) if temp_text else None
    send_mail(subject, msg_plain, settings.EMAIL_HOST_USER, ['info@vedansha.com'], html_message=msg_html)
    return
