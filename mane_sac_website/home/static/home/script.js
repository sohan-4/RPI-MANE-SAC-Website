
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.nav-bar div').forEach(function(div) {
        div.addEventListener('click', function() {
            const link = div.querySelector('a');
            if (link && link.href) {
                window.location.href = link.href;
            }
        })
    })

    document.querySelectorAll(".submit-button").forEach(function(button) {
        button.addEventListener('click', function() {
            if(document.querySelector(".post-content").value == "") {
                alert("Please enter content for your post.");
                return;
            }else{
                alert("Post submitted successfully!");
                document.getElementById("postForm").submit();
            }
        });
    });    
    
})