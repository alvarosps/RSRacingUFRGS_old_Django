function dialog_em_desenvolvimento() {
    var box = bootbox.alert('Funcionalidade em desenvolvimento.');
    box.find(".btn-primary").removeClass("btn-primary").addClass("btn-danger");
    box;
}

function dialog_provas(prova){
	if(prova == "estaticas"){
		var box = bootbox.alert("<h3 style='text-align: center'>Provas Estáticas</h3>" +
				"<div style='text-align: justify'>" +
				"	<p>As provas estáticas avaliam o projeto do veículo sob o ponto de vista de engenharia e também do mercado. As equipes precisam justificar o projeto de cada componente do veículo para juízes que são do ramo automobilístico. Além disso, é feito um levantamento de custos e manufatura e também uma apresentação de negócios visando a uma produção em massa do protótipo.</p>" +
				"	<p>Cada carro é submetido à uma rigorosa inspeção técnica para verificar se a construção e projeto do carro está conforme o regulamento da competição, apenas após esta inspeção ele é liberado para ir para a pista participar das provas dinâmicas.</p>" +
				"</div>")
	}
	else if(prova == "dinamicas"){
		var box = bootbox.alert("<script type='text/javascript'>" +
				"	$('#texto_skip_pad').css('display', 'none');" +
				"	$('#texto_aceleracao').css('display', 'none');" +
				"	$('#texto_autocross').css('display', 'none');" +
				"	$('#texto_enduro').css('display', 'none');" +
				"	$('#esconde_detalhes').on('click', function(){" +
				"						$('#texto_skip_pad').css('display', 'none');" +
				"						$('#texto_aceleracao').css('display', 'none');" +
				"						$('#texto_autocross').css('display', 'none');" +
				"						$('#texto_enduro').css('display', 'none');" +
				"					});" +
				"	$('#skip_pad').on('click', function(){" +
				"						$('#texto_skip_pad').css('display', 'block');" +
				"						$('#texto_aceleracao').css('display', 'none');" +
				"						$('#texto_autocross').css('display', 'none');" +
				"						$('#texto_enduro').css('display', 'none');" +
				"					});" +
				"	$('#aceleracao').on('click', function(){" +
				"						$('#texto_skip_pad').css('display', 'none');" +
				"						$('#texto_aceleracao').css('display', 'block');" +
				"						$('#texto_autocross').css('display', 'none');" +
				"						$('#texto_enduro').css('display', 'none');" +
				"					});" +
				"	$('#autocross').on('click', function(){" +
				"						$('#texto_skip_pad').css('display', 'none');" +
				"						$('#texto_aceleracao').css('display', 'none');" +
				"						$('#texto_autocross').css('display', 'block');" +
				"						$('#texto_enduro').css('display', 'none');" +
				"					});" +
				"	$('#enduro').on('click', function(){" +
				"						$('#texto_skip_pad').css('display', 'none');" +
				"						$('#texto_aceleracao').css('display', 'none');" +
				"						$('#texto_autocross').css('display', 'none');" +
				"						$('#texto_enduro').css('display', 'block');" +
				"					});" +
				"</script>" +
				"<h3 style='text-align:center'>Provas Dinâmicas</h3>" +
				"<div id='tipos_provas'>" +
				"	<p>As provas dinâmicas são divididas nas quatro seguintes etapas:</p>" +
				"	<h6 id='esconde_detalhes' style='text-align:center'>(Clique em cada uma para detalhes, clique aqui para esconder os detalhes.)</h6>" +
				"	<ul>" +
				"		<li id='skip_pad'>Skip Pad</li>" +
				"		<li id='aceleracao'>Aceleração</li>" +
				"		<li id='autocross'>AutoCross</li>" +
				"		<li id='enduro'>Enduro</li>" +
				"	</ul>" +
				"</div>" +
				"<div id='texto_skip_pad'>" +
				"	<h4 style='text-align: center'>Skip Pad</h4>" +
				"	<p style='text-align: center'>No Skip Pad o carro deve percorrer um trajeto em forma de '8' para testar o desempenho e estabilidade em curvas.</p>" +
				"	<div class='jumbotron'>" +
				"		<object>" +
				"			<param name='movieskippad' value='https://www.youtube.com/watch?v=3xgkIQhRfII'></param>" +
				"			<param name='allowFullScreen' value='true'></param>" +
				"			<param name='allowscriptaccess' value='always'></param>" +
				"			<iframe width='300' height='200' src='https://www.youtube.com/embed/3xgkIQhRfII' frameborder='0' allowfullscreen></iframe>" +
				"		</object>" +
				"	</div>" +
				"</div>" +
				"<div id='texto_aceleracao'>" +
				"	<h4 style='text-align: center'>Aceleração</h4>" +
				"	<p style='text-align: center'>As provas de Aceleração consistem em uma simples reta de 75m, feita com o pé no fundo no acelerador. Elas medem, como facilmente dá para ter ideia, a aceleração e velocidade final do veículo.</p>" +
				"	<div class='jumbotron'>" +
				"		<object>" +
				"			<param name='movieaceleracao' value='https://www.youtube.com/watch?v=z9tx-2oYsDc'></param>" +
				"			<param name='allowFullScreen' value='true'></param>" +
				"			<param name='allowscriptaccess' value='always'></param>" +
				"			<iframe width='300' height='200' src='https://www.youtube.com/embed/z9tx-2oYsDc' frameborder='0' allowfullscreen></iframe>" +
				"		</object>" +
				"	</div>" +
				"</div>" +
				"<div id='texto_autocross'>" +
				"	<h4 style='text-align: center'>AutoCross</h4>" +
				"	<p style='text-align: center'>O AutoCross é um trajeto de 1km com uma pista de largura de três metros que tem como ideia simplesmente ver qual é o carro mais rápido.</p>" +
				"	<div class='jumbotron'>" +
				"		<object>" +
				"			<param name='movieautocross' value='https://www.youtube.com/watch?v=6z8yVhfVjqU'></param>" +
				"			<param name='allowFullScreen' value='true'></param>" +
				"			<param name='allowscriptaccess' value='always'></param>" +
				"			<iframe width='300' height='200' src='https://www.youtube.com/embed/6z8yVhfVjqU' frameborder='0' allowfullscreen></iframe>" +
				"		</object>" +
				"	</div>" +
				"</div>" +
				"<div id='texto_enduro'>" +
				"	<h4 style='text-align: center'>Enduro</h4>" +
				"	<p style='text-align: center'>O Enduro, última etapa da competição, consiste em uma pista de 22km de distância para testar a resistência e economia de combústivel de cada carro. Aqui só os fortes sobrevivem.</p>" +
				"	<div class='jumbotron'>" +
				"		<object>" +
				"			<param name='movieenduro' value='https://www.youtube.com/watch?v=CCZLuIpuhOg'></param>" +
				"			<param name='allowFullScreen' value='true'></param>" +
				"			<param name='allowscriptaccess' value='always'></param>" +
				"			<iframe width='300' height='200' src='https://www.youtube.com/embed/CCZLuIpuhOg' frameborder='0' allowfullscreen></iframe>" +
				"		</object>" +
				"	</div>" +
				"</div>")
	}
	box.find(".btn-primary").removeClass("btn-primary").addClass("btn-danger");
    box;
}

