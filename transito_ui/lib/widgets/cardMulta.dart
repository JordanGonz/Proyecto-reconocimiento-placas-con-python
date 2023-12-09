import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

import 'package:transito_ui/models/placas.dart';

class MultaCard extends StatelessWidget {
  final MultasResponse multa;

  MultaCard(this.multa);

  @override
  Widget build(BuildContext context) {
    final formattedDate = DateFormat('yyyy-MM-dd HH:mm').format(multa.fechaHoraInfraccion);

    return Card(
      elevation: 3,
      margin: EdgeInsets.symmetric(horizontal: 10, vertical: 6),
      child: ListTile(

        contentPadding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),

        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Placa: ${multa.placa}'),
            Text('Motivo: ${multa.motivo}'),
            Text('Fecha y Hora de Infracción: $formattedDate'),
            Text('Correo: ${multa.correo}'),
          ],
        ),
      ),
    );
  }
}
