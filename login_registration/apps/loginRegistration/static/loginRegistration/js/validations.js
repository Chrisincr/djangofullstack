

add_validations = function(){
    //EMAIL TAKEN VALIDATIONS
    $("#id_email").change(function () {
        var email = $(this).val();
        

        $.ajax({
        url: '/ajax/validate_email/',
        data: {
            'email': email
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                $('#email_check').html('email taken')
                $("#regbutton").prop('disabled' , true)
            }
            else{
                $('#email_check').html('')
                form_validation(true)
            }
                
        }
        });

    });

    $(".pword").change(function() {
        
        pword = $("#password").val()
        pword2 = $("#confpassword").val()
        
        is_valid = pword == pword2
        
        if(!is_valid){
            $("#password_check").html('password mismatch')
            $("#regbutton").prop('disabled' , true)
        }
        else{
            $("#password_check").html('')
            form_validation()
        }
        
    })

    $("#first_name").change(function(){
        if($(this).val().length >= 2){
            $("#fname_check").html('')
            form_validation()
        }
        else{
            $("#fname_check").html('first name must be atleast 2 characters')
            $("#regbutton").prop('disabled' , true)
        }
    })

    $("#last_name").change(function(){
        if($(this).val().length >= 2){
            $("#lname_check").html('')
            form_validation()
        }
        else{
            $("#lname_check").html('first name must be atleast 2 characters')
            $("#regbutton").prop('disabled' , true)
        }
    })


}

form_validation = function(fromemail = false){
    form = $("#reg_form")
    fname =$("#first_name")
    lname =$("#last_name")
    email =$("#id_email")
    password =$("#password")

    
    if( fname.val().length >=2 && lname.val().length >=2 &&password.val().length >= 8){
        var re = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/;
        if(re.test(email.val().toUpperCase())){
            if(fromemail){
                $("#regbutton").prop('disabled' , false)
            }
            else{
                $("#id_email").change()
            }
        }


    }
    else{
        $("#form_check").html('Form errors exist or is incomplete')
        $("#regbutton").prop('disabled' , true)
    }

    
}