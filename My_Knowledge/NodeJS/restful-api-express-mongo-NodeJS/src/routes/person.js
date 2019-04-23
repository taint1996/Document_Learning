let express = require('express');
let router = express.Router();

// QueryString => query property on the request object
// localhost:3000/person?name=taibeo&age=23
router.get('/person', (req, res) => {
	if (req.query.name)
	{
		res.send(`You have send request person ${req.query.name}`);
	}
	else {
		res.send("U have requested person");
	}
});

// Params property on the request object
router.get('/person/:name', (req, res) => {
	res.send(`You have requested params ${req.params.name}`);
});

router.get('/error', (req, res) => {
	throw new Error('This is a forced error')
});

module.exports = router;