import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_app/src/Alerts/post_success.dart';
import 'package:http/http.dart' as http;
import '../Alerts/format_alert.dart';
import '../Alerts/http_alert.dart';
import '../Alerts/socket_alert.dart';

Future<void> post_persona(BuildContext context, var persona, var idedicio, var temperatura, var type, var edificio) async {

  //--------------------------PARSING------------------------------
  DateTime date = DateTime.now();
  String fecha = date.toString().split(".")[0];
  fecha = fecha.replaceAll(" ", "T");
  fecha = fecha + ".277923+00:00";

  String nombre = persona.split(",")[0] as String;
  nombre = nombre.substring(1, nombre.length);
  String apellido = persona.split(",")[1] as String;
  apellido = apellido.replaceAll(" ", "");

  String uuid = persona.split(",")[2] as String;
  uuid = uuid.replaceAll(" ", "");
  uuid = uuid.replaceAll("}", "");

  //--------------------------PETITION------------------------------
  var data = {
    "user_id": uuid,
    "facility_id": idedicio,
    "timestamp": fecha,
    "type": type,
    "temperature": temperatura,
  };

  try {
    var url = Uri.parse('http://10.0.2.2:8080/api/rest/access_log');
    await http.post(url,
      headers: {"x-hasura-admin-secret": "myadminsecretkey",},
      body: jsonEncode(data),
    );
  } on SocketException{
    socket_alert(context);
  } on HttpException {
    http_alert(context);
  } on FormatException {
    format_alert(context);
  }
  post_success(context, nombre, apellido, edificio, idedicio);
}
