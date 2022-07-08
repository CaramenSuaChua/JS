'use strict'

const newsContainer = document.getElementById('news-container')
const btnPre = document.getElementById('btn-prev')
const btnNext = document.getElementById('btn-next')
const pageNum = document.getElementById('page-num')

const apiKey = "dccbe68d189c4bfb9a176106a11ab1d9";
// const apiKey = "dccbe68d189c4bfb9a176106a11ab1d9";
// const apiKey = 'a12ee94ca96a4a1db258c0769097a7d3'


const pageSize = JSON.parse(getFromStorage("page-size")) || "10";
const category = getFromStorage("category") || "business";

let totalResults =0;

//////////ham lay du lieu /////////////
const getDataNews = async function(country, page) {
    try {
    // Kết nối với API và lấy dữ liệu
    const res = await fetch(`https://newsapi.org/v2/top-headlines?country=${country}&category=${category}&pageSize=${pageSize}&page=${page}&apiKey=${apiKey}`
    );
    
   
    console.log(22)
        const data = await res.json()
        console.log(data)
        if(data.status !== 'error'){

            totalResults = data.totalResults;
            
            renderNewList(data.articles)
        } else { 
            alert('error API')
        }
    // Bắt lỗi
    } catch (err) {
    // thông báo lỗi
    alert("Error: " + err.message);
    }
}
///////// kiem tra nut previous /////////
const checkBTNPrev= function(e){
    
    console.log(pageNum.textContent)

    if(pageNum.textContent ==1){
        btnPre.style.display ='none';
    } else {
        btnPre.style.display = 'block'
    }
   
}
///////an nut previous lui ve/////////////
btnPre.addEventListener("click", function () {
    // Gọi hàm này để lấy dữ liệu và hiển thị danh sách các News trước đó
    getDataNews("us", --pageNum.textContent);
  });
  
  
  ///////////an nut next //////////
  btnNext.addEventListener("click", function () {
    // Gọi hàm này để lấy dữ liệu và hiển thị danh sách các News tiếp theo
    getDataNews("us", ++pageNum.textContent);   
  });

  ////////////kiem tra nut next
const checkBTNNext= function(e){

    console.log(pageNum.textContent)

    if(pageNum.textContent == Math.ceil(totalResults / pageSize )){
        btnNext.style.display ='none';
    } else {
        btnNext.style.display = 'block'
    }
    
    
}
//////////ham hien thi /////////////////
const renderNewList = function(data) {
    // console.log(data.status)
  // Kiểm tra xem có ấn các nút Next, Previous hay chưa và ấn đi
  checkBTNPrev();
  checkBTNNext();
  let html='';
    newsContainer.innerHTML='';
    for(let i=0; i < data.length; i++) {
        html+= 
             `<div class="card flex-row flex-wrap">
            <div class="card mb-3" style="">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <img src="${data[i].urlToImage}" class="card-img">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].title}</h5>
                            <p class="card-text">${data[i].description}</p>
                            <a href="${data[i].url}"
                                class="btn btn-primary">View</a>
                        </div>
                    </div>
                </div>
            </div>
        </div> `
       }
 newsContainer.innerHTML= html;
}

getDataNews("us", 1);