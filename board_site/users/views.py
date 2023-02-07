class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "board/register_user.html"
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(LoginView):
    authentication_form = AuthenticationForm
    template_name = "board/login_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def logout_user(request):
    logout(request)
    return redirect("main")
