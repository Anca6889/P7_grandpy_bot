alert("Grandpy se fait vieux doucement...Il ne vous reconnait plus très bien, il vous prend pour une personne s'appelant 'Billy' et il vous appelera toujours 'fiston'... Soyez indulgent envers lui ;-)");

function getMessage(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    }) // récupère le text écrit dans la fenètre.
        .then(response => response.json())
        .catch(error => console.log(error));
}


//////////////////////////////////////////////////////////////

$(function () {

    var $list, $text_field;
    $list = $('ul'); // sélectionne la liste à puce
    $text_field = $('#text_field'); // sélectionne le formulaire

    $text_field.on('submit', function (e) { //e = évenement
        e.preventDefault();
        getMessage("/ajax", new FormData(text_field))
            .then(response => {
                $list.append('<li class="li_left">' + response + '<br> <img src="/static/images/logotg.png" id="GrandPy"> <br> </li > ');
            })
        var text = $('input:text').val();
        $list.append('<li class="li_right">' + text + '</li > ');
        ;
        $('input:text').val('');
    });
});

