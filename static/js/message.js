const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const roomUser = JSON.parse(document.getElementById('json-roomuser').textContent);
const roomStudent = JSON.parse(document.getElementById('json-roomstudent').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);
const chatSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/websockets/'
    + roomName
    + '/'
);

chatSocket.onclose = function(e) {
    console.log('onclose')
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    if (data.message) {
        document.querySelector('#chat-messages').innerHTML += ('<b>' + data.username + '</b>: ' + data.message + '<br>');
    } else {
        alert('The message was empty!')
    }

    scrollToBottom();
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    e.preventDefault()

    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    console.log({
        'message': message,
        'username': userName,
        'room': roomName,
        'user': roomUser,
        'student': roomStudent
    })

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName,
        'user': roomUser,
        'student': roomStudent
    }));

    messageInputDom.value = '';

    return false
};


function scrollToBottom() {
    let objDiv = document.getElementById("chat-messages");
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();
