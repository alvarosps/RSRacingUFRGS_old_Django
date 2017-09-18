#coding: utf-8
#from rsracingufrgs.forms import ContactForm
from rsracingufrgs.base_membros_sql import retorna_membros
from rsracingufrgs.base_patrocinadores import retorna_patrocinadores

from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


import json


def render_pagina(request, destino):
    c = {}
    c.update(csrf(request))
    return render(request, destino, c)

def inicio(request):
    return render_pagina(request, 'rsracingufrgs/inicio.html')

def sobre_formula_sae(request):
    return render_pagina(request, 'rsracingufrgs/sobre.html')

def carros(request):
    return render_pagina(request, 'rsracingufrgs/carros.html')

def time(request):
    return render_pagina(request, 'rsracingufrgs/time.html')

def historia(request):
    return render_pagina(request, 'rsracingufrgs/historia.html')

def patrocinadores(request):
    return render_pagina(request, 'rsracingufrgs/patrocinadores.html')

def ser_patrocinador(request):
    return render_pagina(request, 'rsracingufrgs/serpatrocinador.html')

def juntando_se_a_equipe(request):
    return render_pagina(request, 'rsracingufrgs/entrarnaequipe.html')
def contato(request):
    return render_pagina(request, 'rsracingufrgs/contato.html')
'''def contato(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'Nome'
            , '')
            contact_email = request.POST.get(
                'Email'
            , '')
            contact_subject = request.POST.get(
                'Assunto'
            , '')
            form_content = request.POST.get('Mensagem', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contato')

    return render(request, 'rsracingufrgs/contato.html', {
        'form': form_class,
    })
'''
def js(request):
    return render_pagina(request, 'rsracingufrgs/js/js.js')

def js_dialog(request):
    return render_pagina(request, 'rsracingufrgs/js/js_dialog.js')


'''def cadastro(request):
    if not request.user.is_authenticated():
        cadastro_modelo = UserInfo()
        cadastro_form = FormUserInfo(instance=cadastro_modelo)
        
        fields_login_info = ['username', 'password', 'password_conf', 'email']
        fields_user_info = ['nome', 'instituicao', 'setor', 'cidade', 'estado']
        
        c = {
             'cadastro_form': cadastro_form,
             'fields_login_info': fields_login_info,
             'fields_user_info': fields_user_info,
             }
        
        c.update(csrf(request))
        return render(request, 'mechg/cadastro.html', c)
    else:
        return HttpResponseRedirect('/./')
    
    
def cadastrar_usuario(request):
    request_body = json.loads(request.body)
    
    form = FormUserInfo(request_body)
    data = form.data
    
    if form.is_valid():
        user = UserInfo.objects.create_user(data['username'], data['email'], data['password'])
        user.nome = data['nome']
        user.instituicao = data['instituicao']
        user.setor = data['setor']
        user.cidade = data['cidade']
        user.estado=data['estado']
        user.save()
        cadastro_ok = 1
        
        #send_email_confirmacao(data['email'])
        response = {'cadastro_ok':cadastro_ok}
    else:
        response = {'errors':form.errors, 'non_field_errors':form.non_field_errors()}
    
    return HttpResponse(json.dumps(response), content_type="application/json")'''


