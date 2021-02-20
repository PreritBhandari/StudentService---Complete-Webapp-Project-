from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import InformationForm
from .models import Information


# Used ModelForm InformationForm
# Used Generic Class Based Views


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
