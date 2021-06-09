import json
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


from .utilities import do_magic
# Create your views here.

class SubmitView(LoginRequiredMixin,View):
    
    submit_template = ''
    result_template = 'submission/result.html'
    file_name = 'file'

    def post(self, request, problem_id):

        context = {}
        
        user = request.user
        file = request.FILES.get(self.file_name)

        if file == None:
            messages.warning(request, "File not provided!!")
            return redirect('/problems/{}'.format(problem_id))

        verdict = do_magic(file, user, problem_id)
        print(verdict)

        return JsonResponse(data=json.dumps({"message":"Success", "data":verdict}), safe=False)

        return render(request, self.result_template, context)
