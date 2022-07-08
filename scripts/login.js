'use strict'

const btnLogin = document.getElementById('btn-submit')
const inputUserName = document.getElementById('input-username');
const inputPassWord = document.getElementById('input-password')

const Key = 'currentUserArray'; 
let currentUserArr = JSON.parse(getFromStorage(Key)) ?? [];
const KEY = "userArray";
const userArr = JSON.parse(getFromStorage(KEY)) || [];


/////////khai bao user//////////////////
class User {
    constructor(userName, password) {
        this.userName = userName;
        this.password = password;
    }
}

//////////ham lafm moi////////////
const clearForm = function(){
    inputUserName.value = '';
    inputPassWord.value = '';
}
///////an nut login
btnLogin.addEventListener("click", function () {
    let currentUserArr = inputUserName.value;
    
    // Valide dữ liệu
    // Thiếu username
    if (inputUserName.value === "") {
      alert("Please input username");
      return false;
    }
    // Thiếu password
    if (inputPassWord.value === "") {
      alert("Please input password");
      return false;
    }
    
    // Sai mật khẩu
    for (let i = 0; i < userArr.length; i++) {
      if (
        inputUserName.value === userArr[i].userName &&
        inputPassWord.value !== userArr[i].password
      ) {
        alert("Wrong password!");
        return false;
      }
    }
    // Tìm người dùng nhập so sánh với trong useArr
    currentUserArr = userArr.find(
      (user) =>
        user.userName === inputUserName.value &&
        user.password === inputPassWord.value
    );
    // Nếu username không tồn tại
    if (!currentUserArr) {
      alert("This username does not exists!");
       clearForm();
      return false;
    }
    // Đăng nhập thành công
    else {
      alert("Logged in successfully");
      saveToStorage(Key, JSON.stringify(currentUserArr))
      console.log(currentUserArr);
      window.location.href = "../index.html";
    }
  });
  