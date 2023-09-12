// documents

var toggleHeader = document.getElementById("toggle_header");

var headerElement = document.querySelector("header");

toggleHeader.addEventListener("click", function() {
  if (headerElement.classList.contains("red")) {
    headerElement.classList.remove("red");
    headerElement.classList.add("green");
  } else {
    headerElement.classList.remove("green");
    headerElement.classList.add("red");
  }
});
