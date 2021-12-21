import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_app/src/alerts/format_alert.dart';
import 'package:flutter_app/src/alerts/http_alert.dart';
import 'package:flutter_app/src/alerts/socket_alert.dart';
import 'package:flutter_app/src/pages/personas.dart';

import 'package:http/http.dart' as http;

Future<List<Persona>> getPersonas(String id_edificio, BuildContext context) async{

  List<Persona> listaPersonas = [];

  var url = Uri.parse('http://10.0.2.2:8080/api/rest/facility_access_log/'+id_edificio);

  try {
    final response = await http.get(url,
        headers: {"x-hasura-admin-secret": "myadminsecretkey",}
    );
    String body = utf8.decode(response.bodyBytes);
    final jsonData = jsonDecode(body);

    if (jsonData.toString().contains("bad-request")) {
      format_alert(context);
    }
    else {
      if (response.statusCode == 200) {
        for (var item in jsonData["access_log"]) {
          listaPersonas.add(Persona(item["user"]["name"], item["user"]["surname"], item["user"]["uuid"], item["user"]["phone"],
              item["user"]["email"], item["temperature"], item["timestamp"], item["type"], item["user"]["is_vaccinated"]));
        }
        return listaPersonas;
      }
      else {
        throw Exception("Error fatal");
      }
    }
  } on SocketException{
    socket_alert(context);
  } on HttpException {
    http_alert(context);
  } on FormatException {
    format_alert(context);
  }
  throw Exception("Error fatal");
}
