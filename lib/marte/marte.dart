

import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;
import 'package:yaml/yaml.dart';

class MartePage extends StatefulWidget { const MartePage({super.key}); @override State<MartePage> createState()=>_MartePageState(); }

class _MartePageState extends State<MartePage> {
  Map<String, dynamic>? cfg;
  @override void initState(){ super.initState(); _loadCfg(); }
  Future<void> _loadCfg() async {
    final y = await rootBundle.loadString('assets/utopia_marte.yaml');
    final parsed = loadYaml(y);
    if (parsed is YamlMap) {
      cfg = Map<String, dynamic>.from(parsed);
    } else {
      cfg = {'raw': y};
    }
    setState(() {});
  }
  @override Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(title: const Text('RAFAELIA • Marte')),
      body: cfg==null ? const Center(child:CircularProgressIndicator())
        : ListView(
            padding: const EdgeInsets.all(16),
            children: const [
              _CardTitulo('Bandeira do Verbo Vivo', 'Ética mínima • Commons • Cristais'),
              _CardTitulo('Matéria', 'Pressão, Água, Solo, Radiação'),
              _CardTitulo('Energia', 'Potência útil, Mix, Dissipação'),
              _CardTitulo('Consciência', 'SNR semântico, Coerência'),
              _CardTitulo('Espírito', 'Alinhamento ético, Intenção pura'),
            ],
          ),
    );
  }
}

class _CardTitulo extends StatelessWidget{
  final String t,s; const _CardTitulo(this.t,this.s,{super.key});
  @override Widget build(BuildContext c)=>Card(
    child: ListTile(title: Text(t,style: const TextStyle(fontWeight: FontWeight.bold)),
    subtitle: Text(s)));
}
