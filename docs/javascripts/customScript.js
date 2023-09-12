window.onload = () => {
    // default footer rewrite
    $('.md-copyright').remove();
    $('footer').remove();
    // NEWS tab coloring
    $( "a:contains('NEWS')")[0].style.color = "tomato";

    // SOCIALS
    const $socialsRow = $('<div/>', { class: 'socials' });
    $('.md-content__inner').before($socialsRow);
    $('.socials').load("/stylesheets/socials.html");

    // TAGS
    $('a.md-nav__link').filter(':contains("Tags")').remove()
};