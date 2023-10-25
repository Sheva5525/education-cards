function sendJSON() {

    if (passwordInput.value != passwordOut.value) {
        alert("Пароли не совпадают");
        return;
    }

    if (passwordInput.value.length < 7) {
        alert("Пароль меньше семи символов");
        return;
    }


    // с помощью jQuery обращаемся к элементам на странице по их именам
    let name = document.querySelector('#name');
    let lastname = document.querySelector('#lastname');
    // а вот сюда мы поместим ответ от сервера
    let result = document.querySelector('.result');
    // создаём новый экземпляр запроса XHR
    let xhr = new XMLHttpRequest();
    // адрес, куда мы отправим нашу JSON-строку
    let url = "http://mihailmaximov.ru/projects/json/json.php";
    // открываем соединение
    xhr.open("POST", url, true);
    // устанавливаем заголовок — выбираем тип контента, который отправится на сервер, в нашем случае мы явно пишем, что это JSON
    xhr.setRequestHeader("Content-Type", "application/json");
    // когда придёт ответ на наше обращение к серверу, мы его обработаем здесь
    xhr.onreadystatechange = function () {
      // если запрос принят и сервер ответил, что всё в порядке
    if (xhr.readyState === 4 && xhr.status === 200) {
        // выводим то, что ответил нам сервер — так мы убедимся, что данные он получил правильно
        result.innerHTML = this.responseText;
      }
    };
    // преобразуем наши данные JSON в строку
    var data = JSON.stringify({ "login": loginInput.value, "password": passwordInput.value });
    // когда всё готово, отправляем JSON на сервер
    xhr.send(data);
}

function qwe() {
    console.log("Login: " + loginInput.value);
    console.log("Password: " + passwordInput.value);
    console.log("Type password: " + typeof passwordInput.value);
}

function show_hide_password(target){

    var input = document.getElementById('passwordInput');

    if (input.getAttribute('type') == 'password') {

        target.classList.add('view');

        input.setAttribute('type', 'text');

    } else {

        target.classList.remove('view');

        input.setAttribute('type', 'password');

    }

    input = document.getElementById('passwordOut');

    if (input.getAttribute('type') == 'password') {

        target.classList.add('view');

        input.setAttribute('type', 'text');

    } else {

        target.classList.remove('view');

        input.setAttribute('type', 'password');

    }


    return false;

}