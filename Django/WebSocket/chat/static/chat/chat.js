var roomId = document.querySelector('.roomId').innerText;
var connectionString = 'ws://' + window.location.host + '/chat/' + roomId + "/"
var chatSocket = new WebSocket(connectionString);
var btn = document.querySelector('.btn');
var input = document.querySelector('#message');
var user = document.querySelector('#user');
var messageBox = document.querySelector('.messageBox');

btn.onclick = function(){
    send_message(input.value);
}
function addMessage(message) {
            var newItem = document.createElement('LI');
            var text = document.createTextNode(message);
            newItem.append(text);
            messageBox.append(newItem);
        }

function send_message(message){
    let data = {
        "message": message,
    };
    chatSocket.send(JSON.stringify(data));
}


function connect() {
    chatSocket.onopen = function open() {
        alert('Connection established.');
    };

    chatSocket.onclose = function (e) {
        alert("Connection could not be established with host.You may not be allowed to join this chat.");
    };

    chatSocket.onmessage = function (e) {
        let data = JSON.parse(e.data);
        data = data["payload"];
        let event = data['event'];
        let message = data['message'];
        let username = data['username'];
        switch (event) {
            case "NewMessage":
                addMessage(username+"--> "+message);
                break;

            case "userandchatlog":
                let chatlog = data['chatlog'];
                user.innerText = username;
                chatlog.split('\n').forEach(addMessage);
                break;

            case "Joined":
                addMessage(username+' Connected')
                break;

            case "Disconnected":
                addMessage(username+" Disconnected!");
                break;
        }
    };


    if (chatSocket.readyState == WebSocket.OPEN) {
        chatSocket.onopen();
    }
}

connect();
