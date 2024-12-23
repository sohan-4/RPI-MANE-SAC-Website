
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.nav-bar div').forEach(function(div) {
        div.addEventListener('click', function() {
            const link = div.querySelector('a');
            if (link && link.href) {
                window.location.href = link.href;
            }
        })
    })

    document.querySelector(".submit-button").addEventListener("click", function () {
        const title = document.querySelector(".post-title").value.trim();
        const content = document.querySelector(".post-content").value.trim();
        const email = document.querySelector(".post-email").value.trim();
    
        if (title === "" || content === "" || email === "") {
            alert("Please fill in all required fields: Title, Content, and Email.");
            return;
        }

        const emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;

        if (!emailRegex.test(email)) {
            alert("Please enter a valid email address.");
            return;
        }
    
        const name = document.querySelector(".post-name").value.trim();
        const major = document.querySelector(".post-major").value.trim();
        const year = document.querySelector(".post-year").value.trim();
        const img = document.querySelector(".post-img").files[0];
    
        alert("Question Successfully Submitted!");
        document.getElementById("postForm").submit();
    });  
    
})