def organizar_times(membros):
    #Pega o dicionario de membros e organiza em equipes para montar a tabela da pagina "Time"
    equipes = {
                    'aerodinamica' : {
                                            'lider' : [],
                                            'membros' : [],
                                      },
                    'capitao' : [],
                    'chassi' : {
                                            'lider' : [],
                                            'membros' : [],
                                      },
                    'drivetrain' : {
                                            'lider' : [],
                                            'membros' : [],
                                      },
                    'eletronica' : {
                                            'lider' : [],
                                            'membros' : [],
                                      },
                    'gestao' : {
                                            'lider' : [],
                                            'membros' : [],
                                      },
                    'marketing' : {
                                            'lider' : [],
                                            'membros' : [],
                                      },
                    'powertrain' : {
                                            'lider' : [],
                                            'membros' : [],
                                      },
                    'suspensao' : {
                                            'lider' : [],
                                            'membros' : [],
                                      },
    }
    
    for i in range(len(membros)):
        membro = membros[i]
        equipe = membro['equipe']
        marketing = membro['eh_marketing']
        gestao_sec = membro['gestao_equipe_secundaria']
        if equipe == 0:
            equipes['capitao'].append(membro)
        elif equipe == 1:
            equipes['eletronica']['membros'].append(membro)
        elif equipe == 2:
            equipes['powertrain']['membros'].append(membro)
        elif equipe == 3:
            equipes['drivetrain']['membros'].append(membro)
        elif equipe == 4:
            equipes['suspensao']['membros'].append(membro)
        elif equipe == 5:
            equipes['chassi']['membros'].append(membro)
        elif equipe == 6:
            equipes['aerodinamica']['membros'].append(membro)
        elif equipe == 7:
            equipes['gestao']['membros'].append(membro)
        if marketing == 1:
            equipes['marketing']['membros'].append(membro)
        if gestao_sec == 1:
            equipes['gestao']['membros'].append(membro)
    for equipe in equipes:
        if equipe != "marketing" and equipe != "capitao":
            membros_equipe = equipes[equipe]['membros']
            for i in range(len(membros_equipe)):
                lider = membros_equipe[i]['eh_lider']
                if lider == 1:
                    equipes[equipe]['lider'].append(membros_equipe[i])
                    equipes[equipe]['membros'].remove(membros_equipe[i])
                    break
        if equipe == "marketing":
            membros_equipe = equipes[equipe]['membros']
            for i in range(len(membros_equipe)):
                lider = membros_equipe[i]['eh_lider_marketing']
                if lider == 1:
                    equipes[equipe]['lider'].append(membros_equipe[i])
                    equipes[equipe]['membros'].remove(membros_equipe[i])
                    break
    
    #Deixar os membros em ordem alfabetica
    equipes["aerodinamica"]['membros'] = sorted(equipes["aerodinamica"]['membros'], key=lambda k: k['nome'])
    equipes['chassi']['membros'] = sorted(equipes['chassi']['membros'], key=lambda k: k['nome'])
    equipes['drivetrain']['membros'] = sorted(equipes['drivetrain']['membros'], key=lambda k: k['nome'])
    equipes['eletronica']['membros'] = sorted(equipes['eletronica']['membros'], key=lambda k: k['nome'])
    equipes['gestao']['membros'] = sorted(equipes['gestao']['membros'], key=lambda k: k['nome'])
    equipes['marketing']['membros'] = sorted(equipes['marketing']['membros'], key=lambda k: k['nome'])
    equipes['powertrain']['membros'] = sorted(equipes['powertrain']['membros'], key=lambda k: k['nome'])
    equipes['suspensao']['membros'] = sorted(equipes['suspensao']['membros'], key=lambda k: k['nome'])
    
    return equipes  #Dicionario com as equipes relacionadas

