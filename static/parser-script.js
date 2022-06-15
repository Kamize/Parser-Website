

const input = document.querySelector("input[name='sentence']");
const form = document.querySelector("form");

form.addEventListener("submit", function(event) {event.preventDefault()});

function checkGrammar(event){
  const params = new URLSearchParams({"sentence" : input.value});
  fetch("/grammar?"+params)
    .then(response => response.json())
    .then(notify);
}

function notify(data){
  if(data["valid"]){
    document.querySelector(".incorrect-notify").hidden=true
    document.querySelector(".correct-notify").hidden=false
  } else {
    document.querySelector(".correct-notify").hidden=true
    document.querySelector(".incorrect-notify").hidden=false
  }
  document.querySelector("#stack_table").innerText = data["parse_stack"];
  document.querySelector("#input_table").innerText = data["parse_input"];
  document.querySelector("#notification").hidden=false;
}

// function responsive(){
//   var x = document.getElementById("myTopnav");
//   if (x.className === "topnav") {
//     x.className += " responsive";
//   } else {
//     x.className = "topnav";
//   }
// }