# AlgoritmoKNN

O algoritmo KNN (K-Nearest Neighbors) é um algoritmo de aprendizado de máquina supervisionado usado para classificação e regressão. Ele é considerado um algoritmo simples, porém eficaz, para problemas de aprendizado de máquina O KNN classifica os pontos de dados com base na proximidade deles com outros pontos de dados no espaço de características. O "K" no KNN refere-se ao número de vizinhos mais próximos que são considerados para tomar uma decisão de classificação ou regressão O KNN pode ser aplicado em várias áreas, como reconhecimento de padrões, sistemas de recomendação, detecção de fraudes, entre outros.

Neste projeto, é realizada a análise de flores das espécies "setosa", "versicolor" e "virnínica" e de acordo com as dimensões de suas pétalas e sépalas é comparado com o arquivo "íris_data2" que não possui o nome das espécies, apenas as dimensões. De acordo com as dimensões e os K elementos mais próximos do arquivo "íris_data" é classificado a nome da espécie mais provável que ela seja

🐳 Executando com Docker
Siga os passos abaixo para executar este projeto usando Docker:

## 🐳 Executando com Docker

Siga os passos abaixo para executar este projeto usando Docker:

### 1. Construir a imagem Docker

Abra o terminal na raiz do projeto (onde está o `Dockerfile`) e execute:

```bash
docker build -t algoritmo-knn .

docker run --rm algoritmo-knn
