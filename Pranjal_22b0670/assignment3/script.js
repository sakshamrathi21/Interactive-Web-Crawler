document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
  
    // Log the form data to the console
    console.log('Submitted Form Data:');
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Message:', message);

    const submittedDetails = document.getElementById('submitted-details');
  submittedDetails.innerHTML = `
    <h2>Thank you for submitting!</h2>
    <p>Name: ${name}</p>
    <p>Email: ${email}</p>
    <p>Message: ${message}</p>`;

});