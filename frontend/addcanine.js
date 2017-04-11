var addCanine = function()
{
    dogname = document.getElementById("dogname").value;
    dogloc = document.getElementById("doglocation").value;
    describe = 'A dog';
    $(document).ready(function() 
        {
            $.ajax({
            url:"http://127.0.0.1:5050/addDog",
            method: 'POST',
            data: {
                name: dogname,
                dlocation: dogloc,
                //describe: describe,
            },
            success: function (response) 
            {
              console.log(response);
            },
            error: function (response) 
            {
              console.log(response);
            },
             
            });  
        });   
    
};
