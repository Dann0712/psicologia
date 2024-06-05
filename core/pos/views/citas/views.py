import json
from django.http import HttpResponse
#from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, TemplateView
from core.pos.forms import CitaForm
from core.pos.models import Cita
from core.security.mixins import GroupPermissionMixin

MODULE_NAME = 'Citas'

class CitaListView(GroupPermissionMixin, TemplateView):
    template_name = 'cita/list.html'
    permission_required = 'view_cita'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'search':
                data = []
                for i in Cita.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Citas'
        context['list_url'] = reverse_lazy('cita_list')
        context['create_url'] = reverse_lazy('cita_create')
        context['module_name'] = MODULE_NAME
        return context

class CitaCreateView(GroupPermissionMixin, CreateView):
    template_name = 'cita/create.html'
    model = Cita
    form_class = CitaForm
    success_url = reverse_lazy('cita_list')
    permission_required = 'add_cita'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nueva Cita'
        context['action'] = 'add'
        context['module_name'] = MODULE_NAME
        return context

class CitaUpdateView(GroupPermissionMixin, UpdateView):
    template_name = 'cita/create.html'
    model = Cita
    form_class = CitaForm
    success_url = reverse_lazy('cita_list')
    permission_required = 'change_cita'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'edit':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Edición de Cita'
        context['action'] = 'edit'
        context['module_name'] = MODULE_NAME
        return context

class CitaDeleteView(GroupPermissionMixin, DeleteView):
    model = Cita
    template_name = 'delete.html'
    success_url = reverse_lazy('cita_list')
    permission_required = 'delete_cita'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Cita'
        context['list_url'] = self.success_url
        context['module_name'] = MODULE_NAME
        return context
