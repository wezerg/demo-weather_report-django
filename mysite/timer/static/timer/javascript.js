setInterval(() => {
    fetch("refreshTime", {
        method: "GET",
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            "X-Frame-Options": "sameorigin",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    }).then(function(response) {
        return response.json()
    }).then(function(response){
        for (const loc of response.message) {
            document.getElementById(loc.localisation).children[1].children[1].innerHTML = loc.date
            document.getElementById(loc.localisation).children[2].children[1].innerHTML = loc.heure
            let hour = parseInt(loc.heure.substring(0,2));
            if (hour > 6 && hour < 19) {
                document.getElementById(loc.localisation).children[3].children[0].setAttribute("src", "../../static/timer/sun.png");
                document.getElementById(loc.localisation).children[3].children[0].classList.replace('imgNight', 'imgDay');
            }
            else{
                document.getElementById(loc.localisation).children[3].children[0].setAttribute("src", "../../static/timer/night.png");
                document.getElementById(loc.localisation).children[3].children[0].classList.replace('imgDay', 'imgNight');
            }
        }
    })
}, 1000);
