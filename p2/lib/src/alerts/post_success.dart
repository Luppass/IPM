import 'package:flutter/material.dart';
import 'package:flutter_app/src/pages/menu_edificio.dart';

import '../../main.dart';

void post_success(BuildContext context, String nombre, String apellido, String edificio, String id){

  showDialog(
      barrierDismissible: true,
      context: context,
      builder: (context) {
        return  AlertDialog(
          title:  const Text('HECHO!', textAlign: TextAlign.center,),
          content: Text('El usuario: '+ nombre+" "+ apellido + "\nha sido registrado con éxito", style: const TextStyle(fontSize: 18, color: Colors.black)),
          actions: [
            TextButton(
                child: const Text('Volver a menú principal', style: TextStyle(color: Colors.blueAccent, fontSize: 17.0, fontWeight: FontWeight.bold)),
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context) => const MyHomePage()));
                }
            ),
            TextButton(
                child: const Text('Volver a menú edificio', style: TextStyle(color: Colors.blueAccent, fontSize: 17.0, fontWeight: FontWeight.bold)),
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context) => menu_edificio(edificio: edificio, id: id)));
                }
            ),
          ],
        );
      }
  );
}