// Select the element with id "red_header"
var redHeader = document.getElementById("red_header");


redHeader.addEventListener("click", function() {

  var headerElement = document.querySelector("header");

  headerElement.style.color = "#FF0000";
});
