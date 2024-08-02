let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: 'centered', targets: [0, 1, 2, 3, 4, 5, 6, 7] },
        { orderable: false, targets: [7] },
        { searchable: false, targets: [1,3,4,6,7] },
    ],
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
    await listOrders();
    dataTable = $('#datatable-orders').DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const listOrders = async () => {
    try {
        const response = await fetch('/order/order_list/');
        const data = await response.json();
        const container = document.getElementById('datatable-orders');
        const urlDeleteTemplate = container.getAttribute('data-url-delete-order').replace('0', '{id}');
        const urlEditOrderTemplate = container.getAttribute('data-url-edit-order').replace('0', '{id}');
        const urlDeliverOrderTemplate = container.getAttribute('data-url-deliver-order').replace('0', '{id}')

        let content = ``;
        data.forEach((order) => {
            const urlEditOrder = urlEditOrderTemplate.replace('{id}', order.id);
            const urlDeliverOrder =urlDeliverOrderTemplate.replace('{id}', order.id);
            content += `
            <tr>
                <td class="centered">${order.id}</td>
                <td class="centered">${order.delivery_date}</td>
                <td class="centered">${order.client.name}</td>
                <td class="centered">% ${order.discount}</td>
                <td class="centered">$ ${order.total}</td>
                <td class="centered">${order.status.name_status}</td>
                <td class="centered">${order.updated_at}</td>
                <td class="text-center">
                    <div>
                        <i class="bi bi-check-circle entregar-pedido" data-url="${urlDeliverOrder}" style="cursor: pointer;"></i>
                        <a onclick="modal_open('${urlEditOrder}')" style="cursor: pointer;"><i class="bi bi-pencil editar-pedido-icon"></i></a>
                    </div>
                </td>
            </tr>
            `;
        });

        const body = document.getElementById('tableBody-orders');
        body.innerHTML = content;
        addEventListeners();
    } catch (error) {
        alert(error);
    }
};

const addEventListeners = () => {
    // Obtener el modal y sus elementos
    const confirmationModal = new bootstrap.Modal(document.getElementById('modal-entregar-pedido'));
    const confirmButton = document.querySelector('#modal-entregar-pedido .btn-primary');

    document.querySelectorAll('.entregar-pedido').forEach(icon => {
        icon.addEventListener('click', async (event) => {
            event.preventDefault();

            // Guardar la URL en un atributo de datos en el botón de confirmación del modal
            const url = event.currentTarget.getAttribute('data-url');
            confirmButton.setAttribute('data-url', url);

            // Mostrar el modal de confirmación
            confirmationModal.show();
        });
    });

    // Manejar el clic en el botón de confirmación del modal
    confirmButton.addEventListener('click', async (event) => {
        const url = event.currentTarget.getAttribute('data-url');

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            const data = await response.json();
            if (data.status === 'success') {
                mostrarMensaje('Pedido entregado, stock descontado', 'success');
                await initDataTable();
            } else if (data.status === 'no-change') {
                // Manejar caso de no cambio
            } else if (data.status === 'error') {
                mostrarMensaje('Ocurrió un error, revisa el stock', 'error');
            }
        } catch (error) {
            console.log(error);
        } finally {
            // Cerrar el modal después de la acción
            confirmationModal.hide();
        }
    });
};




document.addEventListener('DOMContentLoaded', async () => {
    await initDataTable();
});

// Función para abrir el modal
function modal_open(url) {
    $('#modalDetail').load(url, function () {
        $(this).modal('show');
    });
}

// Función para obtener el token CSRF
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

// Función para mostrar mensajes
const mostrarMensaje = (mensaje, tipo) => {
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML = `<div class="alert alert-${tipo}">${mensaje}</div>`;
    setTimeout(() => {
        messagesDiv.innerHTML = '';
    }, 3000);
};