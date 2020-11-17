$(document).ready(function() {
    $('#nav li').click(function(e) {
        alert($(this).addClass("acive-li-nav"));
    });
});