$('#tite').css('color', 'blue')


$(window).on("load", function(){
  var bemEstar= parseFloat(document.getElementById('bem-estar').innerText);
  var educacao= parseFloat(document.getElementById('educacao').innerText);
  var transporte= parseFloat(document.getElementById('transporte').innerText);
  var farmacia= parseFloat(document.getElementById('farmacia').innerText);
  var tabaco= parseFloat(document.getElementById('tabaco').innerText);
  var info=parseFloat( document.getElementById('info').innerText);
  var academia= parseFloat(document.getElementById('academia').innerText);
  var alimentacao= parseFloat(document.getElementById('alimentacao').innerText);
  var mercado= parseFloat(document.getElementById('mercado').innerText);
  var outros= parseFloat(document.getElementById('outros').innerText);
  


  google.charts.load("current", {packages:["corechart"]});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart() {
    var data = google.visualization.arrayToDataTable([
      ['Task', 'gastos por categoria'],
      ['Bem-Estar', bemEstar],
      ['Educação e Softwares', educacao],
      ['Transporte',  transporte],
      ['Farmácia', farmacia],
      ['Tabaco e Cia', tabaco],
      ['Informática', info],
      ['Academia', academia],
      ['Alimentação', alimentacao],
      ['Mercado', mercado],
      ['Outros', outros]
    ]);
  
    var options = {
      title: 'Gastos por categoria',
      pieHole: 0.4,
    };
  
    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);
  }
  
    
  
});


