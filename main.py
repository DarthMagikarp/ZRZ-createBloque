# chat conversation
import json
import pymysql
import requests
import http.client
import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")
    print("REQUEST: "+str(request.json))

    #try:
    cursor = connection.cursor()

    id_bloque = str(request.json['id_bloque'])
    tipo = str(request.json['tipo'])
    día = str(request.json['día'])
    fechaInicio = str(request.json['fechaInicio'])
    fechaFin = str(request.json['fechaFin'])
    repeticiones = str(request.json['repeticiones'])
    horaIni = str(request.json['horaIni'])
    horaFin = str(request.json['horaFin'])
    modalidad = str(request.json['modalidad'])
    frecuencia = str(request.json['frecuencia'])
    id_user = str(request.json['id_user'])
    
    sql_insertar = 'INSERT INTO '+DB_DDBB+'.disponibilidades'+'''
                    (id_bloque, tipo, día, fechaInicio, fechaFin, repeticiones, horaIni, horaFin, modalidad, frecuencia, id_user)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                    '''
    print('INSERT:'+sql_insertar)
    print(id_bloque, tipo, día, fechaInicio, fechaFin, repeticiones, horaIni, horaFin, modalidad, frecuencia, id_user)
    cursor.execute(sql_insertar,(id_bloque, tipo, día, fechaInicio, fechaFin, repeticiones, horaIni, horaFin, modalidad, frecuencia, id_user))
    connection.commit()

    retorno = {
            "estado":True,
            "detalle":"success!!"
        }

    #except Exception as e:
    #    print('Error: '+ str(e))
    #    retorno = {
    #        "estado":False,
    #        "detalle":"fail!!"
    #    }
    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')