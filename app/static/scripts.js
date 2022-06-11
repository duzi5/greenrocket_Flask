$(document).ready(function () {
    // var caixasTexto = $('.linha2');
    // caixasTexto.css('height', '20px');
    // $(this).css('height', '100px');
   
    var altura = window. screen. height;
    var largura = window. screen. width;


    


    if (largura > 1200 ) {
        $('.fonte-pequena').css('font-size', '1.1rem')
        $('.cardimg').css('width', '300px').css('height', '400px') 
        $('.fonte-media').css('font-size', '2rem')
        $('.fonte-grande').css('font-size', '2.4rem')
    } else if (largura > 800 && largura <=1200 ) {
        $('.fonte-pequena').css('font-size', '1.6rem')
        $(' .fonte média').css('font-size', '2rem')
        $('.linha2').css('height', '80vh').css('display', 'flex')
        $('.amarra').css('height', 'fit-content').css('margin:auto')
        $('.fonte-grande').css('font-size', '2rem')
       
    } else if(largura>300 && largura<=800) { 
        $('.fonte-pequena').css('font-size', '2rem')
        $('.fonte-media').css('font-size', '2.5rem')
        $('.fonte-grande').css('font-size', '2.6rem')  
        $('.fonte-gigante').css('font-size ', '3.8rem')    
    }else{
        console.log('tá funcionando')

    }












});


