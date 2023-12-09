import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:transito_ui/services/consult.dart';
import 'package:transito_ui/widgets/cardMulta.dart';


class list_multas2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => MultasProvider(),
      child: Consumer<MultasProvider>(
        builder: (context, provider, child) {
          if (provider.multas.isEmpty) {
            provider.fetchMultas2();
            return CircularProgressIndicator();
          } else {
            return ListView.builder(
              itemCount: provider.multas.length,
              itemBuilder: (context, index) {
                final multa = provider.multas[index];
                return MultaCard(multa);
              },
            );
          }
        },
      ),
    );
  }
}