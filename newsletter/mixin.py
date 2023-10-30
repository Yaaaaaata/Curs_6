from django.contrib import messages
from django.shortcuts import render


class AddCreatorMixin:
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.creator = request.user
            message.save()

            messages.success(request, "OK!")
            form = self.form_class()
        return render(request, self.template_name, {"form": form})


class CreatorOrManagerFilterMixin:
    def get_queryset(self):
        if not self.request.user.is_anonymous:
            q = super().get_queryset()
            if self.request.user.is_manager:
                return q
            return q.filter(creator=self.request.user)


class AddFromCreatorMixin:
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class UserOwnedMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)
