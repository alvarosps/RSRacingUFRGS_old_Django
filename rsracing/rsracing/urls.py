"""rsracing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
    


from rsracing import views

urlpatterns = [
    #url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'mechg/images/favicon.ico')), #google chrome favicon fix
    
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),
    
    url(r'^time/1/$', views.escreve_tabela_equipes, name='tabelatime'),
    url(r'^patrocinadores/1/$', views.escreve_imagens_patrocinadores, name='tabelapatrocinadores'),
    #project
    url(r'^$', views.inicio, name='inicio'),
    url(r'^formulasae/$', views.sobre_formula_sae, name='formulasae'),
    url(r'^carros/$', views.carros, name='carros'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^time/$', views.time, name='time'),
    url(r'^historia/$', views.historia, name='historia'),
    url(r'^patrocinadores/$', views.patrocinadores, name='patrocinadores'),
    url(r'^sejapatrocinador/$', views.ser_patrocinador, name='serpatrocinador'),
    url(r'^juntandoseaequipe/$', views.juntando_se_a_equipe, name='juntandoseaequipe'),
    
    url(r'^js/$', views.js, name='js'),
    url(r'^js/dialog/$', views.js_dialog, name='js_dialog'),
    
    
    
    #apps
    
    #admin
    url(r'^raiz/', admin.site.urls),
]
