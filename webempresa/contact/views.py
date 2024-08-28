from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm  # Asegúrate de importar el formulario aquí
from django.urls import reverse
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extraer datos del formulario
            subject = f"Mensaje de {form.cleaned_data['name']}"
            message = form.cleaned_data['content']
            from_email = form.cleaned_data['email']
            recipient_list = [settings.DEFAULT_FROM_EMAIL]  # Puedes cambiar esto por otro correo

            try:
                # Enviar el correo
                send_mail(subject, message, from_email, recipient_list)

                # Mostrar mensaje de éxito
                messages.success(request, "¡Gracias por contactarnos! Tu mensaje ha sido enviado.")
                return redirect(reverse('contact') + "?ok")
            except Exception as e:
                # Manejo de errores en caso de fallo en el envío
                messages.error(request, f"Ocurrió un error al enviar el mensaje: {str(e)}")
                return redirect(reverse('contact'))

        else:
            # Manejo de errores en caso de formulario inválido
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