def escreve_tabela_equipes(request):
    #Recebe os dados dos membros do DB específico, organiza por equipes e cria o codigo de exibicao HTML
    membros = retorna_membros()
    equipes = organizar_times(membros)
    html_code = "\t<div id='tabela_equipes' class='container-fluid'>\n"

    #Organizacao de cada lista de membros de cada equipe
    #equipe = [lider, membro1, membro2, ...] (membros ja estao em ordem alfabetica)

    aerodinamica = list()
    aerodinamica.append(equipes['aerodinamica']['lider'])
    for i in range(len(equipes['aerodinamica']['membros'])):
        aerodinamica.append(equipes['aerodinamica']['membros'][i])

    capitao = equipes['capitao'][0]

    chassi = list()
    chassi.append(equipes['chassi']['lider'])
    for i in range(len(equipes['chassi']['membros'])):
        chassi.append(equipes['chassi']['membros'][i])

    drivetrain = list()
    drivetrain.append(equipes['drivetrain']['lider'])
    for i in range(len(equipes['drivetrain']['membros'])):
        drivetrain.append(equipes['drivetrain']['membros'][i])

    eletronica = list()
    eletronica.append(equipes['eletronica']['lider'])
    for i in range(len(equipes['eletronica']['membros'])):
        eletronica.append(equipes['eletronica']['membros'][i])

    gestao = list()
    gestao.append(equipes['gestao']['lider'])
    for i in range(len(equipes['gestao']['membros'])):
        gestao.append(equipes['gestao']['membros'][i])

    marketing = list()
    marketing.append(equipes['marketing']['lider'])
    for i in range(len(equipes['marketing']['membros'])):
        marketing.append(equipes['marketing']['membros'][i])

    powertrain = list()
    powertrain.append(equipes['powertrain']['lider'])
    for i in range(len(equipes['powertrain']['membros'])):
        powertrain.append(equipes['powertrain']['membros'][i])

    suspensao = list()
    suspensao.append(equipes['suspensao']['lider'])
    for i in range(len(equipes['suspensao']['membros'])):
        suspensao.append(equipes['suspensao']['membros'][i])

    #Capitao
    html_capitao = "\t\t<div class='membro_individual' id='capitao'>\n"
    html_capitao += "\t\t\t<span class='nome_equipe'><h3>Capitão</h3></span>\n"
    html_capitao += "\t\t\t<div class='imgWrap>\n"
    html_capitao += ("\t\t\t\t<img class='img_membros' src='/static/images/membros/" + capitao['imagem'] + "' alt='" + capitao['nome'] + "' style='cursor: pointer;'>\n")
    html_capitao += ("\t\t\t\t<p class='imgDescription'><b>" + capitao['curso'] + "<br>" + capitao['email'] + "</b></p>\n")
    html_capitao += "\t\t\t</div>\n"
    html_capitao += ("\t\t\t<span class='nome_membro><b>" + capitao['nome'] + "</b></span>")
    html_capitao += "\t\t</div>"

    html_code += html_capitao
    html_code += "\n"

    html_code += "\t</div>\n"

    retorno = {
                    'html' : html_code,
    }
    #return response
    return HttpResponse(json.dumps(retorno), content_type = 'application/json')