function dialog_prototipos(prototipo){
	if(prototipo == "rs01"){
		var box = bootbox.alert("<h3 style='text-align: center'> Protótipo 2011 - RS#01</h3>" +
				"<ul>" +
				"	<li><h4>Descrição Técnica</h4></li>" +
				"	<ul>" +
				"		<li>Motor CB 400 Carburado, Traseiro</li>" +
				"		<li>Refrigeração a ar</li>" +
				"	</ul>" +
				"</ul>")
	}
	else if(prototipo == "rs02"){
		var box = bootbox.alert("<h3 style='text-align: center'> Protótipo 2012 - RS#02</h3>" +
				"<ul>" +
				"	<li><h4>Descrição Técnica</h4></li>" +
				"	<ul>" +
				"		<li>Motor GAS-GAS 450, Lateral</li>" +
				"		<li>Refrigeração a água</li>" +
				"		<li>Injeção Eletrônica Protune PR330" +
				"	</ul>" +
				"</ul>")
	}
	else if(prototipo == "rs03"){
		var box = bootbox.alert("<h3 style='text-align: center'> Protótipo 2013 - RS#03</h3>" +
				"<ul>" +
				"	<li><h4>Descrição Técnica</h4></li>" +
				"	<ul>" +
				"		<li>Motor GAS-GAS 450, Lateral</li>" +
				"		<li>Refrigeração a água</li>" +
				"		<li>Injeção Eletrônica Protune PR330" +
				"	</ul>" +
				"</ul>")
	}
	else if(prototipo == "bagual"){
		var box = bootbox.alert("<h3 style='text-align: center'>Protótipo 2015 - Bagual</h3>" +
				"<ul>" +
				"	<li><h4>Conquistas</h4></li>" +
				"</ul>" +
				"<div style='padding-left:50px'>" +
				"	<h4>Fórmula SAE Brasil 2015</h4>" +
				"	<ul>" +
				"		<li>2º Lugar Geral</li>" +
				"		<li>1º Lugar no Enduro</li>" +
				"		<li>1º Lugar na Economia de Combustível</li>" +
				"		<li>2º Lugar na prova de Custos</li>" +
				"		<li>3º Lugar na apresentação do Business Case</li>" +
				"	</ul>" +
				"</div>" +
				"<ul>" +
				"	<li><h4>Descrição Técnica</h4></li>" +
				"	<ul>" +
				"		<li>Peso: 232kg</li>" +
				"		<li>Potência: 29hp</li>" +
				"		<li>Torque: 30Nm</li>" +
				"		<li>Força G: 1,4g </li>" +
				"	</ul>" +
				"	<li><h4>Provas Dinâmicas</h4></li>" +
				"	<ul>" +
				"		<li>Tempo da prova de aceleração: 5,4s</li>" +
				"		<li>Tempo da prova Enduro: 2059,4s</li>" +
				"		<li>Tempo da prova Skip Pad: 5,34s</li>" +
				"		<li>Tempo da prova Autocross: 82,3s</li>" +
				"	</ul>" +
				"	<li><h4>Prova Estáticas</h4></li>" +
				"	<ul>" +
				"		<li>Design: 51,75 pontos</li>" +
				"		<li>Custos: 71,00 pontos</li>" +
				"		<li>Business Presentation: 70,11 pontos</li>" +
				"	</ul>" +
				"</ul>")
	}
	else if(prototipo == "minuano"){
		var box = bootbox.alert("<h3 style='text-align: center'>Protótipo 2016 - Minuano</h3>" +
				"<ul>" +
				"	<li><h4>Conquistas</h4></li>" +
				"</ul>" +
				"<div style='padding-left:50px'>" +
				"	<h4>Fórmula SAE Brasil 2016</h4>" +
				"	<ul>" +
				"		<li>2º Lugar na apresentação do Business Case</li>" +
				"	</ul>" +
				"</div>" +
				"<ul>" +
				"	<li><h4>Descrição Técnica</h4></li>" +
				"	<ul>" +
				"		<li>Peso: 218kg</li>" +
				"		<li>Potência: 25hp</li>" +
				"		<li>Torque: 26,4Nm</li>" +
				"		<li>Força G: 1,6g </li>" +
				"	</ul>" +
				"	<li><h4>Provas Dinâmicas</h4></li>" +
				"	<ul>" +
				"		<li>Tempo da prova de aceleração: 5,7s</li>" +
				"		<li>Tempo da prova Enduro: -s</li>" +
				"		<li>Tempo da prova Skip Pad: 5,94s</li>" +
				"		<li>Tempo da prova Autocross: 90,51s</li>" +
				"	</ul>" +
				"	<li><h4>Prova Estáticas</h4></li>" +
				"	<ul>" +
				"		<li>Design: 79,45 pontos</li>" +
				"		<li>Custos: 26,00 pontos</li>" +
				"		<li>Business Presentation: 70,26 pontos</li>" +
				"	</ul>" +
				"</ul>")
	}
	box.find(".btn-primary").removeClass("btn-primary").addClass("btn-danger");
    box;
}



