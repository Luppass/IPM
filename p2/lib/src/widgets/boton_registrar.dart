import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app/src/Alerts/qr_failed.dart';
import 'package:flutter_barcode_scanner/flutter_barcode_scanner.dart';
import 'introducir_datos.dart';


Widget boton_registrar(BuildContext context, String id, String edificio){

  var person = "Este QR no tiene asignado a ninguna persona";

  return RaisedButton(
    child: const Text("Registrar persona", style: TextStyle(fontSize: 17, color: Colors.white)),
    color: Colors.blueAccent, padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),
    onPressed: () async {
      try{
        person = await FlutterBarcodeScanner.scanBarcode('#ff6666', 'Cancel', true, ScanMode.QR);
        if(person.length < 20) {
          qr_failed(context);
        }else{
          await Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => introducir_datos(persona: person, id: id, edificio: edificio,))
          );
        }
      }on PlatformException{
        print("QR Internal Error");
      }
    }
  );
}