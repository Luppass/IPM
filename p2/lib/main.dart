import 'package:flutter/material.dart';
import 'package:flutter_app/src/Widgets/cuerpo_inicial.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Control Covid',
      theme: ThemeData(
        primarySwatch: Colors.lightBlue,
      ),
      initialRoute: 'home',
      routes: {
        'home' : (context) =>  const MyHomePage(),
      },
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    TextEditingController textController = TextEditingController();
    return Scaffold(
      body: cuerpo(context, textController),
    );
  }
}




