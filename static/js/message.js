const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const roomUser1 = JSON.parse(document.getElementById('json-roomuser1').textContent);
const roomUser2 = JSON.parse(document.getElementById('json-roomuser2').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
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
        'user1': roomUser1,
        'user2': roomUser2
    })

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName,
        'user1': roomUser1,
        'user2': roomUser2
    }));

    messageInputDom.value = '';

    return false
};


function scrollToBottom() {
    let objDiv = document.getElementById("chat-messages");
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();