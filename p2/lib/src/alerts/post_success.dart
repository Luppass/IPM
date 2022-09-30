import 'package:flutter/material.dart';
import 'package:flutter_app/src/pages/menu_edificio.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';


import '../../main.dart';

void post_success(BuildContext context, String nombre, String apellido, String edificio, String id){

  showDialog(
      barrierDismissible: true,
      context: context,
      builder: (context) {
        return  AlertDialog(
          title: Text(AppLocalizations.of(context)!.done, textAlign: TextAlign.center,),
          content: Text(AppLocalizations.of(context)!.theUser + nombre+" "+ apellido + "\n" + AppLocalizations.of(context)!.registradoConExito, style: const TextStyle(fontSize: 18, color: Colors.black)),
          actions: [
            TextButton(
                child: Text(AppLocalizations.of(context)!.volverPrincipal, style: const TextStyle(color: Colors.blueAccent, fontSize: 17.0, fontWeight: FontWeight.bold)),
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context) => const MyHomePage()));
                }
            ),
            TextButton(
                child: Text(AppLocalizations.of(context)!.volverMenuEdif, style: const TextStyle(color: Colors.blueAccent, fontSize: 17.0, fontWeight: FontWeight.bold)),
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context) => menu_edificio(edificio: edificio, id: id)));
                }
            ),
          ],
        );
      }
  );
}