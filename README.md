# 🔍 Nmap Scanner

Um scanner de rede desenvolvido em Python utilizando o Nmap para automatizar a descoberta de hosts, identificação de portas abertas e detecção de serviços.

## 📖 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar automação em Python aplicada à cibersegurança e ao reconhecimento de redes.

A ferramenta realiza varreduras utilizando o Nmap e organiza os resultados em relatórios de fácil visualização.

## ✨ Funcionalidades

- Descoberta de hosts ativos
- Identificação de portas abertas
- Detecção de serviços em execução
- Geração de relatórios em JSON
- Execução simples via terminal

## 🛠 Tecnologias Utilizadas

- Python 3
- Nmap
- python-nmap

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/nmap-scanner.git
cd nmap-scanner
```

Instale as dependências:

```bash
sudo apt install nmap
pip install -r requirements.txt
```

## 🚀 Utilização

Execute o programa:

```bash
python scanner.py
```

Digite o IP ou domínio desejado:

```text
scanme.nmap.org
```

## 📊 Exemplo de Saída

```json
{
  "scanme.nmap.org": {
    "estado": "up",
    "portas": [
      {
        "porta": 22,
        "servico": "ssh"
      },
      {
        "porta": 80,
        "servico": "http"
      }
    ]
  }
}
```

## 📚 O que Aprendi

- Integração entre Python e Nmap
- Automação de tarefas de reconhecimento
- Manipulação de arquivos JSON
- Estruturação de projetos para GitHub
- Boas práticas de documentação

## ⚠ Aviso Legal

Esta ferramenta destina-se exclusivamente a fins educacionais e ambientes autorizados. Não realize varreduras em sistemas sem permissão.

## 👨‍💻 Autor

Cristyan Antonio
