window.onload = () => {
    // default footer rewrite
    $('.md-copyright').remove();
    $(document).ready(function() {
        $('footer').append(
            $(document.createElement('button')).prop({
                type: 'button',
                innerHTML: 'SOCIALS',
                class: 'btn-socials'
            })
        );
    });
    $("body").on("click", ".btn-socials", function() {
        window.open('https://dom.ru', '_blank');
    });
    // NEWS tab coloring
    $( "a:contains('NEWS')")[0].style.color = "tomato";
};