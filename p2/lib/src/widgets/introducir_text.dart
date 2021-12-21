import 'package:flutter/material.dart';


Widget introduce_text(TextEditingController textController) {

  return Container(
      padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 3),
      child:  TextField(
        controller: textController,
        decoration: const InputDecoration(
          fillColor: Colors.white,
          hintText: "Introducir ID del edificio a controlar",
          filled: true,
        ),
      )
  );
}
