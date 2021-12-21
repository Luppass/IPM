import 'package:flutter/material.dart';

void edificio_notfound(BuildContext context, String string){

  showDialog(
      barrierDismissible: true,
      context: context,
      builder: (context) {
        return  AlertDialog(
          title:  const Text('ERROR', textAlign: TextAlign.center,),
          content: string.isEmpty? const Text('Por favor, introduzca el ID del edificio') : Text('El ID del edificio introducido: '+ string +' no consta en la base de datos'),
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