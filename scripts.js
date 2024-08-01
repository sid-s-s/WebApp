document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('screeningForm');

    form.addEventListener('submit', function (event) {
        const department = document.getElementById('department').value;
        const keywords = document.getElementById('keywords').value;
        const number = document.getElementById('number').value;

        if (!department || !keywords || !number) {
            event.preventDefault();
            alert('Please fill in all fields.');
        }
    });
});
