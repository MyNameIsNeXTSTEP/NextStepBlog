window.onload = () => {
    // UI rewrites
    $('.md-copyright').remove();
    $('footer').remove();
    $('.md-nav--primary').children('label').remove();
    // NEWS tab coloring
    $( "a:contains('NEWS')")[0].style.color = "tomato";

    // SOCIALS
    const $socialsRow = $('<div/>', { class: 'socials' });
    $('.md-content__inner').before($socialsRow);
    $('.socials').load("/NextStepBlog/stylesheets/socials.html");

    // TAGS
    $('a.md-nav__link').filter(':contains("Tags")').remove()
};