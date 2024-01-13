var url={
  'socios':'https://localhost:7100/socios/allSocios',
  'pagos':'https://localhost:7100/Pagos/Historico'
}

//document.getElementById("myButton").addEventListener("click", obtenerDatos());
var $sociosConseguidos=0
var $pagosConseguidos=0
function obtenerDatos(url){
  if ($sociosConseguidos!=0) return
  fetch(url)
  .then(response => response.json())
  .then(data => {
    if(url.includes('pagos')){
      createTable(data);
      $pagosConseguidos+=1
    }else if(url.includes('socios')){
      createTable(data);
      $sociosConseguidos+=1
    }
  })
  .catch(error => {
    console.log(error);
  });
}


function createTable(data) {
  // Obtiene la referencia al elemento de la tabla en el HTML
  const table = document.getElementById('myTable');

  // Crea el encabezado de la tabla con estilo Bootstrap
  const headerRow = document.createElement('tr');
  Object.keys(data[0]).forEach(key => {
    const headerCell = document.createElement('th');
    headerCell.classList.add('bg-primary', 'text-white'); // Agrega clases Bootstrap para el estilo del encabezado
    if( key ==='idSocio'){
      key='Num Socio'
    }else if(key ==='nombre'){
      key='Nombre'
    }else if(key ==='apellido'){
      key='Apellido'
    }else if(key ==='dni'){
      key='Documento'
    }else if(key ==='direccion'){
      key='Direccion'
    }else if(key ==='nombreGenero'){
      key='Genero'
    }else if(key ==='fechaDeInscripcion'){
      key='Socio desde'
    }else if(key ==='nombreEstado'){
      key='Estado'
    }else if(key ==='fechaUltimoPago'){
      key='Ultimo pago'
    }else if(key ==='nombreAbono'){
      key='Abono'
    }
    headerCell.textContent = key;
    headerRow.appendChild(headerCell);
  });
  table.appendChild(headerRow);

  // Crea las filas de datos de la tabla con estilo Bootstrap
  data.forEach(item => {
    const dataRow = document.createElement('tr');
    Object.values(item).forEach(value => {
      const dataCell = document.createElement('td');
      dataCell.textContent = value;
      dataRow.appendChild(dataCell);
    });
    table.appendChild(dataRow);
  });
}


