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
            if (hour > 4 && hour < 12) {
                document.getElementById(loc.localisation).children[3].children[0].setAttribute("src", "../../static/timer/sunrise.png");
                document.getElementById(loc.localisation).children[3].children[0].classList.remove(['imgNight', 'imgDay']);
                document.getElementById(loc.localisation).children[3].children[0].classList.add('imgMorning');
            }
            else if(hour > 12 && hour < 20){
                document.getElementById(loc.localisation).children[3].children[0].setAttribute("src", "../../static/timer/sun.png");
                document.getElementById(loc.localisation).children[3].children[0].classList.remove(['imgMorning', 'imgNight']);
                document.getElementById(loc.localisation).children[3].children[0].classList.add('imgDay');
            }
            else{
                document.getElementById(loc.localisation).children[3].children[0].setAttribute("src", "../../static/timer/night.png");
                document.getElementById(loc.localisation).children[3].children[0].classList.remove(['imgMorning', 'imgDay']);
                document.getElementById(loc.localisation).children[3].children[0].classList.add('imgNight');
            }
        }
    })
}, 1000);
