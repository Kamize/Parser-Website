

const input = document.querySelector("input[name='sentence']"); // Input for API call
const form = document.querySelector("form");  // The form used for API call

form.addEventListener("submit", function(event) {event.preventDefault()});  // Prevents form from refreshing the page

function checkGrammar(event){
  const params = new URLSearchParams({"sentence" : input.value}); // Creating URL from input for API call
  // API call
  fetch("/grammar?"+params)
    .then(response => response.json()) // Creating JSON from API response
    .then(notify); // Notify the result in the web app
}

function notify(data){ // To notify the user the result of the API call
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