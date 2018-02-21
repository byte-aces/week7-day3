$(document).ready(function() {
    console.log("The document is ready.");
    $("teucer").on("submit", function(event) {
        event.preventDefault();
        data = $("teucer").serialize();
        $.ajax({
            method: "POST",
            url: "/login",
            data: data,
            success: function(response) {
                console.log(response);
            }
        });
    });
});