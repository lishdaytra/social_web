from django.urls import reverse_lazy
from django.views import generic
from users.forms import CustomUserCreationForm, UserImageForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    # Set user Group on registration
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # One user Group
            user_group = Group.objects.get_by_natural_key(name=form.cleaned_data['groups'])
            user.groups.add(user_group)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form' : form})

def image_request(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_object = form.instance
            return render(request, 'users/image_form.html', {'form': form, 'img_obj': img_object})
        else:
            form = UserImageForm()

        return render(request, 'users/image_form.html', {'form': form})
