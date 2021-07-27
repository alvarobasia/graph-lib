# Graph lib

Biblioteca implementada em Python que manipula e extrai informações sobre grafos, produzida para a matéria algoritmos e estrutura de dados 3.

## Funcionalidades

- Representa o grafo em matriz e lista de adjacências.

- Realiza busca em largura e em profundidade a partir de qualquer vértice do grafo e exibe os níveis da busca.

- Gera informações sobre os grafos como grau médio, mínimo e máximo, além da frequencia relativa

- Informa os componentes conexos do grafo.

## Modo de uso

Escreva o grafo que deseja utilizar em um arquivo de texto na raiz do projeto no formato Dimacs, após isso escreva um json com as configurações que deseja utilizar. **Importante** este arquivo deve se chamar `config.json`.

### Exemplo do arquivo:

```json
{
  "file": "as_graph.txt",
  "representation": "matriz",
  "sparse": false,
  "search_type": "wide",
  "infos": {
    "output": "testse.txt"
  },
  "search": {
    "init": 0,
    "output": "tesste.txt"
  },
  "connect": {
    "output": "teste.txt"
  }
}
```

### Opções

| Configuração     | Opções           | Padrão  | Informações                                                                                                                                   |
| ---------------- | ---------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `file`           |                  |         | Nome do arquivo de texto em formato Dimacs a ser lido                                                                                         |
| `representation` | `matriz`,`lista` | `lista` | Tipo da representação                                                                                                                         |
| `sparse`         | `true`,`false`   | `true`  | Se verdadeiro, será utilizada uma representação de matriz esparsa, se falso, será utilizado a lista nativa do Python em matriz de adjacências |
| `search_type`    | `wide`, `deep`   | `wide`  | Tipo da busca utilizada                                                                                                                       |
| `infos`          |                  |         | Objeto com a chave `output` com o nome do arquivo de saída                                                                                    |
| `search`         |                  |         | Objeto com a chave `output` com o nome do arquivo de saída e a chave `init` com o vértice inicial da busca                                    |
| `connect`        |                  |         | Objeto com a chave `output` com o nome do arquivo de saída                                                                                    |

Antes de executar você deve instalar as dependências desse projeto com o pip usando o comando:
`pip install scipy numpy`
Após as configurações e arquivo de texto do grafo na raiz do projeto basta digitar no terminal:
`python3 main.py`
