// documents
var redHeader = document.getElementById("red_header");

redHeader.addEventListener("click", function() {
  var headerElement = document.querySelector("header");

  headerElement.classList.add("red");
});
