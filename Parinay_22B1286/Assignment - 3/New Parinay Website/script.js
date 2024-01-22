
document.addEventListener('DOMContentLoaded', function () {
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});


function submitDetails() {
    // Retrieve form data
    var name = document.getElementById('name').value;
    var phoneNumber = document.getElementById('phoneNumber').value;
    var email = document.getElementById('email').value;
    var profession = document.getElementById('profession').value;
    var address = document.getElementById('address').value;

    // You can perform further actions with the details, such as sending them to a server or displaying them
    console.log("Name: " + name);
    console.log("Phone Number: " + phoneNumber);
    console.log("Email: " + email);
    console.log("Profession: " + profession);
    console.log("Address: " + address);

    // Optional: Show a confirmation message to the user
    alert("Details submitted successfully!");
}
