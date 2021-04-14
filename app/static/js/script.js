alert("Grandpy se fait vieux doucement...Il ne vous reconnait plus très bien, il vous prend pour une personne s'appelant 'Billy' et il vous appelera toujours 'fiston'... Soyez indulgent envers lui ;-)");

let question = document.querySelector("#text_field") // sélectionne le formulaire

question.addEventListener("submit", function (event) {
    event.preventDefault();
    console.log("texte envoyé");

    fetch("/ajax", {
        method: "POST",
        body: new FormData(question)
    }); // récupère le text écrit dans la fenètre.
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
        $list.append('<li>' + text + '</li>');
        $('input:text').val('');
    });
});