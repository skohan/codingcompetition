from codingcompetition.settings.base import LANGS
import json
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


from .update import update_user_score
from .utilities import do_magic
from .decorators import contest_is_over
# Create your views here.


class SubmitView(LoginRequiredMixin, View):

    submit_template = ''
    result_template = 'submission/result.html'
    file_name = 'file'

    def post(self, request, problem_id:int):

        context = {}

        user = request.user
        file = request.FILES.get(self.file_name)
        lang = request.POST.get('lang')

        # print("Language ", lang)

        if file == None or lang not in LANGS:
            return JsonResponse(data=json.dumps({
                "message":  "File not provided or language not selected!!", 
                "data": []}), safe=False)
            messages.warning(
                request, "File not provided or language not selected!!")
            return redirect('/problems/{}'.format(problem_id))

        verdict = do_magic(file, user, problem_id, lang)
        print(verdict)

        # if contest_is_over():
        #     message = "Contest is over! Your submissions will not count toward leaderboard position"
        # else:
        v = update_user_score(user, problem_id, verdict)
        message = "Success" if v else "Failure"

        return JsonResponse(data=json.dumps({"message": message, "data": verdict}), safe=False)

        return render(request, self.result_template, context)
