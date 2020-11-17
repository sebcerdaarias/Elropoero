var last;

$(document).ready(function() {
    $('#nav li').click(function(e) {
        $('#nav li').removeClass("acive-li-nav");
        $(this).addClass("acive-li-nav");
        last = $(this).attr('id')
        $(last).addClass("acive-li-nav");
    });
});