<form id="locationForm">
<input id="addLocation" type="text" placeholder="Enter Zipcode">
<button type="submit">Submit</button>
</form>

let locationForm = document.getElementById('locationForm')
let addLocation = document.getElementById('addLocation')
let geoForm = document.getElementById('17c9eb30e0a-widget-3-input')


form.addEventListener('submit', function(event) {
    event.preventDefault
    let location = addTodo.value
    let itemLi = document.createElement('li')
    console.log(itemLi)
    itemLi.innerHTML=item
    todoList.appendChild(itemLi)
    let deleteButton = document.createElement('button')
    deleteButton.innerText = "Remove"
    itemLi.appendChild(deleteButton)
    let completeButton = document.createElement("button")
    completeButton.innerText = "Complete"
    itemLi.appendChild(completeButton)
