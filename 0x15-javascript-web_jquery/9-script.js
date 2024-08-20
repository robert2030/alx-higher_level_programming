// Wait for the document to be ready before executing the script
$(document).ready(function() {
    // Fetch translation and display it in DIV#hello
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        $('#hello').text(data.hello);
    });
});
