window.onload = () => {
    $('.md-footer').remove();
    $('.md-option').on('click', function() {
        const bodyTheme = $('body').attr('data-md-color-scheme');
        const headerIcon = $('.md-header img');
        // Because the triggering starts before then changes of theme
        if (bodyTheme === 'slate') {
            headerIcon.css({
                border: 'solid',
                borderColor: 'white',
            });
        } else if (bodyTheme === 'default') {
            headerIcon.css({
                border: 'solid',
                borderColor: 'black',
            });
        }
   });
};