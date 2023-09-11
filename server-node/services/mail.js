const nodemailer = require('nodemailer');


const transporter = nodemailer.createTransport({
    service: 'Gmail',
    auth: {
      user: 'guidoroberto.25@gmail.com',
      pass: 'awzzeaeokqlnxlbn'
    }
  });


module.exports = transporter;