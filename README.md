# 📚 Sistema de Gestão de Biblioteca Digital

## 🏆 Objetivo
Sistema completo para gerenciamento de bibliotecas digitais com cadastro de livros, usuários, controle de empréstimos e geração de relatórios estatísticos, desenvolvido em Python como trabalho acadêmico.

## ✨ Funcionalidades Principais

### 📖 Cadastros
- **Livros**: Título, autor, ano publicação, ISBN e categoria
- **Usuários**: Nome, e-mail único, tipo (aluno/professor/visitante)
- **Autores**: Nome e ORCID único
- **Categorias**: Organização temática dos livros

### 🔍 Consultas
- Listagem completa de todos os itens cadastrados
- Busca avançada de livros por:
  - Título
  - Autor
  - Categoria

### 🔄 Empréstimos
- Registro completo com datas de empréstimo e devolução
- Controle de disponibilidade dos livros
- Impedimento de empréstimos duplicados

### 📊 Estatísticas
- Relatório de livros por categoria
- Empréstimos por tipo de usuário
- Ranking dos 5 livros mais emprestados

### 💾 Persistência
- Armazenamento automático em arquivos
- CSV para dados estruturados
- TXT para emails cadastrados
- Recuperação dos dados ao reiniciar o sistema

## 🛠️ Tecnologias Utilizadas

### 🐍 Python Puro
- **Estruturas de dados**:
  - Listas para armazenamento principal
  - Dicionários para organização dos registros
  - Conjuntos para controle de unicidade
  - Tuplas para dados imutáveis

### 📁 Manipulação de Arquivos
- Leitura e escrita em formato CSV
- Persistência de dados em texto puro
- Carga automática na inicialização

### 🎮 Interface
- Sistema de menus hierárquico
- Navegação intuitiva
- Formulários com validação

## 🗂️ Estrutura do Projeto
biblioteca/
├── main.py # Ponto de entrada
├── function.py # Lógica principal
├── menu.py # Definição dos menus
├── variables.py # Estado global
├── autores.csv # Base de autores
├── categorias.csv # Categorias cadastradas
├── emprestimos.csv # Histórico de empréstimos
├── livros.csv # Acervo completo
├── usuarios.csv # Usuários cadastrados
└── emails.txt # Controle de emails


## 🚀 Como Executar

1. **Pré-requisitos**:
   - Python 3.6+ instalado
   - Terminal/CMD disponível

2. **Execução**:
   ```bash
   python main.py