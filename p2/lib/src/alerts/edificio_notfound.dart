import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';


void edificio_notfound(BuildContext context, String string){

  showDialog(
      barrierDismissible: true,
      context: context,
      builder: (context) {
        return  AlertDialog(
          title:  const Text('ERROR', textAlign: TextAlign.center,),
          content: string.isEmpty?  Text(AppLocalizations.of(context)!.idEdificio) : Text(AppLocalizations.of(context)!.notFoundEdificio),
          actions: [
            TextButton(
                child: Text(AppLocalizations.of(context)!.tryAgain, style: const TextStyle(color: Colors.blueAccent, fontSize: 17.0, fontWeight: FontWeight.bold)),
                onPressed: () {
                  Navigator.pop(context);
                }
            ),
          ],
        );
      }
  );
}