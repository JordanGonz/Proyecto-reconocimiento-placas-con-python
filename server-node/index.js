
const multas = require('./routes/multa');
const express = require('express');
const cors = require('cors');


const app = express();
app.use(express.json());
//add cors 
app.use(cors({
  origin: '*',
  methods: ['GET', 'PUT', 'DELETE', 'PATCH', 'POST'],
  allowedHeaders: 'Content-Type, Authorization, Origin, X-Requested-With, Accept'
}));




app.use('/multas', multas);



app.listen(3000, () => {
  console.log('http://localhost:3000');
});




