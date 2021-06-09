setInterval(() => {
    fetch("test1", {
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
            document.getElementById(loc.localisation).children[1].innerHTML = "Date : " + loc.date
            document.getElementById(loc.localisation).children[2].innerHTML = "Heure : " + loc.heure
        }
    })
}, 1000);
