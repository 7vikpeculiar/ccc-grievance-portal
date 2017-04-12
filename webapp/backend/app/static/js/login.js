var login = function()
{
	var user1=document.getElementById("user").value;
	var pass1=document.getElementById("pass").value;
	if(!(typeof(user1)==='string' && ^[a-z0-9](\.?[a-z0-9]){5,}@\.com$.test(user1)))
	{
		document.getElementById("user").value=null;
		document.getElementById("pass").value=null;
		alert("INVALID USERNAME");
		throw 'invalid username';
	}
	else
	{
		$.ajax({
			url:"/login",
			method:'GET',
			data:{
				user:user1,
				pass:pass1,
			},
			success: function(response){
				console.log(response);
			},
			error: function(response){
				console.log(response);
			},
		});
	}
};

var loginAdm = function()
{
	var adm1=document.getElementById("useradm").value;
	var passadm1=document.getElementById("passadm").value;
	else
	{
		$.ajax({
			url:,
			method:'GET',
			data:{
				adm:adm1,
				passadm:passadm1,
			},
			success: function(response){
				console.log(response);
			},
			error: function(response){
				console.log(response);
			},
			});
	}
};
