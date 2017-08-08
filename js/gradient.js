
function update_gradient(event){
  var theta = Math.atan(event.clientY/event.clientX)*180/Math.PI;
  //var degrees = event.clientX - event.clientY + 'deg';
  var degrees = theta + 'deg'
  document.querySelector('body').style.background = "linear-gradient("+degrees+", cyan, blue)";

}			
