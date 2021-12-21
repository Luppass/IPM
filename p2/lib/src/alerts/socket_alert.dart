import 'package:flutter/material.dart';


void socket_alert(BuildContext context){

  showDialog(
      barrierDismissible: true,
      context: context,
      builder: (context) {
        return  AlertDialog(
          title:  const Text('ERROR', textAlign: TextAlign.center,),
          content: const Text('No hay conexión a internet o la base de datos no responde!'),
          actions: [
            TextButton(
                child: const Text('Volver a intentar', style: TextStyle(color: Colors.blueAccent, fontSize: 17.0, fontWeight: FontWeight.bold)),
                onPressed: () {
                  Navigator.pop(context);
                }
            ),
          ],
        );
      }
  );
}