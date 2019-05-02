const Joi = require('joi');
const express = require('express');
const app = express();

app.use(express.json());

const courses = [
	{ id: 1, name: 'courses 1'},
	{ id: 2, name: 'courses 2'},
	{ id: 3, name: 'courses 3'},
	{ id: 4, name: 'courses 4'}
]

// HTTP Get Request
app.get('/', (req, res) => {
	res.send('Hello NodeJS');
})

app.get('/api/courses', (req, res) => {
	res.send(courses)
})

app.get('/api/courses/:id', (req, res) => {
	let course = courses.find(i => i.id === parseInt(req.params.id))

	if (!course) return res.status(404).send('The course with the give Id not found!'); // 404 error
	res.send(course);
})

app.get('/api/posts/:year/:month', (req, res) => {
	res.send(req.query)
})

// HTTP Post Request
app.post('/api/courses', (req, res) => {
	const { error } = validateCourse(req.body);

	if (error) return res.status(400).send(error.details[0].message);

	const course = {
		id: courses.length + 1,
		name: req.body.name
	};
	courses.push(course);
	res.send(course);
});

// HTTP Put request
app.put('/api/courses/:id', (req, res) => {	
	// Lookup the course
	// if not exist, return 404
	const course = courses.find(i => i.id === parseInt(req.params.id));

	if (!course) return res.status(404).send('The course with the given Id is Not found!');

	//  Validate
	// if invalid, return 400 - Bad request
	const { error } = validateCourse(req.body);
	if (error) return res.status(400).send(error.details[0].message);

	// update course
	// return update courses
	course.name = req.body.name;
	res.send(course);
});

// HTTP Delete 
app.delete('/api/courses/:id', (req, res) => {
	// Look up the course
	// not exist, return 404
	const course = courses.find(i => i.id === parseInt(req.params.id));

	if (!course) return res.status(404).send('The course with the given Id is Not found!');

	// Delete
	const index = courses.indexOf(course);	
	courses.splice(index, 1);

	// return the same course
	res.send(course);
});

const validateCourse = (course) => {
	const schema = {
		name: Joi.string().min(3).required()
	};

	return Joi.validate(course, schema);	
}

console.log(process.env.PORT);
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port}`));