import 'package:flutter/material.dart';
import 'package:flutter_app/src/functions/lista_personas_petition.dart';
import 'package:flutter_app/src/pages/personas.dart';
import '../pages/listado_personas.dart';


Widget boton_verLista(BuildContext context, String id_edificio, String edificio) {

  return RaisedButton(
    child: const Text("Lista de personas", style: TextStyle(fontSize: 17, color: Colors.blueAccent),),
    color: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),

    onPressed: () async {
      List<Persona> aux =  await getPersonas(id_edificio, context) as List<Persona>;
      Navigator.push(context, MaterialPageRoute(builder: (context) => listado_personas(lista:  aux, edificio: edificio,)));
    },
  );
}
