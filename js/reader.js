function readFile(){
    jQuery.get('../filefacebook',function(txt){
        $('#facey').text(txt); 
        
    });
    jQuery.get('../fileinsta',function(txt){
        $('#insta').text(txt); 
       
    });
    jQuery.get('../file',function(txt){
        $('#twit').text(txt); 
        setTimeout('readFile()',2000);
    });
}