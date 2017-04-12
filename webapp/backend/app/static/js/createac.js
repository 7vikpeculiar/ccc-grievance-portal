var create = function()
{ 
	var name1=document.getElementById("name").value;
	var user1=document.getElementById("user").value;
	var email1=document.getElementById("email").value;
	var pass1=document.getElementById("pass").value;
	var conf1=document.getElementById("confirm").value;
        $(document).ready(function(){
		$.ajax({
                    url:"http://127.0.0.1:5050/addUser",
			method:'POST',
			data:{
				name:name1,
				username:user1,
			        email:email1	
			},
			success: function(response){
				console.log(response);
			},
			error:   function(response){
				console.log(response);
			},
		});
	});
};
