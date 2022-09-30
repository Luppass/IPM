import 'dart:core';
import 'package:flutter/material.dart';

import '../Widgets/boton_registrar.dart';
import '../Widgets/boton_verlista.dart';


class menu_edificio extends StatelessWidget {

  const menu_edificio({Key? key, required this.edificio, required this.id});

  final String id;
  final String edificio;

  @override
  Widget build(BuildContext context) {

    return Material(
      type: MaterialType.transparency,
      child: Container(
        decoration: const BoxDecoration(
          image: DecorationImage(
              image: AssetImage('assets/antecedentes-medicos-3d-celulas-virus-covid-19_1048-12662.jpg'),
              fit: BoxFit.cover),
        ),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(edificio, style: const TextStyle(color: Colors.white, fontSize: 22.0, fontWeight: FontWeight.bold)),
              const SizedBox(height: 25),
              boton_registrar(context, id, edificio),
              const SizedBox(height: 25),
              boton_verLista(context, id, edificio),
            ],
          ),
        ),
      ),
    );
  }
}


