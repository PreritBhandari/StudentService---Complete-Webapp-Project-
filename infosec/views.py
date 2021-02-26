from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import InformationForm
from .models import Information


# Used ModelForm InformationForm

@login_required
def information(request):
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES, instance=request.user.information)
        #
        # instance = ko le form bhitra data haru dinxa kholda kheri taki ramrari update garna paos .
        # tyo lekhena bhane khali hunxa tyo field tessai.

        if form.is_valid():
            form.save()
            messages.success(request, f'Information updated.')
            return redirect('infosec')

    else:

        form = InformationForm(instance=request.user.information)

    context = {
        'form': form

    }

    return render(request, 'infosec/infosec.html', context)


class CreateInfoSec(CreateView, LoginRequiredMixin):
    model = Information
    template_name = 'infosec/infoadd.html'
    fields = ['resume', 'github_link', 'facebook_link', 'phone_no', 'father_name', 'mother_name',
              'guardian_no', 'address']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListInfoSec(ListView, LoginRequiredMixin):
    model = Information
    template_name = 'infosec/infosec-list.html'
    context_object_name = 'infos'
    queryset = Information.objects.all()
    fields = ['resume', 'phone_no', 'father_name', 'mother_name', 'address', 'guardian_no', 'github_link',
              'facebook_link']
