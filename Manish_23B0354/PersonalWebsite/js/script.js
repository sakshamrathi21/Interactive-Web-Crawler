const hobbies = document.querySelectorAll('.hobby');
for(let i=0;i<hobbies.length;++i){
    hobbies[i].addEventListener('mouseover',function(){
        this.classList.add('hovered');})
    hobbies[i].addEventListener('mouseout',function(){this.classList.remove('hovered');})
}


const button = document.querySelector('#click');
let userInput;
button.addEventListener('click',function () {
    userInput=document.querySelector('#userInput').value;
    alert(`Your review is: ${userInput}`);
})