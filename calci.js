
function square(side) {
    return 4 * side;
}

function rectangle(length, breadth) {
    return 2 * (length + breadth);
}

function triangle(a, b, c) {
    return a + b + c;
}

function circle(radius) {
    return 2 * Math.PI * radius;
}

console.log("Square:", square(5));
console.log("Rectangle:", rectangle(5, 10));
console.log("Triangle:", triangle(3, 4, 5));
console.log("Circle:", circle(7));
