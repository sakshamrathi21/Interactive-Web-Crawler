  function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    }
  }
  
  function submit(nme,email) {
    nme = document.getElementById('nme').value;
    email = document.getElementById('email').value;
  }
 nme = nme;
 email = email;

 function undercursor(element) {
  element.classList.add('undercursor');
}

function cursorleft(element) {
  element.classList.remove('undercursor')
}
function runPythonScript() {
  var pythonScriptPath = "/home/gd/Desktop/wids/Recusive-web-crawler-master/main.py";
subprocess.run(["python", pythonScriptPath]);
}
