const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//setTimeout(function() {
  //  $('#message').fadeOut('slow');
  //}, 3000);

  // to change the value of file input if photo submited
  function readURL(input)
  {
    if (input.files && input.files[0])
    {
      var reader = new FileReader();

      reader.onload = function(e){
        $(input).parent().css({'background': ' transparent url('+ e.target.result+') center center  no-repeat',
        'background-size':'cover',
        'color':'#20c997'
      });
      }
      reader.readAsDataURL(input.files[0]);
    }
  }
  $(document).ready(function(){
  var fileInput  = $( ".my-file-input" );
  var the_return = $(".file-return");

  fileInput.on("change", function(){
    readURL(this);
    this.nextElementSibling.innerHTML = "SELECTED<i class='fas fa-check-circle d-block'></i>";
  });
  
});