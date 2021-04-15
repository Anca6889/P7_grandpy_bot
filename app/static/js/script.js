alert("Grandpy se fait vieux doucement...Il ne vous reconnait plus très bien, il vous prend pour une personne s'appelant 'Billy' et il vous appelera toujours 'fiston'... Soyez indulgent envers lui ;-)");
var answer;

function getMessage(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    }) // récupère le text écrit dans la fenètre.
        .then(response => response.json())
        .then(data => answer = data)
        .catch(error => console.log(error));
}

var question = document.querySelector("#text_field"); // sélectionne le formulaire


question.addEventListener("submit", function (event) {
    event.preventDefault();
    
    getMessage("/ajax", new FormData(question))
        .then(response => {
            console.log(response);
        })
})


///////////////////////////////////////////////////////////////

// partie écrit en Jquery le chat (ajoute le texte écrit)
$(function () {

    var $list, $text_field;
    $list = $('ul'); // sélectionne la liste à puce
    $text_field = $('#text_field'); // sélectionne le formulaire

    $text_field.on('submit', function (e) { //e = évenement
        e.preventDefault();
        var text = $('input:text').val();
        $list.append('<li class="li_left">' + text + '</li > ');
        $list.append('<li class="li_right">' + answer + '</li > ');
        $('input:text').val('');
    });
});

