$(document).ready(function() {
    $('#nav li').click(function(e) {
        $('#nav li').removeClass("acive-li-nav");
        $(this).addClass("acive-li-nav");
    });
});
$(document).ready(function() {
    $('.login-form input').addClass('form-control')
    $('.login-form button').addClass('text-center')
    $('.producto_edit input').addClass('form-control-file')
    $('.producto_nuevo input').addClass('form-control-file')
 
    
})