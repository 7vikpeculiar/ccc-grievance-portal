var addCanine = function()
{
    dogname = document.getElementById('dogname').value;
    dogloc = document.getElementById('doglocation').value;
    describe = 'A dog';
    $(document).ready(function() 
        {
        ({
            url: 'http://127.0.0.1:5000/addDog',
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
             
            });  
        });   
    
};
