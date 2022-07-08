'use strict'

const btnAdd = document.getElementById('btn-add') ; 
const todoContainer = document.getElementById('todo-container')
const inputTask = document.getElementById('input-task')
const todoList = document.getElementById("todo-list");

class Task {
    constructor(task,owner, isDone){
        this.task = task,
        this.owner = currentUserArr.userName,
        this.isDone = isDone
    }
}

//////////////các biến ở local ///////////////
const Key_Home = 'currentUserArray'; 
const currentUserArr = getFromStorage(Key_Home) ?JSON.parse(getFromStorage(Key_Home)) : [];

const Key = 'todoArray';
const todoArr = getFromStorage(Key) ?JSON.parse(getFromStorage(Key)): [];
console.log(todoArr)


////////////ấn nút add////////////
btnAdd.addEventListener('click',function(){
    if(!inputTask.value ) {
        alert('Please fill in the blank')
    } else {
    const taskArr = new Task(inputTask.value, currentUserArr.userName, false);
    todoArr.push(taskArr);
    console.log(taskArr)
    saveToStorage(Key , JSON.stringify(todoArr));
    renderTask(todoArr);
    // Xóa dữ liệu trong ô nhập
    inputTask.value = "";
    }
} );

///////////ham ấn ẩn hiện các task///////
const eventTog = function(){
document.querySelectorAll('#todo-list li').forEach(Tog => {
    Tog.addEventListener('click', function(){
        console.log(this)
    // console.log(this.getAttribute('data'))
    Tog.classList.toggle('checked');
    Tog.isDone = Tog.classList.contains("checked") ? true : false;
    saveToStorage(Key, JSON.stringify(todoArr));
    });
});
}

//////////hàm xóa các task/////////////
const deleteTask = function() {
document.querySelectorAll('#todo-list .close').forEach((TogCl, k) => {
    TogCl.addEventListener('click', function(event){
        event.stopPropagation();
        console.log(this)
        const isDelete = confirm('Are You Sure')

        if(isDelete){
            const index =
            todoArr.findIndex((item) => item.owner === currentUserArr.userName&&
            item.task === TogCl.parentElement.textContent.slice(0, 1)
            )
            console.log(index)

            todoArr.splice(k, 1);
            
            saveToStorage(Key, JSON.stringify(todoArr));
            renderTask(todoArr);
               
        }
    })
})
}

/////////ham hiền thị các task///////////
const renderTask = function(todoArr){
    let html = ''; 

    todoArr
    .filter(taskArr => taskArr.owner === currentUserArr.userName)
    .forEach((taskArr) => {
        html += `<li class="${taskArr.isDone }" data='${taskArr.task}'>
        ${taskArr.task}
         <span class="close" data='${taskArr.task}'>×</span></li>`
    } )
    
    todoList.innerHTML = html; 
    eventTog();
    deleteTask();
}

renderTask(todoArr)