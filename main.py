# SERVER API
import base64
import datetime
from flask import Flask, jsonify, request, redirect, url_for, Blueprint, render_template, send_from_directory
from flask_cors import CORS
import json
import mysql.connector
import requests
import boto3
import os
import ast
import time

import pythonProject
from Ponto.ponto import ponto_blueprint


#Amazon
selecao = []
dicionario = []
dic2 = []
dic_whats = []
dic_whats2 = []



#token = "8c4EF9vXi8TZe6581e0af85c25"




def assinar_arquivo(arquivo):
    url = boto3.client('s3').generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': 'dbfilesintellimetrics', 'Key': arquivo},
    ExpiresIn=3600)
    return url
#assinar_arquivo()

def upload_file(file_name, bucket, object_name):
    client = boto3.client('s3')
    try:
        response = client.upload_file(file_name, bucket, object_name,ExtraArgs={'ACL': 'public-read'})
    except ClientError as e:
        logging.error(e)
        return False
    return True


##DAQUI PRA BAIXO GERADOR DE API CONSULTAS NO BANCO
##ATUALIZADO EM 29-05-2024




#Selecionar registros da tabela DbIntelliMetrics.VwTbPosicaoAtual
def Selecionar_VwTbPosicaoAtual():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdDispositivo, dsLat, dsLong, dtData, dtHora from DbIntelliMetrics.VwTbPosicaoAtual'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.VwTbPosicaoAtual
def Inserir_VwTbPosicaoAtual(dsLat, dsLong, dtData, dtHora):
    conexao = pythonProject.conecta_bd()()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.VwTbPosicaoAtual ( dsLat, dsLong, dtData, dtHora ) values ("{dsLat}", "{dsLong}", "{dtData}", "{dtHora}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.VwTbPosicaoAtual
def deletar_VwTbPosicaoAtual(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.VwTbPosicaoAtual where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.VwTbPosicaoAtual
def Alterar_VwTbPosicaoAtual(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.VwTbPosicaoAtual set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO






#Selecionar registros da tabela DbIntelliMetrics.TbChamados
def Selecionar_TbChamados():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdChamados, dtOperacao, dsTipo, dsDescricao, nrQtde, dsUser, dtRegistro from DbIntelliMetrics.TbChamados'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbChamados
def Inserir_TbChamados(dtOperacao, dsTipo, dsDescricao, nrQtde, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbChamados ( dtOperacao, dsTipo, dsDescricao, nrQtde, dsUser, dtRegistro ) values ("{dtOperacao}", "{dsTipo}", "{dsDescricao}", "{nrQtde}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbChamados
def deletar_TbChamados(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbChamados where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbChamados
def Alterar_TbChamados(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbChamados set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbCliente
def Selecionar_TbCliente():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdCliente, dsNome, nrCnpj, nrIe, nrInscMun, dsLogradouro, nrNumero, dsComplemento, dsBairro, dsCep, dsCidade, dsUF, dsObs, cdStatus, dsUser, dtRegistro from DbIntelliMetrics.TbCliente'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbCliente
def Inserir_TbCliente(dsNome, nrCnpj, nrIe, nrInscMun, dsLogradouro, nrNumero, dsComplemento, dsBairro, dsCep, dsCidade, dsUF, dsObs, cdStatus, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbCliente ( dsNome, nrCnpj, nrIe, nrInscMun, dsLogradouro, nrNumero, dsComplemento, dsBairro, dsCep, dsCidade, dsUF, dsObs, cdStatus, dsUser, dtRegistro ) values ("{dsNome}", "{nrCnpj}", "{nrIe}", "{nrInscMun}", "{dsLogradouro}", "{nrNumero}", "{dsComplemento}", "{dsBairro}", "{dsCep}", "{dsCidade}", "{dsUF}", "{dsObs}", "{cdStatus}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbCliente
def deletar_TbCliente(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbCliente where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbCliente
def Alterar_TbCliente(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbCliente set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbDestinatario
def Selecionar_TbDestinatario():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdDestinatario, dsNome, nrCnpj, nrIe, nrInscMun, dsLogradouro, nrNumero, dsComplemento, dsBairro, dsCep, dsCidade, dsUF, dsObs, cdStatus, dsLat, dsLong, nrRaio, dsUser, dtRegistro from DbIntelliMetrics.TbDestinatario'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbDestinatario
def Inserir_TbDestinatario(dsNome, nrCnpj, nrIe, nrInscMun, dsLogradouro, nrNumero, dsComplemento, dsBairro, dsCep, dsCidade, dsUF, dsObs, cdStatus, dsLat, dsLong, nrRaio, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbDestinatario ( dsNome, nrCnpj, nrIe, nrInscMun, dsLogradouro, nrNumero, dsComplemento, dsBairro, dsCep, dsCidade, dsUF, dsObs, cdStatus, dsLat, dsLong, nrRaio, dsUser, dtRegistro ) values ("{dsNome}", "{nrCnpj}", "{nrIe}", "{nrInscMun}", "{dsLogradouro}", "{nrNumero}", "{dsComplemento}", "{dsBairro}", "{dsCep}", "{dsCidade}", "{dsUF}", "{dsObs}", "{cdStatus}", "{dsLat}", "{dsLong}", "{nrRaio}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbDestinatario
def deletar_TbDestinatario(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbDestinatario where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbDestinatario
def Alterar_TbDestinatario(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbDestinatario set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbDispositivo
def Selecionar_TbDispositivo():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdDispositivo, dsDispositivo, dsModelo, dsDescricao, dsObs, dsLayout, nrChip, cdStatus, dsUser, dtRegistro from DbIntelliMetrics.TbDispositivo'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbDispositivo
def Inserir_TbDispositivo(dsDispositivo, dsModelo, dsDescricao, dsObs, dsLayout, nrChip, cdStatus, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbDispositivo ( dsDispositivo, dsModelo, dsDescricao, dsObs, dsLayout, nrChip, cdStatus, dsUser, dtRegistro ) values ("{dsDispositivo}", "{dsModelo}", "{dsDescricao}", "{dsObs}", "{dsLayout}", "{nrChip}", "{cdStatus}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbDispositivo
def deletar_TbDispositivo(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbDispositivo where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbDispositivo
def Alterar_TbDispositivo(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbDispositivo set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbImagens
def Selecionar_TbImagens(codigo):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    if codigo == '0':
        comando = f'select cdImagens, dsCaminho, cdCodigo, cdTipo, dsUser, dtRegistro from DbIntelliMetrics.TbImagens'
    else:
        comando = f'select cdImagens, dsCaminho, cdCodigo, cdTipo, dsUser, dtRegistro from DbIntelliMetrics.TbImagens where SUBSTRING_INDEX(cdCodigo, "-", 1) ={codigo}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbImagens
def Inserir_TbImagens(dsCaminho, cdCodigo, cdTipo, dsUser, dtRegistro, cdProduto, nrImagem):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbImagens ( dsCaminho, cdCodigo, cdTipo, dsUser, dtRegistro, cdProduto, nrImagem ) values ("{dsCaminho}", "{cdCodigo}", "{cdTipo}", "{dsUser}", "{dtRegistro}", "{cdProduto}", "{nrImagem}")'
    #print(comando)
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbImagens
def deletar_TbImagens(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbImagens where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbImagens
def Alterar_TbImagens(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbImagens set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO#


#Selecionar registros da tabela DbIntelliMetrics.TbPosicao
def Selecionar_TbPosicao():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdPosicao, dsModelo, dtData, dtHora, dsLat, dsLong, nrTemp, nrBat, nrSeq, dsArquivo, cdDispositivo, dsEndereco, dtRegistro from DbIntelliMetrics.TbPosicao'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbPosicao
def Inserir_TbPosicao(dsModelo, dtData, dtHora, dsLat, dsLong, nrTemp, nrBat, nrSeq, dsArquivo, cdDispositivo, dsEndereco, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbPosicao ( dsModelo, dtData, dtHora, dsLat, dsLong, nrTemp, nrBat, nrSeq, dsArquivo, cdDispositivo, dsEndereco, dsUser, dtRegistro ) values ("{dsModelo}", "{dtData}", "{dtHora}", "{dsLat}", "{dsLong}", "{nrTemp}", "{nrBat}", "{nrSeq}", "{dsArquivo}", "{cdDispositivo}", "{dsEndereco}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbPosicao
def deletar_TbPosicao(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbPosicao where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbPosicao
def Alterar_TbPosicao(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbPosicao set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbProduto
def Selecionar_TbProduto(codigo):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    # Consulta os dados da tabela produtos
    comando = f"SELECT cdProduto, dsDescricao, dsNome, nrAlt, nrCodigo, nrComp, nrLarg, nrQtde, dsStatus FROM VwTbProdutoTotalStaus where cdProduto = {codigo}"
    cursor.execute(comando)
    produtos = cursor.fetchall()

    # Array para armazenar os resultados
    produtos_json = []

    # Percorre os produtos
    for produto in produtos:
        cdProduto, dsDescricao, dsNome, nrAlt, nrCodigo, nrComp, nrLarg, nrQtde, dsStatus = produto

        # Consulta os dados da tabela imagens para o produto atual
        comando = f"SELECT cdCodigo, dsCaminho  FROM TbImagens WHERE cdProduto = {codigo}"
        # query = "SELECT cdCodigo, dsCaminho  FROM TbImagens WHERE cdImagens = 26"
        cursor.execute(comando)
        imagens = cursor.fetchall()


        # Array para armazenar as imagens
        imagens_array = []

        # Percorre as imagens e adiciona ao array
        for imagem in imagens:
            cdCodigo, dsCaminho = imagem
            imagens_array.append({
                'cdImagens': cdCodigo,
                'dsCaminho': dsCaminho
            })

        # Cria um dicionário com os dados do produto e o array de imagens
        produto_json = {
            'cdProduto': cdProduto,
            'dsDescricao': dsDescricao,
            'dsNome': dsNome,
            'nrAlt': nrAlt,
            'nrCodigo': nrCodigo,
            'nrComp': nrComp,
            'nrLarg': nrLarg,
            'nrQtde': nrQtde,
            'dsStatus': dsStatus,
            'imagens': imagens_array
        }
        #produtos_json.append(produto_json)
        produtos_json.append(produto)
        produtos_json.append(imagens_array)

    # Fecha a conexão com o banco de dados
    cursor.close()
    conexao.close()


    ##if codigo == "0":
    ##    comando = f'select cdProduto, dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, dsUser, dtRegistro from DbIntelliMetrics.TbProduto'
    ##else:
    ##    comando = f'select cdProduto, dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, dsUser, dtRegistro from DbIntelliMetrics.TbProduto where cdProduto = "{codigo}" '

    ##cursor.execute(comando)
    ##resultado = cursor.fetchall()
    ##cursor.close()
    ##conexao.close()
    return jsonify(produtos_json)
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbProduto
def Inserir_TbProduto(dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbProduto ( dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, dsUser, dtRegistro ) values ("{dsNome}", "{dsDescricao}", "{nrCodigo}", "{nrLarg}", "{nrComp}", "{nrAlt}", "{cdStatus}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
    return cursor.lastrowid
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbProduto
def deletar_TbProduto(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbProduto where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbProduto
def Alterar_TbProduto(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbProduto set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbRelacionamento
def Selecionar_TbRelacionamento():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdRelacionamento, cdPai, cdFilho, cdTipo, dsDescricao, cdStatus, dsUser, dtRegistro from DbIntelliMetrics.TbRelacionamento'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbRelacionamento
def Inserir_TbRelacionamento(cdPai, cdFilho, cdTipo, dsDescricao, cdStatus, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbRelacionamento ( cdPai, cdFilho, cdTipo, dsDescricao, cdStatus, dsUser, dtRegistro ) values ("{cdPai}", "{cdFilho}", "{cdTipo}", "{dsDescricao}", "{cdStatus}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbRelacionamento
def deletar_TbRelacionamento(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbRelacionamento where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbRelacionamento
def Alterar_TbRelacionamento(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbRelacionamento set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbSensor
def Selecionar_TbSensor():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdSensor, dsNome, cdTipo, dsDescricao, cdUnidade, nrUnidadeIni, nrUnidadeFim, dsUser, dtRegistro from DbIntelliMetrics.TbSensor'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbSensor
def Inserir_TbSensor(dsNome, cdTipo, dsDescricao, cdUnidade, nrUnidadeIni, nrUnidadeFim, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbSensor ( dsNome, cdTipo, dsDescricao, cdUnidade, nrUnidadeIni, nrUnidadeFim, dsUser, dtRegistro ) values ("{dsNome}", "{cdTipo}", "{dsDescricao}", "{cdUnidade}", "{nrUnidadeIni}", "{nrUnidadeFim}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbSensor
def deletar_TbSensor(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbSensor where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbSensor
def Alterar_TbSensor(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbSensor set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbStatus
def Selecionar_TbStatus():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdStatus, dsStatus, dsUser, dtRegistro from DbIntelliMetrics.TbStatus'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbStatus
def Inserir_TbStatus(dsStatus, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbStatus ( dsStatus, dsUser, dtRegistro ) values ("{dsStatus}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbStatus
def deletar_TbStatus(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbStatus where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbStatus
def Alterar_TbStatus(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbStatus set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbTag
def Selecionar_TbTag():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdTag, dsDescricao, dsConteudo, dsUser, dtRegistro from DbIntelliMetrics.TbTag'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbTag
def Inserir_TbTag(dsDescricao, dsConteudo, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbTag ( dsDescricao, dsConteudo, dsUser, dtRegistro ) values ("{dsDescricao}", "{dsConteudo}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbTag
def deletar_TbTag(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbTag where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbTag
def Alterar_TbTag(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbTag set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbTicket
def Selecionar_TbTicket():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdTicket, dtOperacao, dsAtendimento, nrAbertos, nrFechados, nrPendentes, dsUser, dtRegistro from DbIntelliMetrics.TbTicket'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbTicket
def Inserir_TbTicket(dtOperacao, dsAtendimento, nrAbertos, nrFechados, nrPendentes, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbTicket ( dtOperacao, dsAtendimento, nrAbertos, nrFechados, nrPendentes, dsUser, dtRegistro ) values ("{dtOperacao}", "{dsAtendimento}", "{nrAbertos}", "{nrFechados}", "{nrPendentes}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbTicket
def deletar_TbTicket(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbTicket where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbTicket
def Alterar_TbTicket(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbTicket set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbTicketResumo
def Selecionar_TbTicketResumo():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdTicketResumo, dtOperacao, dsAtendimento, dsNaoAtribuido, dsSemResolucao, dsAtualizado, dsPendente, dsResolvido, dsUser, dtRegistro from DbIntelliMetrics.TbTicketResumo'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbTicketResumo
def Inserir_TbTicketResumo(dtOperacao, dsAtendimento, dsNaoAtribuido, dsSemResolucao, dsAtualizado, dsPendente, dsResolvido, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbTicketResumo ( dtOperacao, dsAtendimento, dsNaoAtribuido, dsSemResolucao, dsAtualizado, dsPendente, dsResolvido, dsUser, dtRegistro ) values ("{dtOperacao}", "{dsAtendimento}", "{dsNaoAtribuido}", "{dsSemResolucao}", "{dsAtualizado}", "{dsPendente}", "{dsResolvido}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbTicketResumo
def deletar_TbTicketResumo(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbTicketResumo where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbTicketResumo
def Alterar_TbTicketResumo(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbTicketResumo set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbTipo
def Selecionar_TbTipo():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdTipo, dsDescricao, dsUser, dtRegistro from DbIntelliMetrics.TbTipo'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbTipo
def Inserir_TbTipo(dsDescricao, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbTipo ( dsDescricao, dsUser, dtRegistro ) values ("{dsDescricao}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbTipo
def deletar_TbTipo(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbTipo where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbTipo
def Alterar_TbTipo(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbTipo set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbUnidade
def Selecionar_TbUnidade():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdUnidade, dsUnidade, dsSimbolo, dsUser, dtRegistro from DbIntelliMetrics.TbUnidade'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbUnidade
def Inserir_TbUnidade(dsUnidade, dsSimbolo, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbUnidade ( dsUnidade, dsSimbolo, dsUser, dtRegistro ) values ("{dsUnidade}", "{dsSimbolo}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbUnidade
def deletar_TbUnidade(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbUnidade where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbUnidade
def Alterar_TbUnidade(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbUnidade set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbUsuario
def Selecionar_TbUsuario():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdUsuario, dsNome, dsLogin, dsSenha, cdPerfil, dsUser, dtRegistro from DbIntelliMetrics.TbUsuario'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbUsuario
def Inserir_TbUsuario(dsNome, dsLogin, dsSenha, cdPerfil, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbUsuario ( dsNome, dsLogin, dsSenha, cdPerfil, dsUser, dtRegistro ) values ("{dsNome}", "{dsLogin}", "{dsSenha}", "{cdPerfil}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbUsuario
def deletar_TbUsuario(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbUsuario where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbUsuario
def Alterar_TbUsuario(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbUsuario set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbVisita
def Selecionar_TbVisita():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdVisita, cdCliente, cdVisitante, dtData, dsUser, dtRegistro from DbIntelliMetrics.TbVisita'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbVisita
def Inserir_TbVisita(cdCliente, cdVisitante, dtData, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbVisita ( cdCliente, cdVisitante, dtData, dsUser, dtRegistro ) values ("{cdCliente}", "{cdVisitante}", "{dtData}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbVisita
def deletar_TbVisita(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbVisita where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbVisita
def Alterar_TbVisita(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbVisita set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbVisitante
def Selecionar_TbVisitante():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdVisitante, dsNome, nrTelefone, nrDocumento, dsEmail, dsUser, dtRegistro from DbIntelliMetrics.TbVisitante'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbVisitante
def Inserir_TbVisitante(dsNome, nrTelefone, nrDocumento, dsEmail, dsUser, dtRegistro):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbVisitante ( dsNome, nrTelefone, nrDocumento, dsEmail, dsUser, dtRegistro ) values ("{dsNome}", "{nrTelefone}", "{nrDocumento}", "{dsEmail}", "{dsUser}", "{dtRegistro}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbVisitante
def deletar_TbVisitante(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbVisitante where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbVisitante
def Alterar_TbVisitante(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbVisitante set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbPosicao
def Selecionar_TbPosicao():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select dtData, dtHora, dsLat, dsLong, nrTemp, nrBat, dsEndereco from DbIntelliMetrics.TbPosicao'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO




#Deletar registros da tabela DbIntelliMetrics.TbPosicao
def deletar_TbPosicao(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbPosicao where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbPosicao
def Alterar_TbPosicao(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbPosicao set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.TbProdutoTipo
def Selecionar_VwTbProdutoTipo(codigo):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    if codigo == "0":
        comando = f'select cdProduto, dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, cdDispositivo, dsDispositivo, dsModelo, DescDispositivo, dsObs, dsLayout, nrChip, StatusDispositivo from DbIntelliMetrics.VwTbProdutoTipo'
    else:
        comando = f'select cdProduto, dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, cdDispositivo, dsDispositivo, dsModelo, DescDispositivo, dsObs, dsLayout, nrChip, StatusDispositivo from DbIntelliMetrics.VwTbProdutoTipo where cdProduto = "{codigo}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.VwTbProdutoTipo
def Inserir_VwTbProdutoTipo(dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, cdDispositivo, dsDispositivo, dsModelo, DescDispositivo, dsObs, dsLayout, nrChip, StatusDispositivo):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.VwTbProdutoTipo ( dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, cdDispositivo, dsDispositivo, dsModelo, DescDispositivo, dsObs, dsLayout, nrChip, StatusDispositivo ) values ("{dsNome}", "{dsDescricao}", "{nrCodigo}", "{nrLarg}", "{nrComp}", "{nrAlt}", "{cdStatus}", "{cdDispositivo}", "{dsDispositivo}", "{dsModelo}", "{DescDispositivo}", "{dsObs}", "{dsLayout}", "{nrChip}", "{StatusDispositivo}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.VwTbProdutoTipo
def deletar_VwTbProdutoTipo(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.VwTbProdutoTipo where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.VwTbProdutoTipo
def Alterar_VwTbProdutoTipo(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.VwTbProdutoTipo set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Selecionar registros da tabela DbIntelliMetrics.VwTbProdutoTotalStaus
def Selecionar_VwTbProdutoTotalStaus(codigo):
    #conexao = conecta_bd()
    #cursor = conexao.cursor(dictionary=True)
    #if codigo == "0":
    #    comando = f'select Status, nrQtde from DbIntelliMetrics.VwTbProdutoTotalStaus order by Status'
    #else:
    #    comando = f'select Status, nrQtde from DbIntelliMetrics.VwTbProdutoTotalStaus where cdProduto = {codigo} order by Status'
    #cursor.execute(comando)
    #resultado = cursor.fetchall()
    #cursor.close()
    #conexao.close()
    #return  resultado
    try:
        # Conecta ao banco de dados
        conexao = pythonProject.conecta_bd()
        cursor = conexao.cursor()  # (dictionary=True)

        # Consulta os dados da tabela produtos
        if codigo == "0":
            comando = f"SELECT cdProduto, dsDescricao, dsNome, nrAlt, nrCodigo, nrComp, nrLarg FROM TbProduto"
        else:
            comando = f"SELECT cdProduto, dsDescricao, dsNome, nrAlt, nrCodigo, nrComp, nrLarg FROM TbProduto where cdProduto = {codigo}"
        cursor.execute(comando)
        produtos = cursor.fetchall()

        # Array para armazenar os resultados
        produtos_json = []

        # Percorre os produtos
        for produto in produtos:
            cdProduto, dsDescricao, dsNome, nrAlt, nrCodigo, nrComp, nrLarg = produto
            codigo = cdProduto
            # Status
            # Consulta os dados da tabela imagens para o produto atual
            comando = f"SELECT dsStatus, nrQtde  FROM VwTbProdutoTotalStaus WHERE cdProduto = {codigo}"
            cursor.execute(comando)
            status = cursor.fetchall()

            # Array para armazenar as imagens
            status_array = []

            # Percorre as imagens e adiciona ao array
            for statu in status:
                dsStatus, nrQtde = statu
                status_array.append({
                    'dsStatus': dsStatus,
                    'nrQtde': nrQtde
                })
            # fim Status

            # Consulta os dados da tabela imagens para o produto atual
            comando = f"SELECT cdCodigo, dsCaminho  FROM TbImagens WHERE cdProduto = {codigo}"
            cursor.execute(comando)
            imagens = cursor.fetchall()
            # Array para armazenar as imagens
            imagens_array = []

            # Percorre as imagens e adiciona ao array
            for imagem in imagens:
                cdCodigo, dsCaminho = imagem
                imagens_array.append({
                    'cdImagens': cdCodigo,
                    'dsCaminho': dsCaminho
                })

            # Cria um dicionário com os dados do produto e o array de imagens
            produto_json = {
                'cdProduto': cdProduto,
                'dsDescricao': dsDescricao,
                'dsNome': dsNome,
                'nrAlt': nrAlt,
                'nrCodigo': nrCodigo,
                'nrComp': nrComp,
                'nrLarg': nrLarg,
                'imagens': imagens_array,
                'status': status_array
            }
            produtos_json.append(produto_json)

        # Fecha a conexão com o banco de dados
        cursor.close()
        conexao.close()
        return jsonify(produtos_json)

    except mysql.connector.Error as error:
        return jsonify({'error': f'Erro ao acessar o banco de dados: {error}'})


#FIM DA FUNÇÃO

def Selecionar_VwTbProdutoTotal(codigo):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    if codigo == "0":
        comando = f'select cdProduto, dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, nrQtde from DbIntelliMetrics.VwTbProdutoTotal'
    else:
        comando = f'select cdProduto, dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, nrQtde from DbIntelliMetrics.VwTbProdutoTotal where cdProduto = {codigo}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    print(comando)
    return  resultado
#FIM DA FUNÇÃO



#Inserir registros da tabela DbIntelliMetrics.VwTbProdutoTotalStaus
def Inserir_VwTbProdutoTotalStaus(dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, Status, nrQtde):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.VwTbProdutoTotalStaus ( dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, Status, nrQtde ) values ("{dsNome}", "{dsDescricao}", "{nrCodigo}", "{nrLarg}", "{nrComp}", "{nrAlt}", "{Status}", "{nrQtde}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.VwTbProdutoTotalStaus
def deletar_VwTbProdutoTotalStaus(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.VwTbProdutoTotalStaus where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.VwTbProdutoTotalStaus
def Alterar_VwTbProdutoTotalStaus(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.VwTbProdutoTotalStaus set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO

#Selecionar registros da tabela DbIntelliMetrics.TbFuncionario
def Selecionar_TbFuncionario():
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'select cdFuncionario, dsBairro, dsCidade, dsComplemento, dsFuncao, dsLogradouro, dsNomeEmpregado, dsNumCasa, dsUser, dtRegistro, nrCodEmpregado, TbFuncionariocol from DbIntelliMetrics.TbFuncionario'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado
#FIM DA FUNÇÃO


#Inserir registros da tabela DbIntelliMetrics.TbFuncionario
def Inserir_TbFuncionario(dsBairro, dsCidade, dsComplemento, dsFuncao, dsLogradouro, dsNomeEmpregado, dsNumCasa, dsUser, dtRegistro, nrCodEmpregado, TbFuncionariocol):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'insert into DbIntelliMetrics.TbFuncionario ( dsBairro, dsCidade, dsComplemento, dsFuncao, dsLogradouro, dsNomeEmpregado, dsNumCasa, dsUser, dtRegistro, nrCodEmpregado, TbFuncionariocol ) values ("{dsBairro}", "{dsCidade}", "{dsComplemento}", "{dsFuncao}", "{dsLogradouro}", "{dsNomeEmpregado}", "{dsNumCasa}", "{dsUser}", "{dtRegistro}", "{nrCodEmpregado}", "{TbFuncionariocol}")'
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Deletar registros da tabela DbIntelliMetrics.TbFuncionario
def deletar_TbFuncionario(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbFuncionario where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbFuncionario
def Alterar_TbFuncionario(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbFuncionario set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


## FIM DAS CONSULTAS NO BANCO


app = Flask(__name__)  # cria o site
app.json.sort_keys = False
CORS(app, resources={r"*": {"origins": "*"}})

app.register_blueprint(ponto_blueprint)




##COMECA A API GERADA AUTOMATICAMENTE

#https://replit.taxidigital.net/Chamados


#Selecionar registros no EndPoint Chamados
@app.route("/Chamados")
def get_Chamados():
    resultado = Selecionar_TbChamados()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Chamados
@app.route('/Chamados', methods=['POST'])
def post_Chamados():
    payload = request.get_json()
    dtOperacao = payload ['dtOperacao']
    dsTipo = payload ['dsTipo']
    dsDescricao = payload ['dsDescricao']
    nrQtde = payload ['nrQtde']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbChamados(dtOperacao, dsTipo, dsDescricao, nrQtde, dsUser, dtRegistro)
    return "Cadastramento realizado com sucesso"
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbChamados
def deletar_TbChamados(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbChamados where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbChamados
def Alterar_TbChamados(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbChamados set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Cliente


#Selecionar registros no EndPoint Cliente
@app.route("/Cliente")
def get_Cliente():
    resultado = Selecionar_TbCliente()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Cliente
@app.route('/Cliente', methods=['POST'])
def post_Cliente():
    payload = request.get_json()
    dsNome = payload ['dsNome']
    nrCnpj = payload ['nrCnpj']
    nrIe = payload ['nrIe']
    nrInscMun = payload ['nrInscMun']
    dsLogradouro = payload ['dsLogradouro']
    nrNumero = payload ['nrNumero']
    dsComplemento = payload ['dsComplemento']
    dsBairro = payload ['dsBairro']
    dsCep = payload ['dsCep']
    dsCidade = payload ['dsCidade']
    dsUF = payload ['dsUF']
    dsObs = payload ['dsObs']
    cdStatus = payload ['cdStatus']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbCliente(dsNome, nrCnpj, nrIe, nrInscMun, dsLogradouro, nrNumero, dsComplemento, dsBairro, dsCep, dsCidade, dsUF, dsObs, cdStatus, dsUser, dtRegistro)
    return "Cadastramento realizado com sucesso"
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbCliente
def deletar_TbCliente(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbCliente where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbCliente
def Alterar_TbCliente(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbCliente set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Destinatario


#Selecionar registros no EndPoint Destinatario
@app.route("/Destinatario")
def get_Destinatario():
    resultado = Selecionar_TbDestinatario()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Destinatario
@app.route('/Destinatario', methods=['POST'])
def post_Destinatario():
    payload = request.get_json()
    dsNome = payload ['dsNome']
    nrCnpj = payload ['nrCnpj']
    nrIe = payload ['nrIe']
    nrInscMun = payload ['nrInscMun']
    dsLogradouro = payload ['dsLogradouro']
    nrNumero = payload ['nrNumero']
    dsComplemento = payload ['dsComplemento']
    dsBairro = payload ['dsBairro']
    dsCep = payload ['dsCep']
    dsCidade = payload ['dsCidade']
    dsUF = payload ['dsUF']
    dsObs = payload ['dsObs']
    cdStatus = payload ['cdStatus']
    dsLat = payload ['dsLat']
    dsLong = payload ['dsLong']
    nrRaio = payload ['nrRaio']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbDestinatario(dsNome, nrCnpj, nrIe, nrInscMun, dsLogradouro, nrNumero, dsComplemento, dsBairro, dsCep, dsCidade, dsUF, dsObs, cdStatus, dsLat, dsLong, nrRaio, dsUser, dtRegistro)
    return "Cadastramento realizado com sucesso"
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbDestinatario
def deletar_TbDestinatario(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbDestinatario where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbDestinatario
def Alterar_TbDestinatario(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbDestinatario set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Dispositivo


#Selecionar registros no EndPoint Dispositivo
@app.route("/Dispositivo")
def get_Dispositivo():
    resultado = Selecionar_TbDispositivo()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Dispositivo
@app.route('/Dispositivo', methods=['POST'])
def post_Dispositivo():
    payload = request.get_json()
    dsDispositivo = payload ['dsDispositivo']
    dsModelo = payload ['dsModelo']
    dsDescricao = payload ['dsDescricao']
    dsObs = payload ['dsObs']
    dsLayout = payload ['dsLayout']
    nrChip = payload ['nrChip']
    cdStatus = payload ['cdStatus']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbDispositivo(dsDispositivo, dsModelo, dsDescricao, dsObs, dsLayout, nrChip, cdStatus, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbDispositivo
def deletar_TbDispositivo(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbDispositivo where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbDispositivo
def Alterar_TbDispositivo(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbDispositivo set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Imagens


#Selecionar registros no EndPoint Imagens
@app.route("/Imagens/<codigo>")
def get_Imagens(codigo):
    resultado = Selecionar_TbImagens(codigo)
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Imagens
@app.route('/Imagens', methods=['POST'])
def post_Imagens():
    payload = request.get_json()
    dsCaminho = payload ['dsCaminho']
    cdCodigo = payload ['cdCodigo']
    cdTipo = payload ['cdTipo']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    cdProduto = payload ['cdProduto']
    nrImagem = payload ['nrImagem']
    Inserir_TbImagens(dsCaminho, cdCodigo, cdTipo, dsUser, dtRegistro, cdProduto, nrImagem)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbImagens
def deletar_TbImagens(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbImagens where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbImagens
def Alterar_TbImagens(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbImagens set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Posicao


#Selecionar registros no EndPoint Posicao
@app.route("/Posicao")
def get_Posicao():
    resultado = Selecionar_TbPosicao()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Posicao
@app.route('/Posicao', methods=['POST'])
def post_Posicao():
    payload = request.get_json()
    dsModelo = payload ['dsModelo']
    dtData = payload ['dtData']
    dtHora = payload ['dtHora']
    dsLat = payload ['dsLat']
    dsLong = payload ['dsLong']
    nrTemp = payload ['nrTemp']
    nrBat = payload ['nrBat']
    nrSeq = payload ['nrSeq']
    dsArquivo = payload ['dsArquivo']
    cdDispositivo = payload ['cdDispositivo']
    dsEndereco = payload ['dsEndereco']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbPosicao(dsModelo, dtData, dtHora, dsLat, dsLong, nrTemp, nrBat, nrSeq, dsArquivo, cdDispositivo, dsEndereco, dsUser ,dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbPosicao
def deletar_TbPosicao(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbPosicao where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbPosicao
def Alterar_TbPosicao(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbPosicao set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Produto


#Selecionar registros no EndPoint Produto
@app.route("/Produto/<codigo>")
def get_Produto(codigo):
    resultado = Selecionar_TbProduto(codigo)
    return resultado

#FIM DA FUNÇÃO


cd = []

#Inserir registros no EndPoint Produto
@app.route('/Produto', methods=['POST'])
def post_Produto():
    payload = request.get_json()
    dsNome = payload ['dsNome']
    dsDescricao = payload ['dsDescricao']
    nrCodigo = payload ['nrCodigo']
    nrLarg = payload ['nrLarg']
    nrComp = payload ['nrComp']
    nrAlt = payload ['nrAlt']
    cdStatus = payload ['cdStatus']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    cd = (Inserir_TbProduto(dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, dsUser, dtRegistro))
    return jsonify(cd)
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbProduto
def deletar_TbProduto(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbProduto where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbProduto
def Alterar_TbProduto(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbProduto set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Relacionamento


#Selecionar registros no EndPoint Relacionamento
@app.route("/Relacionamento")
def get_Relacionamento():
    resultado = Selecionar_TbRelacionamento()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Relacionamento
@app.route('/Relacionamento', methods=['POST'])
def post_Relacionamento():
    payload = request.get_json()
    cdPai = payload ['cdPai']
    cdFilho = payload ['cdFilho']
    cdTipo = payload ['cdTipo']
    dsDescricao = payload ['dsDescricao']
    cdStatus = payload ['cdStatus']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbRelacionamento(cdPai, cdFilho, cdTipo, dsDescricao, cdStatus, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbRelacionamento
def deletar_TbRelacionamento(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbRelacionamento where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbRelacionamento
def Alterar_TbRelacionamento(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbRelacionamento set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Sensor


#Selecionar registros no EndPoint Sensor
@app.route("/Sensor")
def get_Sensor():
    resultado = Selecionar_TbSensor()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Sensor
@app.route('/Sensor', methods=['POST'])
def post_Sensor():
    payload = request.get_json()
    dsNome = payload ['dsNome']
    cdTipo = payload ['cdTipo']
    dsDescricao = payload ['dsDescricao']
    cdUnidade = payload ['cdUnidade']
    nrUnidadeIni = payload ['nrUnidadeIni']
    nrUnidadeFim = payload ['nrUnidadeFim']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbSensor(dsNome, cdTipo, dsDescricao, cdUnidade, nrUnidadeIni, nrUnidadeFim, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbSensor
def deletar_TbSensor(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbSensor where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbSensor
def Alterar_TbSensor(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbSensor set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Status


#Selecionar registros no EndPoint Status
@app.route("/Status")
def get_Status():
    resultado = Selecionar_TbStatus()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Status
@app.route('/Status', methods=['POST'])
def post_Status():
    payload = request.get_json()
    dsStatus = payload ['dsStatus']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbStatus(dsStatus, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbStatus
def deletar_TbStatus(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbStatus where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbStatus
def Alterar_TbStatus(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbStatus set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Tag


#Selecionar registros no EndPoint Tag
@app.route("/Tag")
def get_Tag():
    resultado = Selecionar_TbTag()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Tag
@app.route('/Tag', methods=['POST'])
def post_Tag():
    payload = request.get_json()
    dsDescricao = payload ['dsDescricao']
    dsConteudo = payload ['dsConteudo']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbTag(dsDescricao, dsConteudo, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbTag
def deletar_TbTag(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbTag where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbTag
def Alterar_TbTag(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbTag set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Ticket


#Selecionar registros no EndPoint Ticket
@app.route("/Ticket")
def get_Ticket():
    resultado = Selecionar_TbTicket()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Ticket
@app.route('/Ticket', methods=['POST'])
def post_Ticket():
    payload = request.get_json()
    dtOperacao = payload ['dtOperacao']
    dsAtendimento = payload ['dsAtendimento']
    nrAbertos = payload ['nrAbertos']
    nrFechados = payload ['nrFechados']
    nrPendentes = payload ['nrPendentes']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbTicket(dtOperacao, dsAtendimento, nrAbertos, nrFechados, nrPendentes, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbTicket
def deletar_TbTicket(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbTicket where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbTicket
def Alterar_TbTicket(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbTicket set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/TicketResumo


#Selecionar registros no EndPoint TicketResumo
@app.route("/TicketResumo")
def get_TicketResumo():
    resultado = Selecionar_TbTicketResumo()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint TicketResumo
@app.route('/TicketResumo', methods=['POST'])
def post_TicketResumo():
    payload = request.get_json()
    dtOperacao = payload ['dtOperacao']
    dsAtendimento = payload ['dsAtendimento']
    dsNaoAtribuido = payload ['dsNaoAtribuido']
    dsSemResolucao = payload ['dsSemResolucao']
    dsAtualizado = payload ['dsAtualizado']
    dsPendente = payload ['dsPendente']
    dsResolvido = payload ['dsResolvido']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbTicketResumo(dtOperacao, dsAtendimento, dsNaoAtribuido, dsSemResolucao, dsAtualizado, dsPendente, dsResolvido, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbTicketResumo
def deletar_TbTicketResumo(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbTicketResumo where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbTicketResumo
def Alterar_TbTicketResumo(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbTicketResumo set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Tipo


#Selecionar registros no EndPoint Tipo
@app.route("/Tipo")
def get_Tipo():
    resultado = Selecionar_TbTipo()
    return resultado

#FIM DA FUNÇÃO

def Selecionar_NrImagensMaior(codigo):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    if codigo == '0':
        comando = f'select  SUBSTRING_INDEX(cdCodigo, "-",1) as cdProduto, max(SUBSTRING_INDEX(SUBSTRING_INDEX(cdCodigo, "-",-1),".",1)) as nrMaior from DbIntelliMetrics.TbImagens where cdTipo = 10  group by cdProduto order by cdProduto'
    else:
        comando = f'select  SUBSTRING_INDEX(cdCodigo, "-",1) as cdProduto, max(SUBSTRING_INDEX(SUBSTRING_INDEX(cdCodigo, "-",-1),".",1)) as nrMaior from DbIntelliMetrics.TbImagens where cdTipo = 10 and cdCodigo = {codigo} group by cdProduto'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return  resultado

#Inserir registros no EndPoint Tipo
@app.route('/Tipo', methods=['POST'])
def post_Tipo():
    payload = request.get_json()
    dsDescricao = payload ['dsDescricao']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbTipo(dsDescricao, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbTipo
def deletar_TbTipo(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbTipo where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbTipo
def Alterar_TbTipo(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbTipo set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Unidade


#Selecionar registros no EndPoint Unidade
@app.route("/Unidade")
def get_Unidade():
    resultado = Selecionar_TbUnidade()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Unidade
@app.route('/Unidade', methods=['POST'])
def post_Unidade():
    payload = request.get_json()
    dsUnidade = payload ['dsUnidade']
    dsSimbolo = payload ['dsSimbolo']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbUnidade(dsUnidade, dsSimbolo, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbUnidade
def deletar_TbUnidade(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbUnidade where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbUnidade
def Alterar_TbUnidade(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbUnidade set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Usuario


#Selecionar registros no EndPoint Usuario
@app.route("/Usuario")
def get_Usuario():
    resultado = Selecionar_TbUsuario()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Usuario
@app.route('/Usuario', methods=['POST'])
def post_Usuario():
    payload = request.get_json()
    dsNome = payload ['dsNome']
    dsLogin = payload ['dsLogin']
    dsSenha = payload ['dsSenha']
    cdPerfil = payload ['cdPerfil']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbUsuario(dsNome, dsLogin, dsSenha, cdPerfil, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbUsuario
def deletar_TbUsuario(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbUsuario where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbUsuario
def Alterar_TbUsuario(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbUsuario set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Visita


#Selecionar registros no EndPoint Visita
@app.route("/Visita")
def get_Visita():
    resultado = Selecionar_TbVisita()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Visita
@app.route('/Visita', methods=['POST'])
def post_Visita():
    payload = request.get_json()
    cdCliente = payload ['cdCliente']
    cdVisitante = payload ['cdVisitante']
    dtData = payload ['dtData']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbVisita(cdCliente, cdVisitante, dtData, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbVisita
def deletar_TbVisita(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbVisita where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbVisita
def Alterar_TbVisita(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbVisita set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/Visitante


#Selecionar registros no EndPoint Visitante
@app.route("/Visitante")
def get_Visitante():
    resultado = Selecionar_TbVisitante()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Visitante
@app.route('/Visitante', methods=['POST'])
def post_Visitante():
    payload = request.get_json()
    dsNome = payload ['dsNome']
    nrTelefone = payload ['nrTelefone']
    nrDocumento = payload ['nrDocumento']
    dsEmail = payload ['dsEmail']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    Inserir_TbVisitante(dsNome, nrTelefone, nrDocumento, dsEmail, dsUser, dtRegistro)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.TbVisitante
def deletar_TbVisitante(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbVisitante where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbVisitante
def Alterar_TbVisitante(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbVisitante set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/TbPosicao


#Selecionar registros no EndPoint TbPosicao
@app.route("/TbPosicao")
def get_TbPosicao():
    resultado = Selecionar_TbPosicao()
    return resultado

#FIM DA FUNÇÃO







#Deletar registros da tabela DbIntelliMetrics.TbPosicao
def deletar_TbPosicao(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.TbPosicao where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.TbPosicao
def Alterar_TbPosicao(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.TbPosicao set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/TbProdutoTipo


#Selecionar registros no EndPoint TbProdutoTipo
@app.route("/TbProdutoTipo/<codigo>")
def get_TbProdutoTipo(codigo):
    resultado = Selecionar_VwTbProdutoTipo(codigo)
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint TbProdutoTipo
@app.route('/TbProdutoTipo', methods=['POST'])
def post_TbProdutoTipo():
    payload = request.get_json()
    dsNome = payload ['dsNome']
    dsDescricao = payload ['dsDescricao']
    nrCodigo = payload ['nrCodigo']
    nrLarg = payload ['nrLarg']
    nrComp = payload ['nrComp']
    nrAlt = payload ['nrAlt']
    cdStatus = payload ['cdStatus']
    cdDispositivo = payload ['cdDispositivo']
    dsDispositivo = payload ['dsDispositivo']
    dsModelo = payload ['dsModelo']
    DescDispositivo = payload ['DescDispositivo']
    dsObs = payload ['dsObs']
    dsLayout = payload ['dsLayout']
    nrChip = payload ['nrChip']
    StatusDispositivo = payload ['StatusDispositivo']
    Inserir_VwTbProdutoTipo(dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, cdStatus, cdDispositivo, dsDispositivo, dsModelo, DescDispositivo, dsObs, dsLayout, nrChip, StatusDispositivo)
    return payload
#FIM DA FUNÇÃO



#Deletar registros da tabela DbIntelliMetrics.VwTbProdutoTipo
def deletar_VwTbProdutoTipo(Campo, Dado):
    conexao = pythonProject.conecta_bd()
    cursor = conexao.cursor(dictionary=True)
    comando = f'delete from DbIntelliMetrics.VwTbProdutoTipo where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO


#Alterar registros da tabela DbIntelliMetrics.VwTbProdutoTipo
def Alterar_VwTbProdutoTipo(Campo, Dado, UpCampo, UpDado):
    conexao = pythonProject.conecta_bd()
    comando = f'update DbIntelliMetrics.VwTbProdutoTipo set  {UpCampo}="{UpDado}"  where {Campo}="{Dado}"  '
    cursor.execute(comando)
    conexao.commit()
#FIM DA FUNÇÃO
#https://replit.taxidigital.net/TbProdutoTotalStaus


#Selecionar registros no EndPoint TbProdutoTotalStaus
@app.route("/TbProdutoTotalStaus/<codigo>")
def get_TbProdutoTotalStaus(codigo):
    resultado = Selecionar_VwTbProdutoTotalStaus(codigo)
    return resultado

#FIM DA FUNÇÃO

#Selecionar registros no EndPoint TbProdutoTotalStaus

img = {"Imagens":[]}
status = {"Status":[]}
produto = {"Produto":[]}
resultado = []
#alunos = {"alunos": []}
@app.route("/TbProdutoTotal/<codigo>")
def get_TbProdutoTotal(codigo):

    #resultado = Selecionar_VwTbProdutoTotal(codigo)
    produto["Produto"] = Selecionar_VwTbProdutoTotal(codigo)
    status["Status"] = Selecionar_VwTbProdutoTotalStaus(codigo)
    img["Imagens"] = Selecionar_TbImagens(codigo)
    resultado.append(produto)
    resultado.append(status)
    resultado.append(img)
    return resultado

#FIM DA FUNÇÃO

#https://replit.taxidigital.net/TbPosicaoAtual


#Selecionar registros no EndPoint TbPosicaoAtual
@app.route("/TbPosicaoAtual")
def get_TbPosicaoAtual():
    resultado = Selecionar_VwTbPosicaoAtual()
    return resultado

#FIM DA FUNÇÃO








#Inserir registros no EndPoint TbProdutoTotalStaus
@app.route('/TbProdutoTotalStaus/', methods=['POST'])
def post_TbProdutoTotalStaus():
    payload = request.get_json()
    dsNome = payload ['dsNome']
    dsDescricao = payload ['dsDescricao']
    nrCodigo = payload ['nrCodigo']
    nrLarg = payload ['nrLarg']
    nrComp = payload ['nrComp']
    nrAlt = payload ['nrAlt']
    Status = payload ['Status']
    nrQtde = payload ['nrQtde']
    Inserir_VwTbProdutoTotalStaus(dsNome, dsDescricao, nrCodigo, nrLarg, nrComp, nrAlt, Status, nrQtde)
    return payload
#FIM DA FUNÇÃO

#https://replit.taxidigital.net/Funcionario


#Selecionar registros no EndPoint Funcionario
@app.route("/Funcionario")
def get_Funcionario():
    resultado = Selecionar_TbFuncionario()
    return resultado

#FIM DA FUNÇÃO



#Inserir registros no EndPoint Funcionario
@app.route('/Funcionario', methods=['POST'])
def post_Funcionario():
    payload = request.get_json()
    dsBairro = payload ['dsBairro']
    dsCidade = payload ['dsCidade']
    dsComplemento = payload ['dsComplemento']
    dsFuncao = payload ['dsFuncao']
    dsLogradouro = payload ['dsLogradouro']
    dsNomeEmpregado = payload ['dsNomeEmpregado']
    dsNumCasa = payload ['dsNumCasa']
    dsUser = payload ['dsUser']
    dtRegistro = payload ['dtRegistro']
    nrCodEmpregado = payload ['nrCodEmpregado']
    TbFuncionariocol = payload ['TbFuncionariocol']
    Inserir_TbFuncionario(dsBairro, dsCidade, dsComplemento, dsFuncao, dsLogradouro, dsNomeEmpregado, dsNumCasa, dsUser, dtRegistro, nrCodEmpregado, TbFuncionariocol)
    return payload
#FIM DA FUNÇÃO






#FIM DA FUNÇÃO
#Fim do Gerador de API

## atulizado em 04052024
##  FIM DA API GERADA AUTOMATICAMENTE###


@app.route('/Foto', methods=['POST'])
def post_Foto():
    payload = request.get_json()
    imgFoto = payload ['imgFoto']
    dsFoto = payload['dsFoto']
    photo_data = base64.b64decode(imgFoto)
    with open(dsFoto, "wb") as fh:
        fh.write(photo_data)
    return payload
#FIM DA FUNÇÃO


@app.route('/CadastraImgProduto', methods=['POST'])
def CadastraImgProduto():

    file = request.files['arquivo']
    pathfile = (file.filename)
    cdProduto = pathfile.split("-")[0]
    nrImagem = pathfile.split("-")[1]
    nrImagem = nrImagem.split(".")[0]
    file.save(pathfile)
    upload_file(pathfile, "dbfilesintellimetrics", "produtos/"+pathfile)
    os.remove(pathfile)
    Inserir_TbImagens("produtos/", pathfile, "10", "TESTE", datetime.datetime.now(), cdProduto, nrImagem)
    return pathfile

@app.route('/upload', methods=['POST'])
def upload():
    # Verifica se há algum arquivo enviado na requisição
    if 'images' not in request.files:
        return 'Nenhum arquivo enviado', 400

    # Obtém a lista de arquivos enviados
    images = request.files.getlist('images')

    # Percorre a lista de arquivos
    for image in images:
        # Verifica se o arquivo é uma imagem válida
        if image.filename == '':
            return 'Nome de arquivo inválido', 400
        if not allowed_file(image.filename):
            return 'Tipo de arquivo inválido', 400

        # Grava a imagem no S3
        client = boto3.client('s3')
        client.upload_fileobj(image, 'dbfilesintellimetrics/produtos', image.filename)

    return 'Upload realizado com sucesso'

# Função auxiliar para verificar o tipo de arquivo permitido
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    #return "Cadastro ok "


@app.route('/Assinada', methods=['POST'])
def Assinada():
    payload = request.get_json()
    arquivo = payload['arquivo']
    result = assinar_arquivo(arquivo)
    return result

#Selecionar_NrImagensMaior

@app.route("/NrImagensMaior/<codigo>")
def get_NrImagensMaior(codigo):
    resultado = Selecionar_NrImagensMaior(codigo)
    return resultado

#https://replit.taxidigital.net/AcessoIntelBras





#app.run(port=8080, host='0.0.0.0', debug=True, threaded=True)
#app.run(host="0.0.0.0")  # coloca o site no ar#

def main():
    port = int(os.environ.get("PORT", 80))
    app.run(host="192.168.15.200", port=port)


if __name__ == "__main__":
    main()
