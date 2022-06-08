

const input = document.querySelector("input[name='sentence']");
const to_edit = document.querySelector("#notification");
const form = document.querySelector("form");

form.addEventListener("submit", function(event) {event.preventDefault()});

function checkGrammar(event){
  const params = new URLSearchParams({"sentence" : input.value});
  fetch('/grammar?'+params)
    .then(response => response.json())
    .then(notify);
}

function notify(data){
  console.log(data["tokens"].join(" "));
  to_edit.innerText = data["tokens"].join(" ");
  to_edit.hidden=false;
}