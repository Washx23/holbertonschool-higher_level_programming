// documents
var updateHeaderButton = document.getElementById("update_header");

var headerElement = document.querySelector("header");

updateHeaderButton.addEventListener("click", function() {
  headerElement.textContent = "New Header!!!";
});
