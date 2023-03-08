const socket = io()

socket.on("message", function (message) {
    $("#messages").append('<li>' + message + '</li>')
})

$("#sendButton").on("click", function () {
    let message = $("#message").val()
    socket.send(message)
    $("#message").val("")
})