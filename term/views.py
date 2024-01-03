from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.functions import Lower
from django.db.models import F
from dictionary.settings import BASE_DIR
from .models import Term
from .forms import ContactForm
from django.template.loader import get_template
# from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
# from django.core import mail
# from smtplib import SMTP
from redmail import EmailSender
from markupsafe import Markup
from pathlib import Path
import os
from django.views.generic import DetailView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

class TermDetailView(DetailView):
    model = Term
    template_name = "term/term.html"


email = EmailSender(
    host='smtp.office365.com',
    port=587,
    username='A1231231231231999@outlook.com',
    password='Wu57u4n6'
)
email.receivers=['A1231231231231999@outlook.com']
email.sender='A1231231231231999@outlook.com'
email.set_template_paths(Path(os.path.join(BASE_DIR, 'templates\\term')))

# jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
# jinja_env.join_path('message.html', 'templates/term/')
# email.templates_html = jinja_env

# host = "smtp.office365.com: 587"
# to_addr = "A1231231231231999@outlook.com"
# from_addr = "A1231231231231999@outlook.com"
# password = "Wu57u4n6"
# subject = "User message from Contact form"
# body_text = "Python rules them all!"

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
termdict = {}

def main(request):
    terms = Term.objects.order_by('title')
    for letter in alphabet:
        term_char = terms.filter(title__startswith=letter)
        termdict[letter] = term_char
    return render(request, 'term/main.html', {'termdict': termdict, 'alphabet': alphabet})

def homecarusel(request):
    # terms = Term.objects.order_by('title')
    return render(request, 'term/homecarusel.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'term/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homecarusel')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'The user name already exist'})
        else:
            return render(request, 'term/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'term/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'term/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('homecarusel')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        print('LogOut')
        logout(request)
        return redirect('homecarusel')

# def all_terms(request,char_name='A'):
#     terms = Term.objects.all()
#     # terms = Term.objects.filter(title='Apache Kafka')
#     # terms = Term.objects.filter(title__contains='k')
#     # terms = Term.objects.filter(title__startswith=char_name)
#     # terms = get_list_or_404(Term,title__startswith=char_name)
#     if terms:
#         print('Found needed term')
#     else:
#         print('Not found needed term')
#     return render(request, 'term/all_terms.html', {'terms':terms, 'alphabet': alphabet})

def allterms(request):
    terms = Term.objects.order_by('title')
    for letter in alphabet:
        term_char = terms.filter(title__startswith=letter)
        termdict[letter] = term_char
    return render(request, 'term/allterms.html', {'termdict': termdict, 'alphabet': alphabet})


def terms(request,char_name=None, msg=None):
    if char_name != None:
        terms = Term.objects.filter(title__startswith=char_name).order_by('title')
        if terms:
            print(terms)
        else:
            msg = 'Термін що починається на цю літеру відсутні у словнику. Будь ласка використовуйте Пошук!'
            print(msg)
    return render(request, 'term/terms.html', {'terms':terms, 'alphabet': alphabet, 'char_name': char_name, 'msg': msg})

def termsearch(request, pattern_name=None, msg=None):
    if request.method == 'GET':
            print(request.POST['pattern_name'])
    else:
        pattern_name = request.POST['pattern_name']
        pattern_name_lower = pattern_name.lower()
    terms = Term.objects.annotate(title_lower=Lower(F('title'))).filter(title_lower__contains=pattern_name_lower).order_by('title')
    if not terms:
        msg = 'Термін або частина терміну відсутні у словнику.'
    return render(request, 'term/termsearch.html', {'terms': terms, 'alphabet': alphabet, 'pattern_name': pattern_name, 'msg': msg})

def term(request, term_id):
    term = get_object_or_404(Term, pk=term_id)
    print(term.title)
    return render(request, 'term/term.html', {'term':term, 'alphabet': alphabet})

# def help(request):
#     return render(request, 'term/help.html')

# def contacts(request):
#     return render(request, 'term/contacts.html')

@login_required
def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send_mail(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            # send_email(host, subject, to_addr, from_addr, sender, body_text, password)
            email.send(
                subject='EmailSender subject',
                html_template='message.html',
                body_params={
                    'project_name': 'Big Data Hub',
                    'company': "Форма зворотнього зв'язку",
                    'email': Markup(form.cleaned_data['email']),
                    'name':  Markup(form.cleaned_data['name']),
                    'message': Markup(form.cleaned_data['message'])
                }

                #.......................................................................
                # html="""
                #     <br>
                #     <p>Доброго дня шановний Адміністратор ресурсу: <strong>{{ project_name }}</strong>,</p>
                #     <p style="opacity: 1; transform: translate3d(0px, 0px, 0px);">
                #     Дата: {{ now }}
                #     </p>
                #     <hr>
                #     <p>Вам надішло письмо від відвидувача: <strong>{{ client }}</strong>.</p>
                #     <p>Зворотня поштова адреса: <strong>{{ sender }}</strong></p>
                #     <p><strong>Повідомлення клієнта</strong>:
                #     <hr>
                #     <p style="opacity: 1; transform: translate3d(0px, 0px, 0px);">
                #     {{ message }}
                #     </p>
                #     <hr>
                #     <br>
                #     <p>З повагою,
                #     <br>{{ company }}</p>
                # """,
                # text="""
                #     Hi {{ client }},
                #     we are opening the source of {{ project_name }}.

                #     Kind regards,
                #     {{ company }}
                # """,
                # body_params={
                #     'project_name': 'Big Data Hub',
                #     'company': "Форма зворотнього зв'язку",
                #     'sender': form.cleaned_data['email'],
                #     'client':  form.cleaned_data['name'],
                #     'message': Markup(form.cleaned_data['message'])
                # }
                #.......................................................................
            )           
             
            # print(jinja_env.get_template('D:\Documentation\Python\Django\Projects\big_data\dictionary\term\templates\term\message.html'))
            # template = jinja_env.get_template('term\message.html')
            # print(template)
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'term/contacts.html', context=context)

def view_404(request, exception):
    return render(request, "errors/404.html", status=404)

def view_500(request):
    return render(request, "errors/500.html", status=500)


