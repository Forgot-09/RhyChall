const express = require('express')
const net = require('net')
const app = express()
const port = 2344

var server = net.createServer(function(socket) {
    console.log('클라이언트 접속');
    socket.write('Welcome to Socket Server');

    socket.on('data', function(chunk) {
        console.log('클라이언트가 보냄 : ',
        chunk.toString());
    });

    socket.on('end', function() {
        console.log('클라이언트 접속 종료');
    });
});

server.on('listening', function() {
    console.log('Server is listening');
});

server.on('close', function() {
    console.log('Server closed');
});

server.listen(3000);
/*
app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})*/