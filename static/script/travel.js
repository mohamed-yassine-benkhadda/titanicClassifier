let form = document.querySelector("form");
let sex = document.querySelector(".sex")
let pic=document.querySelector(".pic");

form.addEventListener("click",function(){
    if(sex.value === "male"){
        pic.src = "../static/img/man-svgrepo-com.svg";
    }
    if(sex.value === "female"){
        pic.src = "../static/img/woman-svgrepo-com.svg";
    }
})

