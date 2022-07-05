$('#tite').css('color', 'blue')


$(window).on("load", function(){
  // var bemEstar= parseFloat(document.getElementById('bem-estar').innerText);
  // var educacao= parseFloat(document.getElementById('educacao').innerText);
  // var transporte= parseFloat(document.getElementById('transporte').innerText);
  // var farmacia= parseFloat(document.getElementById('farmacia').innerText);
  // var tabaco= parseFloat(document.getElementById('tabaco').innerText);
  // var info=parseFloat( document.getElementById('info').innerText);
  // var academia= parseFloat(document.getElementById('academia').innerText);
  // var alimentacao= parseFloat(document.getElementById('alimentacao').innerText);
  // var mercado= parseFloat(document.getElementById('mercado').innerText);
  // var outros= parseFloat(document.getElementById('outros').innerText);
  
  var nome = document.getElementsByClassName('nome')
  var subtotal = document.getElementsByClassName('totalclass')
  var linha = []
  var dict = []
  dict.push(['Task', 'gastos por categoria']) 
  
  for (let i = 0; i < nome.length; i++) {
    linha = [
      nome[i].innerHTML, parseFloat(subtotal[i].innerHTML) 
    ]
    dict.push(linha)
  }


  console.log(dict)



  




  google.charts.load("current", {packages:["corechart"]});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart() {
    var data = google.visualization.arrayToDataTable(dict);
  
    var options = {
      title: 'Gastos por categoria',
      pieHole: 0.4,
    };
  
    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);
  }
  
    
  
});


