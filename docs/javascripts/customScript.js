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

    // HOME-PAGE
    const $dropDownMenu = $('.drop-down-menu');
    const $upArrowIcon = $('.upArrowIcon');
    const $dropDownitems = $('.drop-down-items');
    $dropDownMenu.on( "click", function() {
        const isClosed = $upArrowIcon.hasClass("dd-closed");
        if (isClosed) {
            $upArrowIcon.addClass('dd-open').removeClass('dd-closed')
            $dropDownitems.addClass('ddi-open').removeClass('ddi-closed')
        }
        if (!isClosed) {
            $upArrowIcon.addClass('dd-closed').removeClass('dd-open');
            $dropDownitems.addClass('ddi-closed').removeClass('ddi-open')
        }
    });
};