'use strict'

const btnRegister = document.getElementById('btn-submit');
const inputFirstName = document.getElementById('input-firstname')
const inputLastName = document.getElementById('input-lastname')
const inputUserName = document.getElementById('input-username')
const inputPassWord1 = document.getElementById('input-password')
const inputPassWord2 = document.getElementById('input-password-confirm')

const Key_Regis = 'userArray'
const userArr =JSON.parse(getFromStorage(Key_Regis)) ?? [];

////////////khai bao class uer///////////
class User {
    constructor(firstName, lastName, userName, password) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.userName = userName;
        this.password = password;
    }
}

const validateData = function(){

    const firstNameValue = inputFirstName.value.trim();
    const lastNameValue = inputLastName.value.trim();
    const userNameValue = inputUserName.value.trim();
    const passwordValue1 = inputPassWord1.value.trim();
    const passwordValue2 = inputPassWord2.value.trim();

    for (let i = 0; i < userArr.length; i++) {
        if (userArr[i].userName === userNameValue) {
          alert("UserName existed!");
          return false;
        }
      }
    if(firstNameValue ===''){
        alert( 'FirstName cannot be blank')
    } else if(lastNameValue === '') {
        alert('LastName cannot be blank')
        return false;
    } else if (userNameValue === ''){
        alert ('UserName cannot be blank')
        return false;
    } else if (passwordValue1 === ''   ) {
        alert ('PassWord cannot be blank')
        return false;
    }else if (passwordValue2 === '' ) {
        alert ('PassWord Confirm cannot be blank')
        return false;
    } else if ( passwordValue2 !== passwordValue1 ) {
        alert (' Password is different ')
        return false;
    } else if(passwordValue1 <= '8') {
        alert ('Password missing characters')
        return false;
    }
   return true;
}

const clearForm = function(){
    inputFirstName.value = '';
    inputLastName.value= '';
    inputUserName.value='';
    inputPassWord1.value = '';
    inputPassWord2.value = '';
}

btnRegister.addEventListener('click', function(e){
    e.preventDefault();
   validateData()
    
    console.log(e)
    const data = new User(inputFirstName.value, inputLastName.value, inputUserName.value, inputPassWord1.value, );
    
    if (validateData() ){
        console.log(validateData())
        userArr.push(data)
        saveToStorage(Key_Regis, JSON.stringify(userArr));
        alert("Register succesfully");
        window.location.href = '../pages/login.html';
    } else {
    alert('Not Found 404');
    clearForm()
    }   
})


