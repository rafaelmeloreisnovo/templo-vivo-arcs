import 'package:flutter/material.dart';
import 'egg_eater.dart';

void main() {
  runApp(const PsiOneApp());
}

class PsiOneApp extends StatelessWidget {
  const PsiOneApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ψONE Egg',
      theme: ThemeData(primarySwatch: Colors.deepPurple),
      home: const EggEater(),
    );
  }
}
