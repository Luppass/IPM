import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_app/src/Alerts/edificio_notfound.dart';
import 'package:flutter_app/src/Alerts/format_alert.dart';
import 'package:flutter_app/src/Alerts/http_alert.dart';
import 'package:flutter_app/src/Alerts/socket_alert.dart';
import 'package:http/http.dart' as http;

import '../pages/menu_edificio.dart';

Future<void> getPetition(String idEdificio, BuildContext context) async{

  var url = Uri.parse('http://10.20.38.89:8080/api/rest/facilities/'+idEdificio);

  try{
    final response = await http.get(url,
        headers: {"x-hasura-admin-secret": "myadminsecretkey",}
    );

    String body = utf8.decode(response.bodyBytes);
    final jsonData = jsonDecode(body);

    if (jsonData.toString().contains("bad-request")) {
      format_alert(context);
    }

    else{
      String nombreEdificio = "";

      for (var item in jsonData["facilities"]) {
        nombreEdificio = item["name"];
      }

      if (response.statusCode == 200 && idEdificio.isNotEmpty && nombreEdificio.isNotEmpty) {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => menu_edificio(edificio: nombreEdificio, id: idEdificio,))
            );
      }
      else{
        return edificio_notfound(context, idEdificio);
      }
    }
  }
    on SocketException{
      socket_alert(context);
    }
    on HttpException {
      http_alert(context);
    }
    on FormatException {
      format_alert(context);
    }
}





