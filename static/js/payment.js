$(document).on('click', '#cost > *:nth-child(2) > div', function () {
    $(this).closest('form').find('input[type="text"]').val($(this).find('p').attr('data-id') + ' Р.')
})

$(document).on('mouseover', '#cost > *:nth-child(2) > div', function () {
    $(this).parent().find('> *').each(function () {
        $(this).attr('class', '_gray')
    });
    $(this).attr('class', '_black')
})