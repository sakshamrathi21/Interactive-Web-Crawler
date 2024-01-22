function appendC() {
    let fname = document.querySelector('#fname');
    let lname = document.querySelector('#lname');
    var table = document.querySelector('#f');
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = fname.value + " " + lname.value;
    cell2.innerHTML = email.value;
    alert('Contact Added to List');
}

document.addEventListener("DOMContentLoaded", function () {
  // Add an event listener to the submit button
  document.getElementById("submit").addEventListener("click", function () {
    // Get the input values
    var link = document.getElementById("wl").value;
    var depth = document.getElementById("depth").value;

    // Make a POST request to your API
    fetch("http://localhost:8000/crawl", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        param1: link,
        param2: depth,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Update the DOM with the received data
        console.log("Success:", data);
        displayResults(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });

  // Function to display the results in the resultContainer
  function displayResults(data) {
    var resultContainer = document.getElementById("resultContainer");

    // Clear previous results
    resultContainer.innerHTML = "";

    // Create a list to display the URLs
    var ul = document.createElement("ul");

    // Iterate through the URLs and create list items
    data.forEach(function (url) {
      var li = document.createElement("li");
      li.textContent = url;
      ul.appendChild(li);
    });

    // Append the list to the result container
    resultContainer.appendChild(ul);
  }
});