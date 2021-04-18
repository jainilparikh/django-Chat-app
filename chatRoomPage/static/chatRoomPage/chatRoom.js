console.log('Reached Here')
document.getElementById('sendButton').onclick = function() { console.log('Button Pressed')};
function refresh() {
    $.ajax({
        url: "http://0.0.0.0:8000/blog/chat/"
    });
}
var seconds = 3; // seconds, edit here
setInterval(refresh(),seconds * 1000);

