

const input = document.querySelector("input[name='sentence']");
const to_edit = document.querySelector("h1");
const form = document.querySelector("form")

form.addEventListener("submit", function(event) {event.preventDefault()});

function checkGrammar(event){
  const params = new URLSearchParams({"sentence" : input.value});
  fetch('/grammar?'+params)
    .then(response => response.json())
    .then(data => to_edit.innerHTML=data["sentence"]);
}