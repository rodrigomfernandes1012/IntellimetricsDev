from datetime import datetime
# SERVER API
import base64
from random import randrange

from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
import mysql.connector
import requests
import boto3
import os




#Amazon
selecao = []
dicionario = []
dic2 = []
dic_whats = []
dic_whats2 = []



token = "8c4EF9vXi8TZe6581e0af85c25"

def conecta_bd():
  conexao = mysql.connector.connect(
      host='dbintellimetrics.c3kc6gou2fhz.us-west-2.rds.amazonaws.com',
      user='admin',
      password='IntelliMetr!c$',
      database='DbIntelliMetrics')
  return conexao


def converte_horas(minutos):
    # minutos =  int(randrange(1, 59))
    horac = round((minutos / 60) * 100)
    return horac


def ImportarDados():
    try:
        nome_arquivo = input('Nome do arquivo a ser editado:')
        arquivo = open(nome_arquivo, 'r+')
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
        arquivo.writelines(u'Arquivo criado pois nao existia')
    # faca o que quiser
    arquivo.close()

#ImportarDados()


def ler_arquivo():
        arquivo2 = []
        with open("PREDILAR.fun", "r") as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas:
            nrCodEmpregado = (linha[0:6])
            dsNomeEmpregado = (linha[6:86])
            dsLogradouro = (linha[86:136])
            dsNumCasa = (linha[136:141])
            dsComplemento = (linha[141:156])
            dsBairro = (linha[156:176])
            dsCidade = (linha[176:196])
            dsFuncao = (linha[560:610])
            dsUser = "ROBO"
            dtRegistro = datetime.now().strftime("%d/%m/%Y")
            #print(dsNomeEmpregado)
            #arquivo.writelines()
            arquivo2.append(nrCodEmpregado + "\n")
        #return arquivo2

        print(arquivo2)

#ler_arquivo()

def exportar_arquivo():
    try:
        # Conecta ao banco de dados
        conn = conecta_bd()
        cursor = conn.cursor()

        # Consulta os dados da tabela produtos
        query = "SELECT nrCodEmpregado, dsNomeEmpregado nome FROM TbFuncionario"
        cursor.execute(query)

        # Obtém os resultados da consulta
        resultados = cursor.fetchall()

        # Gera o arquivo de texto
        with open('PREDILAR.ORIGEM_1.202405.txt', 'w') as arquivo:
            for nrCodEmpregado, dsNomeEmpregado in resultados:
                nr = nrCodEmpregado.zfill(10)
                local = "00000"
                evento = "00001"
                valor = "000000000003000"
                tipo = "01"
                data = "0000000000"
                descricao = "".ljust(50)
                status = "00"
                linha = f"{nr}{local}{evento}{valor}{tipo}{data}{descricao}{status}\n"
                arquivo.write(linha) # evento 1 salario
                nr = nrCodEmpregado.zfill(10)
                local = "00000"
                evento = "00017"
                valor = "000000000000255"
                tipo = "01"
                data = "0000000000"
                descricao = "".ljust(50)
                status = "00"
                linha = f"{nr}{local}{evento}{valor}{tipo}{data}{descricao}{status}\n"
                arquivo.write(linha) # evento 17 hora extra 50%
                nr = nrCodEmpregado.zfill(10)
                local = "00000"
                evento = "00038"
                valor = "0000000000000" + str(converte_horas((randrange(1, 59))))
                tipo = "01"
                data = "0000000000"
                descricao = "".ljust(50)
                status = "00"
                linha = f"{nr}{local}{evento}{valor}{tipo}{data}{descricao}{status}\n"
                arquivo.write(linha) # evento 38 atrasos e saidas em horas
                nr = nrCodEmpregado.zfill(10)
                local = "00000"
                evento = "00103"
                valor = "000000000000100"
                tipo = "01"
                data = "0000000000"
                descricao = "".ljust(50)
                status = "00"
                linha = f"{nr}{local}{evento}{valor}{tipo}{data}{descricao}{status}\n"
                if int(nr) % 2 == 0: # evento 103 falta dsr em dias não pode ser maior que 4 e apenas 1 por semana
                    arquivo.write(linha)
                nr = nrCodEmpregado.zfill(10)
                local = "00000"
                evento = "00039"
                valor = "000000000000100"
                tipo = "01"
                data = "0000000000"
                descricao = "".ljust(50)
                status = "00"
                linha = f"{nr}{local}{evento}{valor}{tipo}{data}{descricao}{status}\n"
                if int(nr) % 2 == 0:
                    arquivo.write(linha) # evento 39 faltas em dias no mes
        arquivo.close()
        print("Arquivo de texto gerado com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao acessar o banco de dados: {error}")

    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("Conexão com o banco de dados fechada.")

    # Chama a função para gerar o arquivo de texto

def justificado():
    texto = "123"
    texto_justificado = texto.rjust(8, "0")
    print(texto_justificado)



#gerar_arquivo_texto()

exportar_arquivo()

#texto = "123"
#texto_formatado = texto.zfill(18)
#print(texto_formatado)