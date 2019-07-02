const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//setTimeout(function() {
  //  $('#message').fadeOut('slow');
  //}, 3000);

  // to change the value of file input if photo submited
  $(document).ready(function(){
  var fileInput  = $( ".my-file-input" );
  var the_return = $(".file-return");

  fileInput.on("change", function(){
    this.nextElementSibling.innerHTML = "SELECTED<i class='fas fa-check-circle d-block'></i>";
  });
  
});