window.onload = function() {
    alert("Welcome to My Website!");
};

function submitIntroduction() {
    var introduction = document.getElementById("visitorIntroduction").value;
    document.getElementById("visitorIntroductionDisplay").innerHTML = "<p><strong>Visitor's Introduction:</strong> " + introduction + "</p>";
}
function runPythonScript() {
    var pythonScriptPath = "path/to/python/script.py";
    subprocess.run(["python", pythonScriptPath]);
  }