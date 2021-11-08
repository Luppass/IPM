import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Control de accesos COVID'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    final ButtonStyle style = ElevatedButton.styleFrom(textStyle: const TextStyle(fontSize: 30),
        minimumSize: Size(60, 65),
        primary: Colors.deepOrangeAccent);

    return Scaffold(
      body: cuerpo(),
    );
  }
}


Widget cuerpo(){
  return Container(
    decoration: const BoxDecoration(
      image: DecorationImage(image: NetworkImage("https://image.freepik.com/foto-gratis/antecedentes-medicos-3d-celulas-virus-covid-19_1048-12662.jpg"),
          fit: BoxFit.cover),
    ),
    child: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Texto_introducir_edif(),
          const SizedBox(height: 25,),
          introduce_text(),
          const SizedBox(height: 15,),
          boton_buscar(),
        ],
      ),
    ),
  );
}


Widget Texto_introducir_edif(){
  return const Text("Control COVID", style: TextStyle(color: Colors.white, fontSize: 30.0, fontWeight: FontWeight.bold));
}

Widget introduce_text() {
  return Container(
     padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 3),
      child: const TextField(
        decoration: InputDecoration(
          fillColor: Colors.white,
          hintText: "Introducir edificio a controlar",
          filled: true,
        ),
      )
  );
}

Widget boton_buscar(){
  return FlatButton(
      color: Colors.blueAccent,
      padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),
      onPressed: () {  },
      child: Text("Buscar", style: TextStyle(fontSize: 25, color: Colors.white),)
  );
}