import 'package:flutter/material.dart';

import 'package:flutter_app/src/Widgets/text_control_covid.dart';

import 'boton_buscar.dart';
import 'introducir_text.dart';



Widget cuerpo(BuildContext context, TextEditingController textController){
  return Container(
    decoration: const BoxDecoration(
      image: DecorationImage(
          image: AssetImage('assets/antecedentes-medicos-3d-celulas-virus-covid-19_1048-12662.jpg'),
          fit: BoxFit.cover),
    ),
    child: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Texto_introducir_edif(),
          const SizedBox(height: 25),
          introduce_text(textController),
          const SizedBox(height: 15),
          boton_buscar(context, textController),
        ],
      ),
    ),
  );
}