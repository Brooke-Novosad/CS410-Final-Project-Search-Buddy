console.log("hi");
const f = document.getElementById('form');
const q = document.getElementById('query');

function postData(input) {
  $.ajax({
      type: "POST",
      url: "/ranking_function.py",
      data: { param: input },
      success: callbackFunc
  });

}
function submitted(event) {
  event.preventDefault();
  const query = q.value;
  console.log(query);
  search_animal();
}
postData('start');
f.addEventListener('submit', submitted);

function search_animal() { 
  let input = document.getElementById('query').value 
  input=input.toLowerCase(); 
  let x = document.getElementsByClassName('animals'); 
    
  for (i = 0; i < x.length; i++) {  
      if (!x[i].innerHTML.toLowerCase().includes(input)) { 
          x[i].style.display="none"; 
      } 
      else { 
          x[i].style.display="list-item";                  
      } 
  } 
} 
