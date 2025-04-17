// This is a direct copy of the sample we had from class

//Load the express module
const express = require('express');
const path = require('path');

//Put new express app inside an app variable
const app = express();

// Set up axios so we can make calls to the website
const axios = require('axios');

//Set views property and view engine
app.set("views", path.resolve(__dirname, "views"));
app.set("view engine", "ejs");

// Setup body parser
const bodyParser  = require('body-parser');
app.use(bodyParser.urlencoded());

// setup query string
var querystring = require('querystring');

// Store the logged in user
var username = '';
var password = '';
var authenticated = false;


// I copied this code from the Mozilla Firefox developer page
function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
}

app.get('/', function (req, res) {
    res.render("pages/index", {
        message: "David's Final Project"
    });
});

app.get('/login', function(req, res) {
    res.render("pages/login");
})

app.post('/login', function (req, res) {
    axios.post('http://127.0.0.1:5000/api/auth', querystring.stringify({
        'username': req.body.username,
        'password': req.body.password
    }), {
        Headers: {
            'content-type': 'application/x-www-form-urlencoded'
        }
    }).then((response) => {
        if (response.data == 'Authentication successful!') {
            //Save user session
            username = req.body.username;
            password = req.body.password;
            authenticated = true;
            res.render('pages/index', {
                message: 'Successful login!'
            })
        } else {
            res.render('pages/index', {
                message: 'Login failed!'
            })
        }

    })
})

app.get('/facilities', function (req, res) {
    if (authenticated) {
        axios.get('http://127.0.0.1:5000/api/facility/all', {
            params: {
                'username': username,
                'password': password
            }
        }).then((response) => {
                let facilities = response.data;
                console.log(response.data)
                res.render('pages/facilities', {
                    facilities : facilities
                });
            })
    } else {
        res.redirect('/login');
    }
})

app.post('/facilities/add', function (req, res) {
    if (authenticated) {
        axios.post('http://127.0.0.1:5000/api/facility', querystring.stringify({
            'username': username,
            'password': password,
            'name': req.body.name
        })).then((response) => {
                res.redirect('/facilities')
            })
    } else {
        res.redirect('/login');
    }
})

app.post('/facilities/delete/:id', function (req, res) {
    if (authenticated) {
        let id = req.params.id
        axios.delete('http://127.0.0.1:5000/api/facility', {
            params: {
                'username': username,
                'password': password,
                'id': id
            }
        }).then((response) => {
            res.redirect('/facilities')
            })
    } else {
        res.redirect('/login');
    }
})

app.get('/classrooms', function (req, res) {
    if (authenticated) {
        axios.get('http://127.0.0.1:5000/api/classroom/all', {
            params: {
                'username': username,
                'password': password
            }
        }).then((response) => {
                let classrooms = response.data;

                res.render('pages/classrooms', {
                    classrooms : classrooms
                });
            })
    } else {
        res.redirect('/login');
    }
})

app.post('/classrooms/add', function (req, res) {
    if (authenticated) {
        axios.post('http://127.0.0.1:5000/api/classroom', querystring.stringify({
            'username': username,
            'password': password,
            'name': req.body.name,
            'capacity': req.body.capacity,
            'facility': req.body.facility
        })).then((response) => {
                res.redirect('/classrooms')
            })
    } else {
        res.redirect('/login');
    }
})

app.post('/classrooms/delete/:id', function (req, res) {
    if (authenticated) {
        let id = req.params.id
        axios.delete('http://127.0.0.1:5000/api/classroom', {
            params: {
                'username': username,
                'password': password,
                'id': id
            }
        }).then((response) => {
            res.redirect('/classrooms')
            })
    } else {
        res.redirect('/login');
    }
})

app.get('/teachers', function (req, res) {
    if (authenticated) {
        axios.get('http://127.0.0.1:5000/api/teacher/all', {
            params: {
                'username': username,
                'password': password
            }
        }).then((response) => {
                let teachers = response.data;

                res.render('pages/teachers', {
                    teachers : teachers
                });
            })
    } else {
        res.redirect('/login');
    }
})

app.post('/teachers/add', function (req, res) {
    if (authenticated) {
        axios.post('http://127.0.0.1:5000/api/teacher', querystring.stringify({
            'username': username,
            'password': password,
            'firstname': req.body.firstname,
            'lastname': req.body.lastname,
            'room': req.body.room
        })).then((response) => {
                res.redirect('/teachers')
            })
    } else {
        res.redirect('/login');
    }
})

app.post('/teachers/delete/:id', function (req, res) {
    if (authenticated) {
        let id = req.params.id
        axios.delete('http://127.0.0.1:5000/api/teacher', {
            params: {
                'username': username,
                'password': password,
                'id': id
            }
        }).then((response) => {
            res.redirect('/teachers')
            })
    } else {
        res.redirect('/login');
    }
})

app.get('/children', function (req, res) {
    if (authenticated) {
        axios.get('http://127.0.0.1:5000/api/child/all', {
            params: {
                'username': username,
                'password': password
            }
        }).then((response) => {
                let children = response.data;
                
                res.render('pages/children', {
                    children : children
                });
            })
    } else {
        res.redirect('/login');
    }
})

app.post('/children/add', function (req, res) {
    if (authenticated) {
        axios.post('http://127.0.0.1:5000/api/child', querystring.stringify({
            'username': username,
            'password': password,
            'firstname': req.body.firstname,
            'lastname': req.body.lastname,
            'room': req.body.room,
            'age': req.body.age
        })).then((response) => {
                res.redirect('/children')
            })
    } else {
        res.redirect('/login');
    }
})

app.post('/children/delete/:id', function (req, res) {
    if (authenticated) {
        let id = req.params.id
        axios.delete('http://127.0.0.1:5000/api/child', {
            params: {
                'username': username,
                'password': password,
                'id': id
            }
        }).then((response) => {
            res.redirect('/children')
            })
    } else {
        res.redirect('/login');
    }
})

const port = 8080;

//Start the express application on port 8080 and print server start message on console
app.listen(port);
console.log("Application server started and listening on port 8080...");


