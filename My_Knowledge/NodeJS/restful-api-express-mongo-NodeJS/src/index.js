let express = require("express");
let app = express()
let path = require('path');

app.use((req, res, next) => {
	console.log(`${new Date().toString()} => ${req.originalUrl}`);
	next();
})

let personRoute = require('./routes/person');
app.use(personRoute);
app.use(express.static('public'))

// Handler for 404 - Resource not found
app.use((req, res, next) => {
	res.status(404).send("We think you are lost!")
});

// Handler for Error 500
app.use((err, req, res, send) => {
	console.error(err.stack);
	res.sendFile(path.join(__dirname, '../public/500.html'))
})

const PORT = process.env.port || 3000;
app.listen(PORT, console.log(`Server has started at ${PORT}`));