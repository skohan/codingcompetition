from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


from .utilities import do_magic
# Create your views here.

class SubmitView(LoginRequiredMixin,View):
    
    template_name = 'submission/result.html'
    file_name = 'file'

    def post(self, request, problem_id):

        context = {}
        
        user = request.user
        file = request.FILES[self.file_name]

        results = do_magic(file, user, problem_id)
        context['results'] = results


        return render(request, self.template_name, context)
