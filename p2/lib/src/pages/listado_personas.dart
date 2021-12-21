import 'package:flutter/material.dart';
import 'package:flutter_app/src/pages/personas.dart';
import 'package:intl/intl.dart';
class listado_personas extends StatelessWidget {

  const listado_personas({Key? key, required this.lista, required this.edificio});

  final List<Persona> lista;
  final String edificio;

  @override
  Widget build(BuildContext context){
    List<Persona> aux = lista.reversed.toList();
    return Scaffold(
      appBar: AppBar(
        title: Text(edificio, style: const TextStyle(color: Colors.white, fontSize: 20.0, fontWeight: FontWeight.bold)),
      ),
      body: ListView.builder(
          itemCount: aux.length,
          itemBuilder: (BuildContext context, index) {
            return ListTile(
              title: Text(aux[index].name +" "+aux[index].surname+" "+aux[index].inOut , style: const TextStyle(color: Colors.black, fontSize: 15.0, fontWeight: FontWeight.bold)),
              subtitle: Text("Fecha: " + aux[index].date.toString().replaceAll("-", "/").split("T")[0] + " " + aux[index].date.toString().replaceAll("-", "/").split("T")[1].split(".")[0] +"\nemail: "+ aux[index].mail +"\nphone: "+aux[index].phone),

              leading: CircleAvatar(
                child: Text(aux[index].name.substring(0, 1)),
              ),
            );
          }
      ),
    );
  }
}
