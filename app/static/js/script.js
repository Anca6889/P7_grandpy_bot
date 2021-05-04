alert("Grandpy se fait vieux doucement...Il ne vous reconnait plus très bien, il vous prend pour une personne s'appelant 'Billy' et il vous appelera toujours 'fiston'... Soyez indulgent envers lui ;-) ... ah oui Grandpy a aussi un petit soucis avec la boisson mais ne vous en faite pas pour lui, il s'assume ! ;-)...");

function getMessage(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    }) // récupère le text écrit dans la fenêtre.
        .then(response => response.json())
        .catch(error => console.log(error));
}



var map = null;

function initMap(lat, lng, i) {
    map = new google.maps.Map(document.getElementById("map" + i), {
        center: new google.maps.LatLng(lat, lng),
        zoom: 12,
    });
    marker = new google.maps.Marker({
        position: map.getCenter(),
        map: map
    });
}


//////////////////////////////////////////////////////////////

$(function () {
    var i = 0
    var $list, $text_field;
    $list = $('ul'); // sélectionne la liste à puce
    $text_field = $('#text_field'); // sélectionne le formulaire
    $text_field.on('submit', function (e) { //e = évenement
        e.preventDefault();
        getMessage("/ajax", new FormData(text_field))
            .then(response => {
                $("#loader").remove();
                if (response.lat === "") {
                    $list.append('<li class="li_left">' + response.answer + '<br> <img src="/static/images/logotg.png" id="GrandPy"> <br> </li >');
                } else {
                    $list.append('<li class="li_left"><div class="map" id="map' + i + '"></div>' + response.answer + '<br> <img src="/static/images/logotg.png" id="GrandPy"> <br> Regarde donc la carte ci-dessus Billy ! Ca se trouve juste là ! </li >');
                    initMap(parseFloat(response.lat), parseFloat(response.lng), i);
                }
            })
        var text = $('input:text').val();
        $list.append('<li class="li_right">' + text + '</li > ');
        $list.append('<div id = "loader"><li class="li_left"><img src="/static/images/loader.jpg" id="Loader"> <br> <img src="/static/images/logotg.png" id="GrandPy"> <br> </li ></div>')

        $('input:text').val('');
        i++
    });
});

