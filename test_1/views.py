from django.shortcuts import render
from .models import About, MainIndex, Menu, Forwhom, Freeles
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.generic import CreateView
from .forms import LoginForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


# Create your views here.

#Форма обратной связи.
class ContactCreate(CreateView):
    model = Freeles
    succes_url = reverse_lazy('succes_page')
    form_class = ContactForm
    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение с формы от {data["first_name"]}. Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)
def emeil(subject, content):
    send_mail(
        subject,
        content,
        'отправитель@gmail.com',
        ['получатель@gmail.com']
    )
def success(request):
    return HttpResponse('Письмо отправлено!')




'''class AboutListView(generic.ListView):
    model = About
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context'''
def index(request):
# Строка меню.
    logo = str(getattr(Menu.objects.first(), 'logo'))[14:]
    menu_text_1 = getattr(Menu.objects.first(), 'menu_text_1')
    menu_text_2 = getattr(Menu.objects.first(), 'menu_text_2')
    menu_text_3 = getattr(Menu.objects.first(), 'menu_text_3')
    menu_text_4 = getattr(Menu.objects.first(), 'menu_text_4')
    text_lk = getattr(Menu.objects.first(), 'text_lk')
# Блок MainIndex.
    index_h1 = str(getattr(MainIndex.objects.first(), "index_h1")).split(' ')
    index_h1_slice_1 = index_h1[0] + ' ' + index_h1[1]
    index_h1_slice_2 = index_h1[2] + ' '
    index_h1_slice_3 = index_h1[3] + ' '
    index_h1_slice_4 = ' '.join([i for i in index_h1[4 :]])
    index_h2 = getattr(MainIndex.objects.first(), "index_h2")
    index_a_1 = getattr(MainIndex.objects.first(), "index_a_1")
    index_a_2 = getattr(MainIndex.objects.first(), "index_a_2")
    index_img = str(getattr(MainIndex.objects.first(), 'index_img'))[14:]
# Блок About.
    header = getattr(About.objects.first(), 'header')
    main_img = str(getattr(About.objects.first(), 'img'))[14:]
    main_h = getattr(About.objects.first(), 'main_h')
    main_1 = str(getattr(About.objects.first(), 'main_p_1'))[14:]
    main_2 = str(getattr(About.objects.first(), 'main_p_2'))[14:]
    main_3 = str(getattr(About.objects.first(), 'main_p_3'))[14:]
    footer = getattr(About.objects.first(), 'footer')
#Block Forwhom.
    forwhom_h1 = getattr(Forwhom.objects.first(), 'forwhom_h1')
    forwhom_h2 = getattr(Forwhom.objects.first(), 'forwhom_h2')
    forwhom_td_1_img = str(getattr(Forwhom.objects.first(), 'forwhom_td_1_img'))[14:]
    forwhom_td_1 = getattr(Forwhom.objects.first(), 'forwhom_td_1')
    forwhom_td_2_img = str(getattr(Forwhom.objects.first(), 'forwhom_td_2_img'))[14:]
    forwhom_td_2 = getattr(Forwhom.objects.first(), 'forwhom_td_2')
    forwhom_td_3_img = str(getattr(Forwhom.objects.first(), 'forwhom_td_3_img'))[14:]
    forwhom_td_3_img_byce = str(getattr(Forwhom.objects.first(), 'forwhom_td_3_img_byce'))[14:]
    forwhom_td_3  = getattr(Forwhom.objects.first(), 'forwhom_td_3')
    forwhom_td_4_img = str(getattr(Forwhom.objects.first(), 'forwhom_td_4_img'))[14:]
    forwhom_td_4 = getattr(Forwhom.objects.first(), 'forwhom_td_4')
#Форма.
    first_name = getattr(Freeles.objects.first(), 'first_name')
    email = getattr(Freeles.objects.first(), 'email')
    message = getattr(Freeles.objects.first(), 'message')
    text_left_1 = getattr(Freeles.objects.first(), 'text_left_1')
    text_left_2 = getattr(Freeles.objects.first(), 'text_left_2')
    text_left_3 = getattr(Freeles.objects.first(), 'text_left_3')
# 
    return render(
    request,
    'index.html',
    context={
        'logo': logo,
        'menu_text_1': menu_text_1,
        'menu_text_2': menu_text_2,
        'menu_text_3': menu_text_3,
        'menu_text_4': menu_text_4,
        'text_lk': text_lk,
        'index_h1': index_h1,
        'index_h1_slice_1': index_h1_slice_1,
        'index_h1_slice_2': index_h1_slice_2,
        'index_h1_slice_3': index_h1_slice_3,
        'index_h1_slice_4': index_h1_slice_4,
        'index_h2': index_h2,
        'index_a_1': index_a_1,
        'index_a_2': index_a_2,
        'index_img': index_img,
        'header': header, 
        'img': main_img, 
        'main_h': main_h, 
        'main_p_1': main_1, 
        'main_p_2': main_2, 
        'main_p_3': main_3, 
        'footer': footer,
        'forwhom_h1': forwhom_h1,
        'forwhom_h2': forwhom_h2,
        'forwhom_td_1_img': forwhom_td_1_img,
        'forwhom_td_1': forwhom_td_1,
        'forwhom_td_2_img': forwhom_td_2_img, 
        'forwhom_td_2': forwhom_td_2, 
        'forwhom_td_3_img': forwhom_td_3_img,
        'forwhom_td_3_img_byce': forwhom_td_3_img_byce, 
        'forwhom_td_3': forwhom_td_3,  
        'forwhom_td_4_img': forwhom_td_4_img, 
        'forwhom_td_4': forwhom_td_4,
        'first_name': first_name, 
        'email': email,
        'message': message,
        'text_left_1': text_left_1,
        'text_left_2': text_left_2,
        'text_left_3': text_left_3,
            }

            )


