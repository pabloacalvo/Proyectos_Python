let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: 'centered', targets: [0, 1, 2] },
        { orderable: false, targets: [1, 2]},
    ],
    paging:false,
    info:false,
    lengthChange: false, // Deshabilitar el cambio del número de filas" +
    searching: false,
    autoWidth: false, // Deshabilitar ajuste automático del ancho
    responsive: true, // Habilitar tabla responsiva
    pageLength: 10,
    destroy: true,
    language: {
        "decimal": "",
        "emptyTable": "No hay información",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
        "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
        "infoFiltered": "(Filtrado de _MAX_ total entradas)",
        "infoPostFix": "",
        "thousands": ",",
        "lengthMenu": "Mostrar _MENU_ Entradas",
        "loadingRecords": "Cargando...",
        "processing": "Procesando...",
        "search": "Buscar:",
        "zeroRecords": "Sin resultados encontrados",
        "paginate": {
            "first": "Primero",
            "last": "Ultimo",
            "next": "Siguiente",
            "previous": "Anterior"
        }
    }
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    await listOrderItems();
    dataTable = $('#datatable-orderItems').DataTable(dataTableOptions);
    dataTableIsInitialized = true;

    await listOrderDeliveried();
    dataTable = $('#datatable-orderDeliveries').DataTable(dataTableOptions);
    dataTableIsInitialized = true;

    await listArticlesChanges();
    dataTable = $('#datatable-articleStock').DataTable(dataTableOptions);
    dataTableIsInitialized = true;

    await listPartsSlowStock();
        dataTable = $('#datatable-stockParts').DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const listOrderDeliveried = async ()=>{
    try {
        const response = await fetch('http://127.0.0.1:8000/order/next-deliveries/');
        const data = await response.json();

        const container = document.getElementById('datatable-orderDeliveries');
        let content = ``;
        data.forEach((order,index) => {
            content += `
            <tr>
                <td class="centered">${order.id}</td>
                <td class="centered">${order.client.name}</td>
                <td class="centered">${order.status.name_status}</td>
                <td class="centered">${order.delivery_date}</td>
            </tr>
            `
        })
        const body = document.getElementById('tableBody-orderDeliveries');
        body.innerHTML = content;
    } catch (error){
        console.log(error);
    }
}

const listOrderItems = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/order/get-shortfalls/');
        const data = await response.json();

        const container = document.getElementById('datatable-orderItem');

        let content = ``;
        data.forEach((order_item, index) => {

            content += `
            <tr>
                <td class="centered">${order_item.order}</td>
                <td class="centered">${order_item.article.article_code}</td>
                <td class="centered">${order_item.article.stock}</td>
                <td class="text-center">${order_item.quantity}</td>
            </tr>
            `;
        });

        const body = document.getElementById('tableBody-orderItems');
        body.innerHTML = content;
    } catch (error) {
        alert(error);
    }
};

const listArticlesChanges = async ()=>{
    try {
        const response = await fetch('http://127.0.0.1:8000/article/latest-changes/');
        const data = await response.json();

        const container = document.getElementById('datatable-articleStock');
        let content = ``;
        data.forEach((article,index) => {
            content += `
            <tr>
                <td class="centered">${article.article_code}</td>
                <td class="centered">${article.article_name}</td>
                <td class="centered">${article.stock}</td>
                <td class="centered">${article.price}</td>
            </tr>
            `
        })
        const body = document.getElementById('tableBody-articleStock');
        body.innerHTML = content;
    } catch (error){
        console.log(error);
    }
}

const listPartsSlowStock = async ()=>{
    try {
        const response = await fetch('http://127.0.0.1:8000/parts/get-slow-stock');
        const data = await response.json();

        const container = document.getElementById('datatable-stockParts');
        let content = ``;
        data.forEach((part,index) => {
            content += `
            <tr>
                <td class="centered">${part.name}</td>
                <td class="centered">${part.stock}</td>
                <td class="centered">${part.cost}</td>
            </tr>
            `
        })
        const body = document.getElementById('tableBody-stockParts');
        body.innerHTML = content;
    } catch (error){
        console.log(error);
    }
}

window.addEventListener('load', async () => {
    await initDataTable();
});


