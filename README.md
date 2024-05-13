
# ETL-bd3

Este projeto implementa um processo de ETL (Extração, Transformação e Carregamento) usando Python. Ele é configurado para ser facilmente executado em containers Docker, utilizando `docker-compose` para simplificar a gestão dos serviços necessários.

## Pré-requisitos

- Docker
- Docker Compose

Instale Docker e Docker Compose em sua máquina para seguir com a configuração e execução deste projeto.

## Configuração

### Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto de acordo com os arquivos .env.example (caso queira rodar nativamente) ou .env.docker.example (caso queira executar em um docker). Em um abiente linux pode gerar o arquivo com o seguinte comando:

```bash
cp .env.example .env
```

ou caso queira executar em um docker:

```bash
cp .env.docker.example .env
```



Adapte os valores conforme necessário para seu ambiente.

### Docker Compose

O `docker-compose` é utilizado para definir e rodar multi-containers Docker. O arquivo `docker-compose.yml` já está configurado para rodar o serviço necessário para o projeto.

#### Construindo e rodando o container

Na raiz do projeto, execute:

```bash
docker-compose up -d --build
```

Este comando constrói e inicia todos os serviços definidos no `docker-compose.yml`. Seu ambiente de ETL estará rodando em containers isolados após este comando.

## Estrutura do Projeto

- `src/`: Contém os scripts Python para o processo de ETL.
- `data/`: Diretório para os dados usados e gerados pelo ETL.
- `Dockerfile`: Define a configuração do container Docker.
- `docker-compose.yml`: Configura os serviços Docker utilizados no projeto.

## Contribuições

Sinta-se livre para contribuir com melhorias no código ou na documentação. Faça um fork do projeto, realize as alterações e proponha um pull request.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Autor

- João Pedro Barboza - [Github](https://github.com/lionezajoao)