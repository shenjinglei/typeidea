from django.shortcuts import redirect
from django.views.generic import TemplateView

from comment.forms import CommentForm


class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        comment_form = CommentForm(request.POST)
        #comment_form = CommentForm({'nickname':'jerry','website':'https://www.cnblogs.com/hjy123/p/12957489.html','email':'shen@com','content':'写好了写好了写好了写好了写好了写好了写好了'})
        #print(comment_form)
        # print(comment_form.data.get('nickname'))
        # print(comment_form.data.get('website'))
        # print(comment_form.data.get('email'))
        # print(comment_form.data.get('content'))
        target = request.POST.get('target')

        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False

        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
        }
        return self.render_to_response(context)