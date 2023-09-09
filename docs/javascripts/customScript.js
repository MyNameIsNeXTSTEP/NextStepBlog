window.onload = () => {
    // default footer rewrite
    $('.md-copyright').remove();
    $('footer').remove();
    // NEWS tab coloring
    $( "a:contains('NEWS')")[0].style.color = "tomato";

    // SOCIALS
    const $div = $('<div/>', { class: 'socials' });
    $('.md-content__inner').before($div);
    $('.socials').load("/temp.html");
};