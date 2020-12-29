from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView
from strayhome.models import Pet


class PetList(ListView):
    model = Pet
    template_name = "index.html"
    # context_object_name = "pets"
    ordering = ("name", "pet_type", "-gender", "breed__name", "color__name", "age")

    def get_context_data(self, **kwargs):
        context = super(PetList, self).get_context_data(**kwargs)
        context["active_page"] = "index"
        return context

    # def post(self, request, *args, **kwargs):
    #     pet_type = self.request.POST.get("pet-type")
    #     return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        pets = self.get_queryset()

        pt = request.GET.get("pet-type")
        pg = request.GET.get("pet-gender")
        # print(pet_type, pet_gender)

        if pt:
            if pt != "A":
                pets = pets.filter(pet_type=pt)
        if pg:
            if pg != "A":
                pets = pets.filter(gender=pg)

        out_data = {"object_list": pets, "active_page": "index"}

        return render(request, self.template_name, out_data)


class PetDetail(DetailView):
    model = Pet
    template_name = "pet_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_page"] = "index"
        return context


def donate(request):
    template = loader.get_template('donate.html')
    out_data = {"active_page": "donate"}
    return HttpResponse(template.render(out_data, request))


def contact(request):
    template = loader.get_template('contact.html')
    out_data = {"active_page": "contact"}
    return HttpResponse(template.render(out_data, request))


def tech_info(request):
    template = loader.get_template('tech_info.html')
    out_data = {"active_page": "tech_info"}
    return HttpResponse(template.render(out_data, request))
