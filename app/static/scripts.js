$(document).ready(function () {
    // var caixasTexto = $('.linha2');
    // caixasTexto.css('height', '20px');
    // $(this).css('height', '100px');
   
    var altura = window. screen. height;
    var largura = window. screen. width;


    


    if (largura > 1200 ) {
        $('.card-text').css('font-size', '1.1rem')
        $('.cardimg').css('width', '300px').css('height', '400px') 
        $('.card-title').css('font-size', '2rem')
    } else if (largura > 800 && largura <=1200 ) {
        $('.card-text').css('font-size', '1.6rem')
        $('.card-title').css('font-size', '2rem')
    } else if(largura>300 && largura<=800) { 
        $('.card-text').css('font-size', '2rem')
        $('.card-title').css('font-size', '2.5rem')
        
    }else{
        console.log('tá funcionando')

    }












});


