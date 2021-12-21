import 'package:flutter/material.dart';
import 'package:flutter_app/src/Alerts/data_insert_notvalid.dart';


import '../Functions/post_persona.dart';

class introducir_datos extends StatelessWidget{

  const introducir_datos({Key? key, required this.persona, required this.id, required this.edificio});

  final id;
  final persona;
  final edificio;

  Widget build(BuildContext context) {

    List<bool> isSelected = [false, false];
    isSelected: isSelected;

    String nombre = persona.split(",")[0] as String;
    nombre = nombre.substring(1, nombre.length);
    String apellido = persona.split(",")[1] as String;

    TextEditingController textControllerTemp = TextEditingController();

    String temperatura = "";
    String type = "";
    return Material(
      child: Container(
        decoration: const BoxDecoration(
          image: DecorationImage(
              image: AssetImage('assets/fondo-datos_waiting.jpg'),
              fit: BoxFit.cover),
        ),
        child: Center(
          child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children:  <Widget>[
                Text(nombre+apellido, style: const TextStyle(color: Colors.black, fontSize: 33.0, fontWeight: FontWeight.bold)),
                const SizedBox(height: 25),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 110, vertical: 3),
                  child: TextField(
                  controller: textControllerTemp,
                  decoration: const InputDecoration(
                    fillColor: Colors.white,
                    hintText: " Temperatura",
                    filled: true,
                    prefixIcon: Icon(Icons.thermostat),
                  ),

                ),
                ),
                const SizedBox(height: 25),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 110, vertical: 3),
                    child: ToggleButtons(
                      fillColor: Colors.white,
                      color: Colors.white,
                      splashColor: Colors.white,
                      children: const <Widget>[
                        Icon(Icons.check,
                            color: Colors.green, size: 15),
                        Icon(Icons.close_rounded,
                            color: Colors.red),

                      ],
                        isSelected: isSelected,
                        onPressed: (int index) {
                          isSelected[index] = !isSelected[index];
                          if(isSelected[0] == true){
                            type = "IN";
                          }else{
                            type = "OUT";
                          }
                      },
                    ),
                ),
                const SizedBox(height: 15),
                RaisedButton(
                  child: const Text("Registrar persona", style: TextStyle(fontSize: 20, color: Colors.black54)),
                  color: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 10),
                  splashColor: Colors.green,
                  onPressed: () => {
                    post_persona(context, persona, id, temperatura, type, edificio),
                  },
                ),
              ]
          ),
        ),
      ),
    );
  }
}