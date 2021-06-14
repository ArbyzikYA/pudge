//initial number of cookies    
var num = 0;

window.onload = function () {
        var name = prompt("What is your name");
        
        var space = document.getElementById("space");
        
        space.innerHTML = name + "'s Bakery";
}

var cookie = document.getElementById("cookie");

function cookieClick() { 
    num += 1;

    var numbers = document.getElementById("numbers");
    
    //upgrade level for printing
    var upgradeLevel = document.getElementById("upgradeLevel");
    
    numbers.innerHTML = num;      
    //automatic Granny upgrade to 2x
    if(num >= 30 ){
        num += 2;
        upgradeLevel.innerHTML = " BOOST X2 ";
    }

    //automatic factory upgrade to 10x
    if(num >= 500) {
        num += 10;
        upgradeLevel.innerHTML = "BOOST X3";
    }

    //automatic plant upgrade to 30x
    if(num >= 1000) {
        num += 30;
        upgradeLevel.innerHTML = "BOOST X4";
    }

    //automatic super factory upgrade to 1000x
    if(num >= 100000) {
        num += 1000;
        upgradeLevel.innerHTML = "BOOST X5";
    }
}
   document.getElementById("popup-btn").addEventListener("click", function(){
    document.getElementById("modal-area").style.display = "flex";
})

document.querySelector(".modal-close").addEventListener('click', function(){
    document.getElementById("modal-area").style.display = "none";
})
document.getElementById("popup-btn").addEventListener("click", function(){
    document.getElementById("modal-area").style.display = "flex";
})

document.querySelector(".modal-close").addEventListener('click', function(){
    document.getElementById("modal-area").style.display = "none";
})
