from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout

from .forms import CustomUserCreationForm
from .models import Comment

def register_view(request):
	form = CustomUserCreationForm()
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST or None)
		if form.is_valid():
			user = form.save()
			# username = form.cleaned_data.get('username')
			# messages.success(request, f"Account successfully created for {username}!")
			return redirect('login')
		
	context = {'form': form}
	if request.user.is_authenticated:
		return redirect('comment')
	return render(request, 'registration/register.html', context)


def logout_view(request):
	logout(request)
	return render(request, "registration/logout.html")


@login_required
def comment_view(request):
	comments = Comment.objects.all()
	context = {}
	if request.method == "POST":
		name = request.POST.get("name")
		text = request.POST.get("text")

		comment = Comment(user=request.user, name=name, text=text)
		comment.save()

		messages.success(request, "Comment posted successfully!")
		return render(request, "comment.html")

	# render comments
	context["comments"] = comments
	return render(request, "comment.html", context)


