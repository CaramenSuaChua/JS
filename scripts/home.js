'use strict'

const loginModal = document.getElementById('login-modal');
const mainContent = document.getElementById('main-content');
const btnLogout = document.getElementById('btn-logout')
const welcomeMessage = document.getElementById("welcome-message");
const newss = document.getElementById('newss') 

const Key = 'currentUserArray'; 
const currentUserArr = JSON.parse(getFromStorage(Key)) ?? [];
const Key_Regis = 'userArray'
const userArr =JSON.parse(getFromStorage(Key_Regis)) ?? [];

class User {
    constructor(firstName, lastName, userName, password) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.userName = userName;
        this.password = password;
    }
}

const displayLog = function() {
 ////////chua dang nhap 
if (!currentUserArr.firstName  ) {
    loginModal.style.display = "block";
    mainContent.style.display = "none";
    console.log("no user");
    newss.style.display= 'none'
  }
  // da dang nhap //////////
  else {
    loginModal.style.display = "none";
    mainContent.style.display = "block";
    
    console.log("user logged in", currentUserArr);
    welcomeMessage.innerHTML = `Welcome ${userArr[0].userName}`;
    console.log(welcomeMessage.innerHTML)
  }
}
displayLog();

/////////an nut log out 
btnLogout.addEventListener('click', function(){
    const isLogout = alert('Are you sure')

    localStorage.removeItem('currentUserArray');
    console.log('success')
    // hien thi trang dang nhap////////////////
    displayLog()
    
    // ///////chuyen den trang tiep//////
    window.location.reload(true);
    window.location.href = 'pages/login.html';    
})
