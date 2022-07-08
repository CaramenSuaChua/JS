'use strict'

const btnSave = document.getElementById('btn-submit');
const inputPage = document.getElementById('input-page-size')
const inpCategory = document.getElementById('input-category')

btnSave.addEventListener('click', function(e){
    e.preventDefault();

    let pageSize = inputPage.value;
    let category = inpCategory.value
    if(!inputPage.value) {
        alert('Please input News per page')
        return false;
    }

    saveToStorage('page-size', pageSize)
    saveToStorage('category', category)

    alert('Save succesful'); 
    window.location.href = '../pages/news.html'
})

