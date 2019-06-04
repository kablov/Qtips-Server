$(document).on('submit', '#iheader form', function (e) {
  e.preventDefault();
  window.location.href = '/' + $(this).closest('form').find('input[type="text"]').val()
})
