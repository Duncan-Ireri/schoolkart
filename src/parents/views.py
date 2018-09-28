from django.shortcuts import render
# from django.views.generic import TemplateView


# class ParentView(TemplateView):
#     template_name = 'parent/parent.html'

def parents_list(request):
	return render(request, 'parent/parent.html')