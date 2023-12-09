import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:transito_ui/services/consult.dart';
import 'package:transito_ui/widgets/cardMulta.dart';

class list_multas extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    ScrollController _scrollController = ScrollController();
    _scrollController.addListener(() {
      if (_scrollController.position.pixels == _scrollController.position.maxScrollExtent) {
        MultasProvider().fetchMultas();
      }
    });

    return ChangeNotifierProvider(
      create: (_) => MultasProvider(),
      child: Consumer<MultasProvider>(
        builder: (context, provider, child) {
          if (provider.multas.isEmpty) {
            provider.fetchMultas();
            return CircularProgressIndicator();
          } else {
            return Column(
              children: [
                ElevatedButton(
                  onPressed: () async  {
                    provider.fetchMultas();
                    
                  },
                  child: Text('Actualizar'),
                ),
                Expanded(
                  child: ListView.builder(
                    controller: _scrollController,


                    itemCount: provider.multas.length,
                    itemBuilder: (context, index) {
                      final multa = provider.multas[index];
                      return MultaCard(multa);

                    },

                  ),
                ),
              ],
            );
          }
        },
      ),
    );


  }

}