'''
def escreve_tabela_equipes(request):
    membros = retorna_membros()
    equipes = organizar_times(membros)
    html = ""
    
    #Capitao, depois Equipes em ordem alfabetica
    
    #Capitao
    html += "<table id='tab_capitao'>\n"
    html += ""
    html += "\t<tr>\n"
    html += "\t\t<th><h3>Capitão</h3></th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap'>\n"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['capitao'][0]['imagem'] + "' alt='" + equipes['capitao'][0]['nome'] + "' >\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['capitao'][0]['curso'] + "<br>" + equipes['capitao'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><b>" + equipes['capitao'][0]['nome'] + "</b></td>\n"
    html += "\t</tr>\n"
    html += "</table>\n"
    
    html += "<hr>\n"
    
    #Aerodinamica
    html += "<h3 class='nome_equipe'>Aerodinâmica</h3>"
    html += "<table>\n"
    html += "\t<tr>\n"
    html += "\t\t<th>Líder</th>\n"
    
    membros = equipes['aerodinamica']['membros']
    num_membros = len(membros)
    
    for i in range(num_membros):
        html += "\t\t<th> </th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap'>"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['aerodinamica']['lider'][0]['imagem'] + "' alt='" + equipes['aerodinamica']['lider'][0]['nome'] + "'>\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['aerodinamica']['lider'][0]['curso'] + "<br>" + equipes['aerodinamica']['lider'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>\n"
    for i in range(num_membros):
        html += "\t\t<td><div class='imgWrap'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['aerodinamica']['membros'][i]['imagem'] + "' alt='" + equipes['aerodinamica']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['aerodinamica']['membros'][i]['curso'] + "<br>" + equipes['aerodinamica']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += ("\t\t<td><b>" + equipes['aerodinamica']['lider'][0]['nome'] + "</b></td>\n") 
    for i in range(num_membros):
        html += ("\t\t<td><b>" + equipes['aerodinamica']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr>\n"
    html += "</table>"
    
    html += "<hr>\n"
    
    #Chassi
    html += "<h3 class='nome_equipe'>Chassi</h3>"
    html += "<table>\n"
    html += "\t<tr>\n"
    html += "\t\t<th>Líder</th>\n"
    
    membros = equipes['chassi']['membros']
    num_membros = len(membros)
    
    for i in range(num_membros):
        html += "\t\t<th> </th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap''>"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['chassi']['lider'][0]['imagem'] + "' alt='" + equipes['chassi']['lider'][0]['nome'] + "'>\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['chassi']['lider'][0]['curso'] + "<br>" + equipes['chassi']['lider'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>\n"
    for i in range(num_membros):
        html += "\t\t<td><div class='imgWrap'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['chassi']['membros'][i]['imagem'] + "' alt='" + equipes['chassi']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['chassi']['membros'][i]['curso'] + "<br>" + equipes['chassi']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += ("\t\t<td><b>" + equipes['chassi']['lider'][0]['nome'] + "</b></td>\n") 
    for i in range(num_membros):
        html += ("\t\t<td><b>" + equipes['chassi']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr>\n"
    html += "</table>"
    
    html += "<hr>\n"
    
    #Drivetrain
    html += "<h3 class='nome_equipe'>Drivetrain</h3>"
    html += "<table>\n"
    html += "\t<tr>\n"
    html += "\t\t<th>Líder</th>\n"
    
    membros = equipes['drivetrain']['membros']
    num_membros = len(membros)
    
    for i in range(num_membros):
        html += "\t\t<th> </th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap'>"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['drivetrain']['lider'][0]['imagem'] + "' alt='" + equipes['drivetrain']['lider'][0]['nome'] + "'>\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['drivetrain']['lider'][0]['curso'] + "<br>" + equipes['drivetrain']['lider'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>\n"
    for i in range(num_membros):
        html += "\t\t<td><div class='imgWrap'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['drivetrain']['membros'][i]['imagem'] + "' alt='" + equipes['drivetrain']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['drivetrain']['membros'][i]['curso'] + "<br>" + equipes['drivetrain']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += ("\t\t<td><b>" + equipes['drivetrain']['lider'][0]['nome'] + "</b></td>\n") 
    for i in range(num_membros):
        html += ("\t\t<td><b>" + equipes['drivetrain']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr>\n"
    html += "</table>"
    
    html += "<hr>\n"
    
    #Eletronica
    html += "<h3 class='nome_equipe'>Eletrônica</h3>"
    html += "<table>\n"
    html += "\t<tr>\n"
    html += "\t\t<th>Líder</th>\n"
    
    membros = equipes['eletronica']['membros']
    num_membros = len(membros)
    
    for i in range(0,3):
        html += "\t\t<th> </th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap' style='width: 205px;'>"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['eletronica']['lider'][0]['imagem'] + "' alt='" + equipes['eletronica']['lider'][0]['nome'] + "'>\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['eletronica']['lider'][0]['curso'] + "<br>" + equipes['eletronica']['lider'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>\n"
    #Adicionar os 4 primeiros na primeira linha
    for i in range(0,3):    
        html += "\t\t<td><div class='imgWrap' style='width: 205px;'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['eletronica']['membros'][i]['imagem'] + "' alt='" + equipes['eletronica']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['eletronica']['membros'][i]['curso'] + "<br>" + equipes['marketing']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += ("\t\t<td><b>" + equipes['eletronica']['lider'][0]['nome'] + "</b></td>\n") 
    for i in range(0,3):
        html += ("\t\t<td><b>" + equipes['eletronica']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr><tr>\n"
    for i in range(3, num_membros):    
        html += "\t\t<td><div class='imgWrap' style='padding-top: 10px;'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['eletronica']['membros'][i]['imagem'] + "' alt='" + equipes['eletronica']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['eletronica']['membros'][i]['curso'] + "<br>" + equipes['eletronica']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    for i in range(3, num_membros):
        html += ("\t\t<td><b>" + equipes['eletronica']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr>\n"
    html += "</table>"
    
    html += "<hr>\n"
    
    #Gestao
    html += "<h3 class='nome_equipe'>Gestão</h3>"
    html += "<table>\n"
    html += "\t<tr>\n"
    html += "\t\t<th>Líder</th>\n"
    
    membros = equipes['gestao']['membros']
    num_membros = len(membros)
    
    for i in range(num_membros + 1):
        html += "\t\t<th> </th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap'>"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['gestao']['lider'][0]['imagem'] + "' alt='" + equipes['gestao']['lider'][0]['nome'] + "'>\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['gestao']['lider'][0]['curso'] + "<br>" + equipes['gestao']['lider'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>\n"
    for i in range(num_membros):
        html += "\t\t<td><div class='imgWrap'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['gestao']['membros'][i]['imagem'] + "' alt='" + equipes['gestao']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['gestao']['membros'][i]['curso'] + "<br>" + equipes['gestao']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += ("\t\t<td><b>" + equipes['gestao']['lider'][0]['nome'] + "</b></td>\n") 
    for i in range(num_membros):
        html += ("\t\t<td><b>" + equipes['gestao']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr>\n"
    html += "</table>"
    
    html += "<hr>\n"
    
    #Marketing
    html += "<h3 class='nome_equipe'>Marketing</h3>"
    html += "<table>\n"
    html += "\t<tr>\n"
    html += "\t\t<th>Líder</th>\n"
    
    membros = equipes['marketing']['membros']
    num_membros = len(membros)
    
    
    for i in range(0,3):
        html += "\t\t<th> </th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap' style='width:205px'>"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['marketing']['lider'][0]['imagem'] + "' alt='" + equipes['marketing']['lider'][0]['nome'] + "'>\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['marketing']['lider'][0]['curso'] + "<br>" + equipes['marketing']['lider'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>\n"
    #Adicionar os 4 primeiros na primeira linha
    for i in range(0,3):    
        html += "\t\t<td><div class='imgWrap' style='width:205px;'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['marketing']['membros'][i]['imagem'] + "' alt='" + equipes['marketing']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['marketing']['membros'][i]['curso'] + "<br>" + equipes['marketing']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += ("\t\t<td><b>" + equipes['marketing']['lider'][0]['nome'] + "</b></td>\n") 
    for i in range(0,3):
        html += ("\t\t<td><b>" + equipes['marketing']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr><tr>\n"
    for i in range(3, num_membros):    
        html += "\t\t<td><div class='imgWrap' style='padding-top: 10px; width:205px;'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['marketing']['membros'][i]['imagem'] + "' alt='" + equipes['marketing']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['marketing']['membros'][i]['curso'] + "<br>" + equipes['marketing']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    for i in range(3, num_membros):
        html += ("\t\t<td><b>" + equipes['marketing']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr>\n"
    html += "</table>"
    
    html += "<hr>\n"
    
    #Powertrain
    html += "<h3 class='nome_equipe'>Powertrain</h3>"
    html += "<table>\n"
    html += "\t<tr>\n"
    html += "\t\t<th>Líder</th>\n"
    
    membros = equipes['powertrain']['membros']
    num_membros = len(membros)
    
    for i in range(0,3):
        html += "\t\t<th> </th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap'>"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['powertrain']['lider'][0]['imagem'] + "' alt='" + equipes['powertrain']['lider'][0]['nome'] + "'>\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['powertrain']['lider'][0]['curso'] + "<br>" + equipes['powertrain']['lider'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>\n"
    #Adicionar os 4 primeiros na primeira linha
    for i in range(0,3):    
        html += "\t\t<td><div class='imgWrap''>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['powertrain']['membros'][i]['imagem'] + "' alt='" + equipes['powertrain']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['powertrain']['membros'][i]['curso'] + "<br>" + equipes['powertrain']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += ("\t\t<td><b>" + equipes['powertrain']['lider'][0]['nome'] + "</b></td>\n") 
    for i in range(0,3):
        html += ("\t\t<td><b>" + equipes['powertrain']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr><tr>\n"
    for i in range(3, num_membros):    
        html += "\t\t<td><div class='imgWrap' style='padding-top: 10px;'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['powertrain']['membros'][i]['imagem'] + "' alt='" + equipes['powertrain']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['powertrain']['membros'][i]['curso'] + "<br>" + equipes['powertrain']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    for i in range(3, num_membros):
        html += ("\t\t<td><b>" + equipes['powertrain']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr>\n"
    html += "</table>"
    
    html += "<hr>\n"
    
    #Suspensao
    html += "<h3 class='nome_equipe'>Suspensão</h3>"
    html += "<table>\n"
    html += "\t<tr>\n"
    html += "\t\t<th>Líder</th>\n"
    
    membros = equipes['suspensao']['membros']
    num_membros = len(membros)
    
    for i in range(0,3):
        html += "\t\t<th> </th>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += "\t\t<td><div class='imgWrap'>"
    html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['suspensao']['lider'][0]['imagem'] + "' alt='" + equipes['suspensao']['lider'][0]['nome'] + "'>\n")
    html += ("\t\t\t<p class='imgDescription'><b>" + equipes['suspensao']['lider'][0]['curso'] + "<br>" + equipes['suspensao']['lider'][0]['email'] + "</b></p>\n")
    html += "\t\t</div></td>\n"
    #Adicionar os 4 primeiros na primeira linha
    for i in range(0,3):    
        html += "\t\t<td><div class='imgWrap''>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['suspensao']['membros'][i]['imagem'] + "' alt='" + equipes['suspensao']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['suspensao']['membros'][i]['curso'] + "<br>" + equipes['suspensao']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    html += ("\t\t<td><b>" + equipes['suspensao']['lider'][0]['nome'] + "</b></td>\n") 
    for i in range(0,3):
        html += ("\t\t<td><b>" + equipes['suspensao']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr><tr>\n"
    for i in range(3, num_membros):    
        html += "\t\t<td><div class='imgWrap' style='padding-top: 10px;'>"
        html += ("\t\t\t<img class='img_membros' src='/static/images/membros/" + equipes['suspensao']['membros'][i]['imagem'] + "' alt='" + equipes['suspensao']['membros'][i]['nome'] + "'>\n")
        html += ("\t\t\t<p class='imgDescription'><b>" + equipes['suspensao']['membros'][i]['curso'] + "<br>" + equipes['suspensao']['membros'][i]['email'] + "</b></p>\n")
        html += "\t\t</div></td>\n"
    html += "\t</tr>\n"
    html += "\t<tr>\n"
    for i in range(3, num_membros):
        html += ("\t\t<td><b>" + equipes['suspensao']['membros'][i]['nome'] + "</b></td>\n")
    html += "\t</tr>\n"
    html += "</table>"
    
    
    retorno = {
                    'html' : html,
    }
    #return response
    return HttpResponse(json.dumps(retorno), content_type = 'application/json')
'''
def escreve_imagens_patrocinadores(request):
    patrocinadores = retorna_patrocinadores()
    patrocinadores = sorted(patrocinadores, key=lambda k: k['nome'])
    
    html = ""
    
    html += "<table>\n"
    html += "\t<tr><th></th></tr>\n"
    for i in range(len(patrocinadores)):
        html += "\t<tr><td>\n"
        html += "\t\t<a href='" + patrocinadores[i]['site'] + "'" + ' target="_blank"' + "><img src='/static/images/patrocinadores/" + patrocinadores[i]['logo'] + "' alt='" + patrocinadores[i]['nome'] + "'></a>\n"
        html += "\t</td></tr>\n"
    html += "</table>"
    retorno = {
                    'html' : html,
    }
    #return response
    return HttpResponse(json.dumps(retorno), content_type = 'application/json')