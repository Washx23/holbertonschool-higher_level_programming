// documents
var addItemButton = document.getElementById("add_item");

var myList = document.querySelector(".my_list");

addItemButton.addEventListener("click", function() {
  var newItem = document.createElement("li");
  
  newItem.textContent = "Item";
  
  myList.appendChild(newItem);
});
