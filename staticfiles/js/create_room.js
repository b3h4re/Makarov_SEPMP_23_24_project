const userName = JSON.parse(document.getElementById('json-username').textContent);
const userId = JSON.parse(document.getElementById('json-user-id').textContent);
const studentName = JSON.parse(document.getElementById('json-student-username').textContent);


function CreateRequest()
{
    var Request = false;

    if (window.XMLHttpRequest)
    {
        //Gecko-совместимые браузеры, Safari, Konqueror
        Request = new XMLHttpRequest();
    }
    else if (window.ActiveXObject)
    {
        //Internet explorer
        try
        {
             Request = new ActiveXObject("Microsoft.XMLHTTP");
        }
        catch (CatchException)
        {
             Request = new ActiveXObject("Msxml2.XMLHTTP");
        }
    }

    if (!Request)
    {
        alert("Невозможно создать XMLHttpRequest");
    }

    return Request;
}


function SendRequest(r_method, r_path, r_args, r_handler) {
    //Создаём запрос
    var Request = CreateRequest();

    //Проверяем существование запроса еще раз
    if (!Request)
    {
        return;
    }

    //Назначаем пользовательский обработчик
    Request.onreadystatechange = function()
    {
        //Если обмен данными завершен
        if (Request.readyState == 4)
        {
            //Передаем управление обработчику пользователя
            r_handler(Request);
        }
    }

    //Проверяем, если требуется сделать GET-запрос
    if (r_method.toLowerCase() == "get" && r_args.length > 0)
    r_path += "?" + r_args;

    //Инициализируем соединение
    Request.open(r_method, r_path, true);

    if (r_method.toLowerCase() == "post")
    {
        //Если это POST-запрос

        //Устанавливаем заголовок
        Request.setRequestHeader("Content-Type","application/x-www-form-urlencoded; charset=utf-8");
        //Посылаем запрос
        Request.send(r_args);
    }
    else
    {
        //Если это GET-запрос

        //Посылаем нуль-запрос
        Request.send(null);
    }
}


document.querySelector('#start-chat').onclick = function(e) {
    e.preventDefault()



    console.log({
        'username': userName,
        'user-id': userId,
        'student-username': studentName
    })

    SendRequest("POST")

//    $.ajax({
//      type: 'POST',
//      url:'user/' + userId.toString() + '/start-chat',
//      data:{
//        'username': username,
//        'student-username': studentName
//      }
//      success.function(){
//        alert('created')
//      }
//    })

    return false
};