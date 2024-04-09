const userName = JSON.parse(document.getElementById('json-username').textContent);
const studentName = JSON.parse(document.getElementById('json-student-username').textContent);


document.querySelector('#start-chat').onclick = function(e) {
    e.preventDefault()

    console.log({
        'username': userName,
        'student-username': studentName
    })

//    chatSocket.send(JSON.stringify({
//        'message': message,
//        'username': userName,
//        'room': roomName,
//        'user1': roomUser1,
//        'user2': roomUser2
//    }));

    return false
};