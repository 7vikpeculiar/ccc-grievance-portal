var create = function()
{ 
	var name1=document.getElementById("name").value;
	var user1=document.getElementById("user").value;
	var pass1=document.getElementById("pass").value;
	var conf1=document.getElementById("confirm").value;
	else
	{
		$.ajax({
			url:"/register",
			method:'GET',
			data:{
				name:name1,
				user:user1,
				pass:pass1,
				conf:conf1,
			},
			success: function(response){
				console.log(response);
			},
			error:   function(response){
				console.log(response);
			},
		});
	}
}
