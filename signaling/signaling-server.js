const WebSocket = require('ws');

const clientServer = new WebSocket.Server({ port: 9000 });
const gatewayServer = new WebSocket.Server({ port: 9001 });

let client = null;
let gateway = null;

clientServer.on('connection', (socket) => {
    console.log('Client connected');
    client = socket;

    socket.on('message', (message) => {
        if (gateway) {
            gateway.send(message);
        }
    });

    socket.on('close', () => {
        client = null;
    });
});

gatewayServer.on('connection', (socket) => {
    console.log('Gateway connected');
    gateway = socket;

    socket.on('message', (message) => {
        if (client) {
            client.send(message);
        }
    });

    socket.on('close', () => {
        gateway = null;
    });
});

console.log('Signaling Server Running (Client: 9000, Gateway: 9001)');