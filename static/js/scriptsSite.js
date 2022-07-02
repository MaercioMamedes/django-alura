function toEmail(){
    var label = document.querySelector("#label-login");
    var inputLogin = document.querySelector("#user_login");

    inputLogin.placeholder='Entre com o usuário cadastrado';
    label.innerText = 'E-mail';
}