import express from "express";
import morgan from "morgan";
import cors from "cors";
import entititys from "./routes/multa.js";




const app = express();
app.use(morgan("dev"));
app.use(express.json());
app.use(cors({
  origin: '*',
  methods: ['GET', 'PUT', 'DELETE', 'PATCH', 'POST'],
  allowedHeaders: 'Content-Type, Authorization, Origin, X-Requested-With, Accept'
}));


app.use("/",entititys)



app.use((req, res, next) => {
    const error = new Error("ERROR 404 NOT FOUND");
    error.status = 404;
    next(error);
  });

  app.use((error, req, res, next) => {
    console.error(error.stack);
    res.status(error.status || 500).json({
      error: {
        message: error.message,
      },
    });
  });
  
  export default app;