document.addEventListener('DOMContentLoaded', function() {
    var pageNotFound = document.getElementById('not-found');
    var body = document.getElementById('body');
    
    if (pageNotFound) {
        body.classList.add('not-found');
    }
});