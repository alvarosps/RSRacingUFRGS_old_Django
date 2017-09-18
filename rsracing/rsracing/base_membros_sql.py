#coding: utf-8

'''
    Script para insercao dos membros da equipe no banco de dados
    Equipes:
                0 - Capitao
                1 - Eletronica
                2 - Powertrain
                3 - Drivetrain
                4 - Suspensao
                5 - Chassi
                6 - Aerodinamica
                7 - Gestao
'''
def retorna_membros():
    membros = [
                {
                    'nome' : 'Alvaro Souza Pereira da Silva',
                    'email' : 'alvaro123sps@gmail.com',
                    'imagem' : 'alvaro.png',
                    'equipe' : 1,
                    'eh_lider' : 0,
                    'eh_marketing' : 1,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia da Computação',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Gabriel Ribeiro Freitas',
                    'email' : 'gabriel.freitas@ufrgs.br',
                    'imagem' : 'freitas.png',
                    'equipe' : 1,
                    'eh_lider' : 1,
                    'eh_marketing' : 1,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia de Controle e Automação',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Artur Dieguez Backes',
                    'email' : 'arturbackes@gmail.com',
                    'imagem' : 'artur1.png',
                    'equipe' : 6,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'João Pedro Donassolo Lisboa',
                    'email' : 'joaolisboa@me.com',
                    'imagem' : 'lisboa.png',
                    'equipe' : 6,
                    'eh_lider' : 0,
                    'eh_marketing' : 1,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 1,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Renato Fensterseifer Junior',
                    'email' : 'renato.fensjr@gmail.com',
                    'imagem' : 'renato.png', 
                    'equipe' : 6,
                    'eh_lider' : 1,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Lucas Bizotto Longhi',
                    'email' : 'lucas.bizotto@yahoo.com',
                    'imagem' : 'lucasb.png',
                    'equipe' : 4,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Mateus Dandolini Pescador',
                    'email' : 'mateus.pescador@ufrgs.br',
                    'imagem' : 'pescador.png',
                    'equipe' : 5,
                    'eh_lider' : 0,
                    'eh_marketing' : 1,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Flávia Roesler Cordeiro',
                    'email' : 'froeslercordeiro@gmail.com',
                    'imagem' : 'flavia.png',
                    'equipe' : 7,
                    'eh_lider' : 1,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia de Produção',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Valter Ferreira da Silva Junior',
                    'email' : 'valterfsj@hotmail.com',
                    'imagem' : 'valter.png',    #Ainda nao enviada
                    'equipe' : 4,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Leonardo Scaravelli',
                    'email' : 'leo_scaravelli96@hotmail.com',
                    'imagem' : 'scaravelli.png',
                    'equipe' : 4,
                    'eh_lider' : 1,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Gabriel Vianna Cortez',
                    'email' : 'gabrielcortez.gvc@gmail.com',
                    'imagem' : 'cortez.png',
                    'equipe' : 1,
                    'eh_lider' : 0,
                    'eh_marketing' : 1,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Elétrica',
                    'gestao_equipe_secundaria' : 1
                },
                {
                    'nome' : 'Gabriel Motta',
                    'email' : 'gabrielrs.web@gmail.com',
                    'imagem' : 'motta.png',
                    'equipe' : 4,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Metalúrgica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Rafael Santos Netto Matias',
                    'email' : 'rafaelsantosnettomatias@gmail.com',
                    'imagem' : 'matias.png',
                    'equipe' : 0,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 1,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Tito Conrado Stoffel Efrom',
                    'email' : 'titoefrom@hotmail.com',
                    'imagem' : 'tito.png',
                    'equipe' : 4,
                    'eh_lider' : 0,
                    'eh_marketing' : 1,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : "Marcus Vinícius Dall'Agnol Signor",
                    'email' : 'marcussignor@outlook.com',
                    'imagem' : 'marcus1.png',
                    'equipe' : 4,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Gustavo Luiz Zeidler',
                    'email' : 'gustavozeidler@gmail.com',
                    'imagem' : 'gustavo1.png',
                    'equipe' : 3,
                    'eh_lider' : 1,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Leonardo Guilherme Scherer',
                    'email' : 'Leonardo.scherer@ufrgs.br',
                    'imagem' : 'leonardo1.png',
                    'equipe' : 4,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Egnaldo Neto',
                    'email' : 'egnaldo.gsneto@gmail.com',
                    'imagem' : 'egnaldo.png',
                    'equipe' : 5,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Carlos Henrique Possebon',
                    'email' : 'carlos.possebon@ufrgs.br',
                    'imagem' : 'possebon.png',
                    'equipe' : 5,
                    'eh_lider' : 1,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Alexandre Caon Biondo',
                    'email' : 'alexandrecbiondo@gmail.com',
                    'imagem' : 'alexandre.png',
                    'equipe' : 2,
                    'eh_lider' : 1,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Lucas Zannoni',
                    'email' : 'lucas.zannoni@hotmail.com',
                    'imagem' : 'zannoni.png',
                    'equipe' : 6,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Diego Lopes',
                    'email' : 'diegolopesrs@hotmail.com',
                    'imagem' : 'diego.png',
                    'equipe' : 3,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },
                {
                    'nome' : 'Isabelle Kircher Baiocco',
                    'email' : 'isabelle.kircherbaiocco@gmail.com',
                    'imagem' : 'isabelle.png',
                    'equipe' : 5,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },    
                {
                    'nome' : 'Felipe Antonio Zardo',
                    'email' : 'felipez775@gmail.com',
                    'imagem' : 'zardo.png',
                    'equipe' : 2,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                }, 
                {
                    'nome' : 'Matheus Cepik Brune',
                    'email' : 'matheuscepik@hotmail.com',
                    'imagem' : 'cepik.png',
                    'equipe' : 2,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                }, 
                {
                    'nome' : 'Augusto Scheeren Mattos',
                    'email' : 'augustomee@gmail.com',
                    'imagem' : 'augusto.png',
                    'equipe' : 1,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Elétrica',
                    'gestao_equipe_secundaria' : 0
                },  
                {
                    'nome' : 'Gabriel Mottin Santana',
                    'email' : 'gabrielmottin@hotmail.com',
                    'imagem' : 'mottin.png',
                    'equipe' : 7,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia de Produção',
                    'gestao_equipe_secundaria' : 0
                }, 
                {
                    'nome' : 'Davi Ebert Bobsin',
                    'email' : 'davibobsin@gmail.com',
                    'imagem' : 'davi.png',
                    'equipe' : 1,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia de Controle e Automação',
                    'gestao_equipe_secundaria' : 0
                }, 
                {
                    'nome' : 'William Porcher',
                    'email' : 'will_ipanema@hotmail.com',
                    'imagem' : 'william.png',
                    'equipe' : 2,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                }, 
                {
                    'nome' : 'Mauro Vinícius Bruno de Azevedo',
                    'email' : 'maurovini@hotmail.com',
                    'imagem' : 'mauro.png',
                    'equipe' : 2,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },      
                {
                    'nome' : 'João Paulo Martignago Mezzari',
                    'email' : 'joaopaulomezzari@gmail.com',
                    'imagem' : 'mezzari.png',
                    'equipe' : 7,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },           
                {
                    'nome' : 'Rodrigo Felipe Klein',
                    'email' : 'rodrigofelipek@yahoo.com.br',
                    'imagem' : 'klein.png',
                    'equipe' : 2,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },        
                {
                    'nome' : 'Bruno Cavalli Vieceli',
                    'email' : 'bruno_vieceli@hotmail.com',
                    'imagem' : 'vieceli.png',
                    'equipe' : 2,
                    'eh_lider' : 0,
                    'eh_marketing' : 1,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },         
                {
                    'nome' : 'Samuel Mathias Neitzke',
                    'email' : 'samuelneitzke@hotmail.com',
                    'imagem' : 'samuel.png',
                    'equipe' : 3,
                    'eh_lider' : 0,
                    'eh_marketing' : 0,
                    'eh_capitao' : 0,
                    'eh_lider_marketing' : 0,
                    'curso' : 'Engenharia Mecânica',
                    'gestao_equipe_secundaria' : 0
                },   
    ]
    return membros