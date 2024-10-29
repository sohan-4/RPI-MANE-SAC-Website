
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.nav-bar div').forEach(function(div) {
        div.addEventListener('click', function() {
            const link = div.querySelector('a');
            if (link && link.href) {
                console.log(23);
                window.location.href = link.href;
            }
        })
    })
})