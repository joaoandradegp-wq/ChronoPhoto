import os
import json
import shutil
import subprocess
import sys

from datetime import datetime


# ============================================================
# CAMPOS DE DATA
# ============================================================

CAMPOS_DATA = [
    "DateTimeOriginal",
    "CreationDate",
    "CreateDate",
    "MediaCreateDate",
    "TrackCreateDate",
    "ModifyDate",
    "FileModifyDate"
]


# ============================================================
# LOG
# ============================================================

_callback = None


def log(texto, substituir=False):

    if _callback:
        _callback(texto, substituir)
    else:
        print(texto)

def progresso(atual, total):

    if _callback:
        _callback(f"Renomeando: {atual}/{total}", substituir=True)        


# ============================================================
# GARANTE EXIFTOOL
# ============================================================

def garantir_exiftool():

    if shutil.which("exiftool"):
        log("ExifTool encontrado.")
        return

    log("ExifTool não encontrado.")
    log("Instalando ExifTool...")

    if os.geteuid() == 0:

        subprocess.run(
            ["apt", "update"],
            check=True
        )

        subprocess.run(
            [
                "apt",
                "install",
                "-y",
                "libimage-exiftool-perl"
            ],
            check=True
        )

    else:

        subprocess.run(
            [
                "sudo",
                "apt",
                "update"
            ],
            check=True
        )

        subprocess.run(
            [
                "sudo",
                "apt",
                "install",
                "-y",
                "libimage-exiftool-perl"
            ],
            check=True
        )

    if not shutil.which("exiftool"):
        raise Exception("Não foi possível instalar o ExifTool.")

    log("ExifTool instalado com sucesso.")


# ============================================================
# CONVERSÃO DE DATA
# ============================================================

def converter_data(valor):

    if not valor:
        return None

    valor = valor.split("+")[0].strip()

    if valor.endswith("Z"):
        valor = valor[:-1]

    formatos = [

        "%Y:%m:%d %H:%M:%S",

        "%Y:%m:%d %H:%M:%S.%f",

        "%Y-%m-%d %H:%M:%S",

        "%Y-%m-%d %H:%M:%S.%f",

        "%Y-%m-%dT%H:%M:%S",

        "%Y-%m-%dT%H:%M:%S.%f"

    ]

    for fmt in formatos:

        try:
            return datetime.strptime(valor, fmt)
        except:
            pass

    return None


# ============================================================
# EXECUTAR
# ============================================================

def executar(pasta, callback=None):

    global _callback

    _callback = callback

    garantir_exiftool()

    log("")
    log("Lendo metadados...")

    comando = [
        "exiftool",
        "-json",
        "-r",
        pasta
    ]

    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    dados = json.loads(resultado.stdout)

    log(f"{len(dados)} arquivos encontrados.")

    arquivos = []

    log("Analisando datas...")

    for item in dados:

        caminho = item.get("SourceFile")

        if not caminho:
            continue

        data = None

        for campo in CAMPOS_DATA:

            if campo in item:

                data = converter_data(item[campo])

                if data:
                    break

        if not data:

            data = datetime.fromtimestamp(
                os.path.getmtime(caminho)
            )

        arquivos.append({

            "arquivo": caminho,

            "data": data

        })

    grupos = {}

    log("Agrupando arquivos...")

    for item in arquivos:

        chave = item["data"].strftime("%Y_%m_%d")

        grupos.setdefault(
            chave,
            []
        ).append(item)

    total_arquivos = len(arquivos)
    renomeados = 0

    log("Renomeando arquivos...")

    total = 0

    for chave, lista in sorted(grupos.items()):

        lista.sort(
            key=lambda x: (
                x["data"],
                x["arquivo"].lower()
            )
        )

        contador = 1

        for item in lista:

            renomeados += 1

            progresso(renomeados,total_arquivos)

            origem = item["arquivo"]

            pasta_arquivo = os.path.dirname(origem)

            extensao = os.path.splitext(origem)[1].lower()

            while True:

                novo_nome = f"{chave}_{contador:04d}{extensao}"

                destino = os.path.join(
                    pasta_arquivo,
                    novo_nome
                )

                if (
                    not os.path.exists(destino)
                    or os.path.samefile(origem, destino)
                ):
                    break

                contador += 1

            if os.path.basename(origem) != novo_nome:                

                os.rename(
                    origem,
                    destino
                )

                total += 1

            contador += 1

    log("")
    log("===================================")
    log(f"Arquivos renomeados: {total}")
    log("Processo concluído!")
    log("===================================")

    return total
