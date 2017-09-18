$(document).ready(documentReady());

// Ao carregar a página, realiza os seguintes procedimentos automaticamente:
function documentReady() {
	$('.em_desenvolvimento').on('click', function(){dialog_em_desenvolvimento();});
	
	//Página "Sobre Fórmula SAE"
	if(pagina_atual_substring("/formulasae/")){
		$('#img_prova_estatica').on('click', function(){dialog_provas("estaticas");});
		$('#img_prova_dinamica').on('click', function(){dialog_provas("dinamicas");});
	}
	
	//Página "Carros"
	if(pagina_atual_substring("/carros/")){
		$('#rs01').on('click', function(){dialog_prototipos("rs01")});
		$('#rs02').on('click', function(){dialog_prototipos("rs02")});
		$('#rs03').on('click', function(){dialog_prototipos("rs03")});
		$('#bagual').on('click', function(){dialog_prototipos("bagual");});
		$('#minuano').on('click', function(){dialog_prototipos("minuano");});
	}
	
	
	//Página "Time"
	if(pagina_atual_substring("/time/")){
		tabela_time();
	}
	
	//Página "Patrocinadores"
	if(pagina_atual_substring("/patrocinadores/")){
		tabela_patrocinadores();
	}
}

// Checa se "pagina" é igual ao referer (URL sem o domínio) da página atual.
function pagina_atual(pagina) {
    return window.location.pathname == pagina;
}

//Checa se "pagina" é substring da URL da página atual.
function pagina_atual_substring(pagina) {
    return window.location.href.indexOf(pagina) > -1;
}

// Substitui as vírgulas de um string por pontos.
function replaceCommaWithDot(string) {
    if (string) {
        string = string.replace(/,/g,'.');
    }
    return string;
}

// Substitui os pontos de um string por vírgulas.
function replaceDotWithComma(string) {
    if (string) {
        string = string.replace(/./g,',');
    }
    return string;
}

function round_number(num, dec) {
    return Math.round(num * Math.pow(10, dec)) / Math.pow(10, dec);
}

function resetForm($form) {
// to call, use:
// resetForm($('#myform')); // by id, recommended
// resetForm($('form[name=myName]')); // by name
    $form.find('input:text, input:password, input:file, input[type="email"], select, textarea').val('');
    $form.find('input:radio, input:checkbox')
         .removeAttr('checked').removeAttr('selected');
}

//Limpa as mensagens de erro.
function limpa_error_msg() {
    $('.error_msg').html('');
}

function limpa_select(select_selector) {
    $(select_selector).select2('val', '');
}

function getUrlVars() {
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

function formReturnKey(event, input_text_types) {
    var text_fields = $(event.delegateTarget).find(input_text_types);
    var event_field_index = $(text_fields).index(event.target);
    var next_field_index = event_field_index + 1;
    
    if (event.keyCode == 13) {
        event.preventDefault();
        
        while ($(text_fields[next_field_index]).prop('disabled')) {
            next_field_index += 1;
        }
        
        if (next_field_index < text_fields.length) {
            $(text_fields[next_field_index]).focus();
        }
        else {
            $(event.target).submit();
            //$(text_fields[0]).focus();
            $(event.target).blur();
        }
    }
} 

function tabela_time(){
	//Cria o HTML da pagina time, e adiciona no div com id="equipe" de time.html
	$.ajax({
        type: "POST",
        url: '{% url "tabelatime" %}', //views.escreve_tabela_equipes
        data: JSON.stringify({}),
        success: function(response){
        	$('#membros').html(response.html);
        },
        beforeSend: function(jqXHR, settings) {
            jqXHR.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
        }
    });
}

function tabela_patrocinadores(){
	//Cria o HTML da pagina patrocinadores, e adiciona no div com id="patrocinadores" de patrocinadores.html
	$.ajax({
        type: "POST",
        url: '{% url "tabelapatrocinadores" %}', //views.escreve_imagens_patrocinadores
        data: JSON.stringify({}),
        success: function(response){
        	$('#patrocinadores').html(response.html);
        },
        beforeSend: function(jqXHR, settings) {
            jqXHR.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
        }
    });
}
