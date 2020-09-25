var fname = document.querySelector("#fname")
var sname = document.querySelector("#lname")
var button = document.querySelector("#test")
var label = document.querySelector("#label")

window.addEventListener("load", function(){
    button.addEventListener("click", function() {
        label.innerHTML = "Hello " + fname.value + " " + lname.value
    })
})



