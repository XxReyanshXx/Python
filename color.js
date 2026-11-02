
function changeColor() {
    var colors = ["red", "blue", "green", "yellow", "pink"];

    var random = Math.floor(Math.random() * colors.length);

    document.body.style.backgroundColor = colors[random];
}

var button = document.createElement("button");

button.innerText = "Change Colour";

button.onclick = changeColor;

document.body.appendChild(button);
