from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404

from support.forms import ProfileForm
from support.models import Profile
from support.serializers import ProfileSerializer

def profile(request, id):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, pk=id)
        return render(request, 'profile_detail.html', {
            'profile': profile,
        })
    elif request.method == 'POST':
        pass

def addprofile(request):
    pass
    print "Hello!"
    data = request.POST.copy()
    form = ProfileForm(data)
    if request.method == 'POST':
        profile = Profile.objects.create_profile(
            data['nick_name'],
            data['first_name'],
            data['last_name'],
            data['wins'],
            data['losses'],
            data['win_streak'],
            data['created'],
            data['last_seen']
        )
    return render(request, 'profile_create.html', {
        'form': form,
    })

class ProfileCreateView(CreateView):
    """
    TODO
    """

    template_name = 'profile_create.html'
    model = Profile
    form_class = ProfileForm
    success_url = '/users'


class ProfileDetailView(DetailView):
    """
    TODO
    """

    model = Profile
    template_name = 'profile_detail.html'
    serializer_class = ProfileSerializer
