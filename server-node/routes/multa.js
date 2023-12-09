const db = require('../db/db.js');
const transporter = require('../services/mail.js');
const express = require('express');
const router = express.Router(); 





router.post('/multar', async (req, res) => {
  console.log("Respuesta", req.body);
  const { placa, motivo } = req.body; 
  const query = 'INSERT INTO multas (placa, motivo, correo, fecha_hora_infraccion) VALUES (?, ?, ?, NOW())';

  try {
    // Retrieve the corresponding owner's information from the propietario table
    const selectOwnerQuery = 'SELECT nombre, correo FROM propietario WHERE placa = ?';
    const [ownerResults] = await db.query(selectOwnerQuery, [placa]);

    if (ownerResults.length === 0) {
      // Owner not found
      return res.status(404).send('Owner not found');
    }

    const { nombre, correo } = ownerResults[0]; 

    // Insert multa into the table
    const [results] = await db.query(query, [placa, motivo, correo]);

    const mailOptions = {
      from: 'MUNICIPIO DE QUITO',
      to: correo,
      subject: 'Multa registrada',
      text: 'Se ha registrado una multa para su vehículo ' + placa,
    };

    transporter.sendMail(mailOptions, (mailErr, info) => {
      if (mailErr) {
        console.error('Error al enviar correo:', mailErr);
        res.status(500).send('Error al enviar correo');
      } else {
        console.log('Multa registrada y correo enviado:', results);
        res.status(200).send('Multa registrada y correo enviado');
      }
    });
  } catch (err) {
    console.error('Error al insertar multa:', err);
    res.status(500).send('Error al insertar multa');
  }
});


router.get('/multas', async (req, res) => {
  const query = 'SELECT * FROM multas';
  
  try {
    const [results, fields] = await db.execute(query);
    console.log('Multas obtenidas:', results);
    res.status(200).json(results);
  } catch (err) {
    console.error('Error al obtener multas:', err);
    res.status(500).send('Error al obtener multas');
  }
});

const handleServerError = (res, err) => {
  console.error('Error en el servidor:', err);
  res.status(500).send('Error en el servidor');
};

router.get('/propietario', async (req, res) => {
  const placa = req.query.placa;

  if (!placa || typeof placa !== 'string') {
    return res.status(400).json({ error: 'Placa inválida' });
  }

  try {
    const [results] = await db.execute('SELECT * FROM multas WHERE placa = ?', [placa]);

    if (results.length === 0) {
      return res.status(404).json({ message: 'No se encontró ningún propietario con la placa proporcionada' });
    }

    console.log('Propietario obtenido:', results);
    res.status(200).json(results);

    await db.execute(
      'INSERT INTO registro_consultas (placa) VALUES (?) ON DUPLICATE KEY UPDATE fecha_consulta = CURRENT_TIMESTAMP',
      [placa]
    );
    console.log('Consulta insertada en registro_consultas');
  } catch (err) {
    handleServerError(res, err);
  }
});



module.exports = router; 
