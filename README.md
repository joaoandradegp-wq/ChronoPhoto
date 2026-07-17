<h1 align="center">📸 ChronoPhoto</h1>

<p align="center">
ChronoPhoto é uma ferramenta inteligente para organização e renomeação de fotos baseada em metadados.
Ele utiliza o ExifTool para identificar a data real de captura dos arquivos e reorganiza sua biblioteca de imagens em ordem cronológica.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Beta-orange">
  <img src="https://img.shields.io/badge/Plataforma-Linux%20Mint%20%2F%20Linux-blue">
  <img src="https://img.shields.io/badge/Linguagem-Python-green">
  <img src="https://img.shields.io/badge/Interface-Tkinter-purple">
  <img src="https://img.shields.io/badge/Metadados-ExifTool-red">
</p>

---

## ✨ Recursos

<table>
<tr>

<td width="50%" valign="top">

<h3>📂 Seleção de Pasta</h3>

<ul>
<li>Interface gráfica simples</li>
<li>Seleção visual da pasta de processamento</li>
<li>Dispensa uso de linha de comando</li>
<li>Suporte para grandes coleções de arquivos</li>
</ul>

<br>

</td>

<td width="50%" valign="top">

<h3>🖥️ Interface Gráfica Leve</h3>

<ul>
<li>Desenvolvido em Python + Tkinter</li>
<li>Baixo consumo de recursos</li>
<li>Interface responsiva</li>
<li>Log visual em tempo real</li>
</ul>

</td>

</tr>


<tr>

<td width="50%" valign="top">

<h3>🕒 Identificação Inteligente de Datas</h3>

<ul>

<li>Analisa diferentes campos de metadados:</li>

<ul>
<li>DateTimeOriginal</li>
<li>CreationDate</li>
<li>CreateDate</li>
<li>MediaCreateDate</li>
<li>TrackCreateDate</li>
<li>ModifyDate</li>
<li>FileModifyDate</li>
</ul>

<li>Seleciona automaticamente a data mais confiável disponível</li>

</ul>

</td>


<td width="50%" valign="top">

<h3>📷 Leitura Completa de Metadados</h3>

<ul>

<li>Utiliza ExifTool em modo completo</li>
<li>Processa todos os metadados disponíveis</li>
<li>Maior precisão na identificação da data original</li>
<li>Suporte para imagens e arquivos multimídia</li>

</ul>

</td>

</tr>


<tr>

<td width="50%" valign="top">

<h3>🔄 Renomeação Automática</h3>

<ul>

<li>Criação de nomes cronológicos:</li>

<pre>
AAAA_MM_DD_0001.jpg
AAAA_MM_DD_0002.jpg
AAAA_MM_DD_0003.jpg
</pre>

<li>Agrupamento por data de captura</li>
<li>Ordenação por data e nome original</li>
<li>Controle automático de conflitos</li>

</ul>

</td>


<td width="50%" valign="top">

<h3>⚙️ Instalação Automática</h3>

<ul>

<li>Verifica a existência do ExifTool</li>
<li>Instala automaticamente quando necessário</li>
<li>Compatível com sistemas Debian:</li>

<ul>
<li>Linux Mint</li>
<li>Ubuntu</li>
<li>Debian</li>
</ul>

</ul>

</td>

</tr>


<tr>

<td width="50%" valign="top">

<h3>📊 Processamento em Tempo Real</h3>

<ul>

<li>Log visual durante a execução</li>
<li>Exibe cada etapa do processo:</li>

<pre>
Verificando ExifTool...

Lendo metadados...

Analisando datas...

Renomeando: 15234/30000
</pre>

<li>Execução em segundo plano</li>
<li>Interface permanece responsiva</li>

</ul>

</td>


<td width="50%" valign="top">

<h3>🛡️ Processamento Seguro</h3>

<ul>

<li>Não altera conteúdo dos arquivos</li>
<li>Modifica somente os nomes</li>
<li>Mantém extensões originais</li>
<li>Verifica conflitos antes da alteração</li>

</ul>

</td>

</tr>

</table>

---

## 📦 Requisitos

<ul>

<li>Linux Mint / Ubuntu / Debian</li>
<li>Python 3</li>
<li>Tkinter</li>
<li>ExifTool</li>

</ul>


O ChronoPhoto verifica automaticamente a instalação do ExifTool.

Instalação manual:

```bash
sudo apt install libimage-exiftool-perl
```

---

## 🚀 Instalação

Clone o projeto:

```bash
git clone https://github.com/joaoandradegp-wq/ChronoPhoto.git
```

Acesse a pasta:

```bash
cd ChronoPhoto
```

Execute:

```bash
python3 main.py
```

---

## 🖥️ Como utilizar

1. Execute o ChronoPhoto

2. Clique em:

```
Selecionar...
```

3. Escolha a pasta contendo suas fotos

4. Clique em:

```
Iniciar
```

5. O processo será executado automaticamente:

```
Verificando ExifTool...

Lendo metadados...

Analisando datas...

Agrupando arquivos...

Renomeando arquivos...
```

---

## 📷 Exemplo de Organização

Antes:

```
IMG_5421.JPG
DSC_0012.JPG
VID_20240101.MP4
```

Depois:

```
2024_01_01_0001.JPG
2024_01_01_0002.JPG
2024_01_01_0003.MP4
```

---

## 🧠 Como funciona

Fluxo de processamento:

```
Selecionar Pasta
        |
        v
Verificar ExifTool
        |
        v
Ler todos os metadados
        |
        v
Identificar melhor data disponível
        |
        v
Agrupar arquivos por dia
        |
        v
Ordenar cronologicamente
        |
        v
Renomear arquivos
```

---

## 📁 Estrutura do Projeto

```
ChronoPhoto/

├── main.py
│   └── Interface gráfica Tkinter
│
├── renomeador.py
│   └── Motor de leitura de metadados e renomeação
│
└── README.md
```

---

## 🎯 Casos de Uso

<ul>

<li>Organização de bibliotecas pessoais de fotos</li>

<li>Correção de nomes após backups</li>

<li>Organização de fotos antigas de celulares e câmeras</li>

<li>Recuperação da ordem cronológica de grandes coleções</li>

<li>Preparação de arquivos para NAS e servidores domésticos</li>

<li>Gerenciamento de acervos fotográficos</li>

</ul>

---

## 📌 Campos de Data Utilizados

O ChronoPhoto busca as datas nesta ordem:

```
1. DateTimeOriginal
2. CreationDate
3. CreateDate
4. MediaCreateDate
5. TrackCreateDate
6. ModifyDate
7. FileModifyDate
```

Caso nenhum metadado esteja disponível:

```
Data de alteração do arquivo
```

é utilizada como alternativa.

---

## ⚠️ Observações

<ul>

<li>Desenvolvido inicialmente para Linux Mint e sistemas baseados em Debian</li>

<li>Necessário possuir permissão de escrita na pasta selecionada</li>

<li>Apenas os nomes dos arquivos são modificados</li>

<li>Arquivos grandes podem levar mais tempo devido à leitura completa dos metadados</li>

<li>A leitura completa oferece maior precisão que métodos rápidos de análise</li>

</ul>

---

## 📸 Prévia

<p align="center">

<img width="600" alt="ChronoPhoto Screenshot" src="https://github.com/user-attachments/assets/IMAGEM_AQUI">

</p>

---

<p align="center">
Criado para quem deseja preservar e organizar suas memórias através do tempo. 📷
</p>
