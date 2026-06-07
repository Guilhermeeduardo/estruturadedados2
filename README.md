# Estrutura de Dados 2

## Sobre o Projeto

Este repositório contém a implementação de estruturas de dados avançadas em Python, projetadas para otimizar desempenho e eficiência em cenários de grande volume de dados. O objetivo é oferecer códigos claros, bem documentados e testados, que sirvam tanto como material de estudo quanto como base para aplicações reais.

## Estruturas Implementadas

- **Lista Encadeada** (simples e duplamente encadeada)
- **Fila e Pilha**
- **Árvore Binária de Busca (BST)**
- **Árvore AVL** (balanceamento automático)
- **Heap (mínimo e máximo)**
- **Tabela Hash** com tratamento de colisões via encadeamento separado

## Requisitos

- Python ≥ 3.8
- `pytest` para execução dos testes (opcional)

## Instalação

```bash
# Clone o repositório
git clone https://github.com/Guilhermeeduardo/estruturadedados2.git
cd estruturadedados2

# Opcional: crie um ambiente virtual
python -m venv venv
source venv/bin/activate

# Instale as dependências de desenvolvimento
pip install -r requirements.txt
```

## Uso

Cada estrutura de dados possui sua própria classe em módulos separados dentro da pasta `src/`. Veja exemplos de uso abaixo:

```python
from src.linked_list import LinkedList

# Criar uma lista encadeada
lista = LinkedList()
lista.append(10)
lista.append(20)
lista.prepend(5)
print(lista)
```

Os testes automatizados podem ser rodados com:

```bash
pytest tests/
```

## Contribuição

Contribuições são bem‑vindas! Siga os passos abaixo para propor melhorias:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)
3. Implemente e adicione testes
4. Submeta um Pull Request descrevendo claramente as mudanças

Por favor, siga o padrão de código PEP‑8 e inclua documentação nas novas classes/métodos.

## Licença

Este projeto está licenciado sob a licença MIT – veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.

## Contato

- **Autor:** Guilherme Eduardo
- **E‑mail:** guilherme@example.com
- **GitHub:** [Guilhermeeduardo](https://github.com/Guilhermeeduardo)

