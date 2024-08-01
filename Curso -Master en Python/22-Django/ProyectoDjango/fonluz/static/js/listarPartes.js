let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: 'centered', targets: [0, 1, 2, 3, 4, 5] },
        { orderable: false, targets: [5] },
        { searchable: false, targets: [0, 2, 3, 4, 5] },
    ],
    pageLength: 10,
    destroy: true,
    language: {
        "decimal": "",
        "emptyTable": "No hay información",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
        "infoEmpty": "Mostrando 0 a 0 de 0 Entradas",
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
            "last": "Último",
            "next": "Siguiente",
            "previous": "Anterior"
        }
    }
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    await listParts();
    dataTable = $('#datatable-parts').DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const listParts = async () => {
    try {
        const response = await fetch('/parts/');
        const data = await response.json();
        const container = document.getElementById('datatable-parts');
        const urlEditPartTemplate = container.getAttribute('data-url-edit-part').replace('0', '{id}');
        let content = ``;
        data.forEach((part) => {
            const urlEditPart = urlEditPartTemplate.replace('{id}', part.id);
            content += `
            <tr>
                <td class="centered">${part.id}</td>
                <td class="centered">${part.name}</td>
                <td class="centered">${part.stock}</td>
                <td class="centered">$ ${part.cost}</td>
                <td class="centered">${part.updated_at}</td>
                <td class="text-center">
                    <div>
                        <a href="#" onclick="modal_open(event, '${urlEditPart}')" style="cursor: pointer;"><i class="bi bi-pencil editar-pedido-icon"></i></a>
                    </div>
                </td>
            </tr>
            `;
        });
        const body = document.getElementById('tableBody-parts');
        body.innerHTML = content;
    } catch (error) {
        alert(error);
    }
};

const modal_open = (event, url) => {
    event.preventDefault();
    $('#modalPartDetail').load(url, function () {
        $(this).modal('show');
    });
};

document.addEventListener('DOMContentLoaded', async () => {
    await initDataTable();
});

