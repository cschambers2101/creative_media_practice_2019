var fname = document.querySelector("#fname")
console.log(fname)

var button = document.querySelector("#test")
console.log(button)
var label = document.querySelector("#label")


document.addEventListener("load", function(){
    button.addEventListener("click", function() {
        label.innerHTML = fname.value

    })
})



