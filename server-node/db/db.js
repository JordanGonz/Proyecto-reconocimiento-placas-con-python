const mysql = require('mysql2/promise'); 

const db = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "",
  port: "3306",
  database: "placas",
});

module.exports = db;
