import 'package:flutter/material.dart';
import 'package:flutter_app/src/Functions/edificio_name_petition.dart';


Widget boton_buscar(BuildContext context, TextEditingController textController){

  String edificioBuscado;
  return RaisedButton(
    child: const Text("Buscar", style: TextStyle(fontSize: 25, color: Colors.white),),
    color: Colors.blueAccent, padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),

    onPressed: () => {
      edificioBuscado = textController.text,
      getPetition(edificioBuscado, context),
    },
  );
}
