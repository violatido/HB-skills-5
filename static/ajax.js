// Replace this with your code

$('#id-button').on('click', () => {
    const humanData = {
        firstName = $('#fname').val(),
        lastName = $('#lname').val(),
        email = $('#email').val()
    }

    $.get('/api/human/<int:human_id>', humanData, (response) => {
        $('#human-id').html(response);
    })
});