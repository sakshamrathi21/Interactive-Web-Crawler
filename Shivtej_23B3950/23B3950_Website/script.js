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
