var complain=function()
{
	var complaint1=document.getElementById("complaint");
	var dog=[],j=0;
	for(var i=0;i<complaint1.options.length;i++)
	{
		if(complaint1.options[i].selected==true)
		{
			dog[j]=complaint1.options[i].value;
			j++;
		}	
	}
	var comment1= document.getElementById("comment").value;
	var imagefile1=document.getElementById("imagefile").value;
        
        
}
