$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        console.log('Button clicked');
        $('#sidebar').toggleClass('active');
        console.log('Toggled active class');
    });
});