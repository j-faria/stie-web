$(function() {

  /* hide all errors */	
  $('.error').hide();
  
  
  /* when the submit button is clicked lets do some validation */
  $(".submit_btn").click(function() {
		
		
    $('.error').hide();
	
	/* get the value of the name field, check its not empty, 
	  if it is, show the error for the name field, its the
	  same for all the fields */	
	var name = $("input#name").val();
	if (name == "") {
      $("span#name_error").show();
      $("input#name").focus();
      return false;
    }
    
	var email = $("input#email").val();
	if (email == "") {
      $("span#email_error").show();
      $("input#email").focus();
      return false;
    }
	
	var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
	if(!emailReg.test(email)) {
	  $("span#email_error2").show();
      $("input#email").focus();
      return false;
	}
	
	var msg = $("textarea#msg").val();
	if (msg == "") {
	  $("span#msg_error").show();
	  $("textarea#msg").focus();
	  return false;
    }
		
	/* concatenate all the field data into a string, ready to pass via ajax */
	var dataString = 'name='+ name + '&email=' + email + '&msg=' + msg;
		
	/* include the process.php via ajax  */
	  $.ajax({
      type: "POST",
      url: "process.php",
      data: dataString,
      success: function() {
        $('#contactform').html("<div id='message'></div>");
        $('#message').html("<p>Your message has been sent!<br /> Thank you - I will be in touch soon.</p>")
        .hide()
        .fadeIn(1500, function() {
          $('#message');
        });
      }
     });
    return false;
	});
});
