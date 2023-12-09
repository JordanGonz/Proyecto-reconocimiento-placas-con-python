import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:transito_ui/widgets/image_placas.dart';
import 'package:transito_ui/widgets/list_multas.dart';
import 'package:transito_ui/widgets/placaReal.dart';


class Homescreen extends StatelessWidget {
  const Homescreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    return Row(
      children: [

        Container(
          width: MediaQuery.of(context).size.width * 0.3,
          height: MediaQuery.of(context).size.height ,
          color: Colors.white,
          child: list_multas(),

        ),

        Container(
          width: MediaQuery.of(context).size.width * 0.2,
          height: MediaQuery.of(context).size.height ,
          color: Colors.white,
          child: list_multas2(),

        ),
        Container(
          width: MediaQuery.of(context).size.width * 0.5,
          height: MediaQuery.of(context).size.height ,
          color: Colors.blue,
          child: MyImageListWidget()
        ),

      ],
    );
  }
}
