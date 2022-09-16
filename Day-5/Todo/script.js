// References|Selectors
var todoInput = document.querySelector(".todo-input");
var btn = document.querySelector("button");
var todoList = document.querySelector(".todo-list");

// Event Handler
btn.onclick = create;
todoList.onclick = deletecomplt;

function create(e) {
  if (todoInput.value != "") {
    // propblem of page refreshing
    // prevent data to send to the server
    e.preventDefault();

    // Creating New Div
    var newDiv = document.createElement("div");
    newDiv.classList.add("todo");

    // Creating New Li
    var newLi = document.createElement("li");
    newLi.innerHTML = todoInput.value;
    newLi.classList.add("todo-item");
    newDiv.appendChild(newLi);

    // Creating New Complete Button
    var cmpltBtn = document.createElement("button");
    cmpltBtn.classList.add("cmplt-btn");
    cmpltBtn.innerHTML = '<i class="fa fa-check"></i>';
    newDiv.appendChild(cmpltBtn);

    // Creating New Delete Button
    var deleteBtn = document.createElement("button");
    deleteBtn.classList.add("delete-btn");
    deleteBtn.innerHTML = '<i class="fa fa-trash"></i>';
    newDiv.appendChild(deleteBtn);

    todoList.appendChild(newDiv);

    // to clear the text field
    todoInput.value = "";
  } else {
    alert("Input Field can't be BLANK");
  }
}

function deletecomplt(e) {
  console.log(e.target);

  var item = e.target;
  if (item.classList[0] == "delete-btn") {
    // logic to delete
    var parent = item.parentElement;

    console.log(parent);
    parent.remove();
  } else {
    if (item.classList[0] == "cmplt-btn") {
      // logic to complete
      var parent = item.parentElement;
      parent.classList.toggle("completion");
    }
  }
}
