<h1><b>Título do Projeto</b></h1>

Controle de Ponto

<h1><b>Descrição do Projeto</b></h1>

Um sistema para Gestão de Ponto Eletrônico com registro e consulta de ponto, validação de ponto, folha de pagamento e etc.
Projeto desenvolvido para agregar conhecimento em complexidade de modelagem de database e manipulação de datetime.

<h1><b>Funcionalidades do projeto</b></h1>

- Autenticação

Sistema possui autenticação, após registro do funcionário o mesmo recebe uma senha provisória para realizar seu acesso.
Possui mecanismo opcional para segurança de senha como período de validade (a senha expira).
A senha pode ser resetada para alteração a qualquer momento. Tudo isso mediado por um supervisor com regras bem definidas.

- Acesso as funcionalidades principais do sistema

O funcionário só consegue ter acesso as funcionalidades principais após o Login e consequentemente Registro de Ponto, e precisa estar dentro do seu período de trabalho.

- Registro de Ponto e Validação

Os funcionários registram diariamente o ponto e estes registros são acessados por seus supervisores para validação provisória, após validação provisória, os reggistros voltam para o funcionário validá-los por definitivo.

- Consulta de Ponto e Folha de Pagamento

As consultas ficam disponíveis para os funcionário terem acesso a qualquer momento, bastam filtrar por períodos.

<h1><b>Tecnologias utilizadas</b></h1>

- HTML e CSS(Bootstrap5) para o Front-End.
- Framework Django do Python para o Back-End.
- SQLite3 para Banco de Dados.

<h1><b>Inicialização</b></h1>

Após realizar o <code>git clone</code> aplicar o ambiente virtual (virtualenv), instalar o python e django. 
Acessar a pasta do projeto e rodar a aplicação com o comando <code>python manage.py runserver</code>
Após este comando acessar <code>localhost:8000 ou 127.0.0.1:8000</code> para visualizar o sistema.

<h1><b>Implementações futuras</b></h1>

O sistema pode expandir para um sistema completo de Gestão de Pessoas.

<h1><b>Status do projeto</b></h1>

Em andamento.

