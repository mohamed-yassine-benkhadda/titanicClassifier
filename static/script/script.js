let counters = document.querySelectorAll(".counter");
let vals = [];
for(let i = 0; i < counters.length; i++) {
    vals[i] = parseInt(counters[i].innerText);
    counters[i].innerText = 0;
    const updateCounter = ()=>{
        let c = +parseInt(counters[i].innerText);
        let increment = vals[i]/200;
        if(c<vals[i]){
            counters[i].innerText= `${Math.ceil(c+increment)} %`;
            setTimeout(updateCounter,2);
        }
    }
    updateCounter();
}

let path = document.querySelectorAll(".path");