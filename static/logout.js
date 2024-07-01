function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let profile = document.getElementById("uProfile");

function toggleMenu(){
    profile.classList.toggle("open-menu")
}

document.getElementById('logout').addEventListener('click',(event)=>{
    fetch("/logout/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken,
        }
    })
    .then(response => response.json())
    .then(data => {
        const message = data.res;
        if (message === "success"){
            location.reload()
        }
    });
})