function dialog_bagual(){
	var box = bootbox.alert("<h3 style='text-align: center'>Protótipo 2015 - Bagual</h3>" +
							"<ul>" +
							"	<li><h4>Conquistas</h4></li>" +
							"</ul>" +
							"<div style='padding-left:50px'>" +
							"	<h4>Fórmula SAE Brasil 2015</h4>" +
							"	<ul>" +
							"		<li>2º Lugar Geral</li>" +
							"		<li>1º Lugar no Enduro</li>" +
							"		<li>1º Lugar na Economia de Combustível</li>" +
							"		<li>2º Lugar na prova de Custos</li>" +
							"		<li>3º Lugar na apresentação do Business Case</li>" +
							"	</ul>" +
							"</div>" +
							"<ul>" +
							"	<li><h4>Descrição Técnica</h4></li>" +
							"	<ul>" +
							"		<li>Peso: 232kg</li>" +
							"		<li>Potência: 29hp</li>" +
							"		<li>Torque: 30Nm</li>" +
							"		<li>Força G: 1,4g </li>" +
							"	</ul>" +
							"	<li><h4>Provas Dinâmicas</h4></li>" +
							"	<ul>" +
							"		<li>Tempo da prova de aceleração: 5,4s</li>" +
							"		<li>Tempo da prova Enduro: 2059,4s</li>" +
							"		<li>Tempo da prova Skip Pad: 5,34s</li>" +
							"		<li>Tempo da prova Autocross: 82,3s</li>" +
							"	</ul>" +
							"	<li><h4>Prova Estáticas</h4></li>" +
							"	<ul>" +
							"		<li>Design: 51,75 pontos</li>" +
							"		<li>Custos: 71,00 pontos</li>" +
							"		<li>Business Presentation: 70,11 pontos</li>" +
							"	</ul>" +
							"</ul>")
	box.find(".btn-primary").removeClass("btn-primary").addClass("btn-danger");
	box;
}

