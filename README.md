Sistema de Gerenciamento de Pendências

O Sistema de Gerenciamento de Pendências é uma aplicação web construída usando o framework Django para gerenciar pendências de forma eficiente. Este sistema permite o cadastro, consulta e atualização de pendências, bem como a manutenção de um histórico de ações realizadas pelos usuários.

Funcionalidades

- Página Inicial de Pendências: Exibe estatísticas sobre as pendências, incluindo o número total de pendências, pendências pendentes e pendências resolvidas.

- Inserir Pendência: Permite adicionar novas pendências ao sistema, incluindo informações como nome da pessoa, CPF, código PA e descrição. Verifica a integridade dos dados e registra a ação no histórico.

- Consultar Pendência: Permite buscar pendências com base no nome da pessoa, CPF ou código PA. Exibe os resultados da consulta.

- Mostrar Pendência: Exibe os detalhes de uma pendência específica e permite alternar o status (pendente/resolvido) da pendência.

- Excluir Pendência: Permite a exclusão de pendências após a autenticação do usuário. Registra a ação no histórico.

- Histórico de Ações: Exibe um histórico de ações realizadas pelos usuários, incluindo inserção, atualização e exclusão de pendências.

Pré-requisitos

Certifique-se de que você tenha os seguintes requisitos antes de executar aplicação:

- Python (versão recomendada: 3.6+)
- Django (versão recomendada: 3.0+)
- Banco de dados compatível com o Django (por exemplo, SQLite, MySQL, PostgreSQL) mas foi utilizado o sqlite
- Dependências adicionais (instaladas via pip): django-crispy-forms, django-db-utils, re

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para criar issues, fazer pull requests ou propor melhorias para o projeto. Certifique-se de seguir as diretrizes de contribuição do projeto.

Autor

- Rafael Orlando (https://github.com/rafaelorland) - Desenvolvedor Principal
