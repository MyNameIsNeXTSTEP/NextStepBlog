window.onload = () => {
    // UI rewrites
    $('.md-copyright').remove();
    $('footer').remove();
    $('.md-nav--primary').children('label').remove();
    // NEWS tab coloring
    $( "a:contains('NEWS')")[0].style.color = "tomato";

    // SOCIALS
    // if ($(window).width() < 960) {
        // const $socialsRow = $('<div/>', { class: 'socials' });
        // $('.md-sidebar--secondary').find('.md-sidebar__inner').after($socialsRow);
        // $('.socials').load("/stylesheets/socials.html");
    // }
    // TAGS
    $('a.md-nav__link').filter(':contains("Tags")').remove()
};