'use strict' ; 

/////////goi bien /////////////
const btnSearch = document.getElementById('btn-submit');
const inputSearch = document.getElementById('input-query');
const btnPre = document.getElementById("btn-prev");
const btnNext = document.getElementById("btn-next");
var pageNum = document.getElementById('page-num');

const newsContainer = document.getElementById("news-container");


// const apiKey = "dccbe68d189c4bfb9a176106a11ab1d9";
// const apiKey = "756cd85ac4dc45e185e27ef202194bb0";
const apiKey = 'a12ee94ca96a4a1db258c0769097a7d3'
const pageSize = JSON.parse(getFromStorage("page-size")) || "10";

////////////khai báo biến num/////////
var pageNum=Number(pageNum.innerHTML);
console.log(pageNum);
let totalResults =0;

////////an cac nut pre, num, next ///////////////
btnPre.style.display ='none';
btnNext.style.display ='none';
document.getElementById('page-num').style.display ='none';

////////////an nut search////////
btnSearch.addEventListener('click', function(){
    
    ///////////lay du lieu tu api ///////////////
    let searchData = inputSearch.value;
    if(searchData === ''){
        alert("Please fill information to search");
        return false;
    } else {
        const getDataNews = async function(){
            let res = await fetch(
                `https://newsapi.org/v2/everything?q=${searchData}&pageSize=${pageSize}&page=${pageNum}&apiKey=${apiKey}`)
            
                const data = await res.json()
                    console.log(data)
                    let item = data.articles
                    totalResults =data.totalResults;
                    renderNewList(item, data)
        }
        getDataNews(pageNum);
        //////////hien thi num///////////
        document.getElementById('page-num').style.display ='block';

        ///////an nut previous lui ve/////////////
        btnPre.addEventListener("click", function () {
            pageNum--
        // Gọi hàm này để lấy dữ liệu và hiển thị danh sách các News trước đó
        document.getElementById('page-num').innerHTML = pageNum
        getDataNews(pageNum);
        });     
        
        ///////////an nut next //////////
        btnNext.addEventListener("click", function () {
            // Gọi hàm này để lấy dữ liệu và hiển thị danh sách các News tiếp theo
            pageNum++
            document.getElementById('page-num').innerHTML = pageNum
            console.log()
            getDataNews( pageNum);   
        });

        ////////////kiem tra nut next
        const checkBTNNext= function(){

            console.log(pageNum);
            console.log(Math.ceil(totalResults / pageSize ));

            if(pageNum == Math.ceil(totalResults / pageSize )){
                btnNext.style.display ='none';
            } else {
                btnNext.style.display = 'block'
            }
            
        }
        ////////////kiem tra nut pre
        const checkBTNPrev= function(){

            console.log(pageNum)

            if(pageNum == 1){
                btnPre.style.display ='none';
            } else {
                btnPre.style.display = 'block'
            }
            
        }
        ///////////////hien thi 
        let renderNewList = function(item, data){

            checkBTNNext();
            checkBTNPrev();
            newsContainer.innerHTML='';
            let html='';
            if (data.totalResults === 0) {
                html = "No result!";
              } else {   
                
                console.log(data)
                for(let i=0; i < item.length; i++) {
               html+= 
                    `<div class="card flex-row flex-wrap">
                   <div class="card mb-3" style="">
                       <div class="row no-gutters">
                           <div class="col-md-4">
                               <img src="${item[i].urlToImage}" class="card-img">
                           </div>
                           <div class="col-md-8">
                               <div class="card-body">
                                   <h5 class="card-title">${item[i].title}</h5>
                                   <p class="card-text">${item[i].description}</p>
                                   <a href="${item[i].url}"
                                       class="btn btn-primary">View</a>
                               </div>
                           </div>
                       </div>
                   </div>
               </div> `
              }
        newsContainer.innerHTML= html;
        }
    }
    }
});