function dialog_minuano(){
	var box = bootbox.alert("<h3 style='text-align: center'>Protótipo 2016 - Minuano</h3>" +
			"<ul>" +
			"	<li><h4>Conquistas</h4></li>" +
			"</ul>" +
			"<div style='padding-left:50px'>" +
			"	<h4>Fórmula SAE Brasil 2016</h4>" +
			"	<ul>" +
			"		<li>2º Lugar na apresentação do Business Case</li>" +
			"	</ul>" +
			"</div>" +
			"<ul>" +
			"	<li><h4>Descrição Técnica</h4></li>" +
			"	<ul>" +
			"		<li>Peso: 218kg</li>" +
			"		<li>Potência: 25hp</li>" +
			"		<li>Torque: 26,4Nm</li>" +
			"		<li>Força G: 1,6g </li>" +
			"	</ul>" +
			"	<li><h4>Provas Dinâmicas</h4></li>" +
			"	<ul>" +
			"		<li>Tempo da prova de aceleração: 5,7s</li>" +
			"		<li>Tempo da prova Enduro: -s</li>" +
			"		<li>Tempo da prova Skip Pad: 5,94s</li>" +
			"		<li>Tempo da prova Autocross: 90,51s</li>" +
			"	</ul>" +
			"	<li><h4>Prova Estáticas</h4></li>" +
			"	<ul>" +
			"		<li>Design: 79,45 pontos</li>" +
			"		<li>Custos: 26,00 pontos</li>" +
			"		<li>Business Presentation: 70,26 pontos</li>" +
			"	</ul>" +
			"</ul>")
	box.find(".btn-primary").removeClass("btn-primary").addClass("btn-danger");
	box;
}