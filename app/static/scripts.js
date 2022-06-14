$(document).ready(function () {
    // var caixasTexto = $('.linha2');
    // caixasTexto.css('height', '20px');
    // $(this).css('height', '100px');
    
    var altura = window. screen. height;
    var largura = window. screen. width;
    
    
    
//     function mudacor(cor1, cor2, tmp)
//     { 
//         setInterval(()=>{
//             $('.header').css('background-color', cor1)
//         },tmp)  
//         setInterval(()=>{
//             $('.header').css('background-color', cor2)
//         },tmp/2)
//     }
    
//    setInterval(mudacor('yellowgreen', 'orange', 3000), 3000)


    if (largura > 1200 ) {
        $('.fonte-pequena').css('font-size', '1.3rem')
        // $('.cardimg').css('width', '300px').css('height', '400px') 
        $('.fonte-media').css('font-size', '2rem')
        $('.fonte-grande').css('font-size', '2.4rem')
    } else if (largura > 800 && largura <=1200 ) {
        $('.fonte-pequena').css('font-size', '1.9rem')
        $(' .fonte média').css('font-size', '2rem')
        $('.linha2').css('height', '80vh').css('display', 'flex')
        $('.amarra').css('height', 'fit-content').css('margin:auto')
        $('.fonte-grande').css('font-size', '2rem')
       
    } else if(largura>300 && largura<=800) { 
        $('.fonte-pequena').css('font-size', '2.3rem')
        $('.fonte-media').css('font-size', '2.5rem')
        $('.fonte-grande').css('font-size', '2.6rem')  
        $('.fonte-gigante').css('font-size ', '3.8rem')    
    }else{
        console.log('tá funcionando')
    }









    // $(window).scroll(
    //     ()=>{
    
    //         $('.header').animate({height: '100px', opacity: '1', width:'0px'},2000, ()=>{
    //             $('.imglogo').css('height', '70px').css('width', '70px').css('margin', 'auto')
    //             $('.conteudo').css('display', 'none')
    //             $('.header').css('height', '100px').css('position', 'fixed').css('z-index', '3').css('padding', '0').css('top', '0').css('width', '100px').css('position', 'fixed').css('right', '30px').css('background-color', 'orange').css('opacity', 0.7)
    //             $('.header').css('-webkit-border-bottom-right-radius', '15px').css('-webkit-border-bottom-left-radius', '15px').css('-moz-border-radius-bottomright', '15px').css('-moz-border-radius-bottomleft','15px').css('border-bottom-left-radius', '15px').css('border-bottom-right-radius', '15px')
        
    //         })
    //     }       
    // )
    











})