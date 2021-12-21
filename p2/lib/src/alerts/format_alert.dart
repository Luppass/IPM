import 'package:flutter/material.dart';

void format_alert(BuildContext context){

  showDialog(
      barrierDismissible: true,
      context: context,
      builder: (context) {
        return  AlertDialog(
          title:  const Text('ERROR', textAlign: TextAlign.center,),
          content: const Text('El formato ID introducido no es correcto!'),
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