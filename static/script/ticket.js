let y = document.querySelector(".results_number");
let result = document.querySelector(".results");
let ticket= document.querySelector(".left_ticket");
let body= document.querySelector("body");
let mark= document.querySelector(".mark");
let message = document.querySelector(".message");
let try_num = 0;
let nameP= document.querySelector(".name");
let sex = document.querySelector(".sex");
let pclass= document.querySelector(".pclass");
let age= document.querySelector(".age");
let Ticket = document.querySelector(".Ticket");
let Cabin = document.querySelector(".Cabin");
let embarked = document.querySelector(".embarked");
let name_info = document.querySelector(".name_info");
let cabin_info = document.querySelector(".cabin_info");
let ticket_info = document.querySelector(".ticket_info");
let class_info = document.querySelector(".class_info");
let from_info = document.querySelector(".from_info");

name_info.innerText=nameP.innerText;
sex.innerText=sex.innerText;
class_info.innerText=pclass.innerText;
cabin_info.innerText=Cabin.innerText;
ticket_info.innerText=Ticket.innerText;
if(embarked.innerText =="S"){
    from_info.innerText = "SOUTHAMPTON";
}
if(embarked.innerText =="Q"){
    from_info.innerText = "QUEENSTOWN";
}

if(embarked.innerText =="C"){
    from_info.innerText = "CHERBOURG";
}

ticket.addEventListener("click",function(){
    console.log("clicked");
    if(try_num == 0){
        result.style.cssText = "display: flex; flex-direction: column; width: 100%; height: 100vh; justify-content: center; align-items:center;";
        try_num++;
    }
    
    if(parseInt(y.innerText) == 0){
        mark.src = "../static/img/no.svg";
        message.innerText = "unfortunately, You couldn't survive the disaster";
    }
    if(parseInt(y.innerText) == 1){
        mark.src = "../static/img/yes.svg";
        message.innerText = "Congratulations, You've survived the titanic disaster";
    }
    console.log(parseInt(y.innerText));
    result.scrollIntoView({behavior: 'smooth', block: 'end'});
})