let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: 'centered', targets: [0, 1, 2, 3, 4] },
        { orderable: false, targets: [4] },
        { searchable: false, targets: [4] },
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

const initDataTable = () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    dataTable = $('#datatable-articlesPedidos').DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const listarArticulos = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/articles/');
        const data = await response.json();
        let content = ``;
        data.forEach((article) => {
            content += `
            <tr>
                <td class="centered">${article.article_code}</td>
                <td class="centered">${article.article_name}</td>
                <td class="centered">$ ${article.price}</td>
                <td class="centered">${article.stock}</td>
                <td class="text-center">
                    <div>
                        <button type="button" class="btn btn-primary mb-3 add-to-cart" data-id="${article.id}" data-quantity="1"><i class="bi bi-cart-plus"></i>Agregar</button>
                    </div>
                    <div class="col-md-5 mx-auto text-center">
                        <input type="number" class="form-control quantity-input" name="quantity" placeholder="Cant" value="1" min="1">
                    </div>
                </td>
            </tr>
            `;
        });

        document.getElementById('tableBodyarticles').innerHTML = content;

        // Inicializar DataTable después de cargar el contenido
        initDataTable();

        // Añadir eventos click a los botones de agregar al carrito
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', async (event) => {
                const articleId = event.currentTarget.getAttribute('data-id');
                const quantityInput = event.currentTarget.closest('td').querySelector('.quantity-input');
                const quantity = quantityInput.value;

                try {
                    const response = await fetch('/cart/add/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken') // Asegúrate de incluir el CSRF token
                        },
                        body: JSON.stringify({
                            article_id: articleId,
                            quantity: quantity,
                            override_quantity: false
                        })
                    });
                    const data = await response.json();
                    if (data.status === 'success') {
                        mostrarMensaje('Artículo agregado al carrito.', 'success');
                        await actualizarCarrito();
                    } else {
                        mostrarMensaje('Error al agregar el artículo al carrito: ' + data.message, 'error');
                    }
                } catch (error) {
                    console.log(error);
                    mostrarMensaje('Error al agregar el artículo al carrito.', 'error');
                }
            });
        });
    } catch (error) {
        console.log(error);
    }
};

const actualizarCarrito = async () => {
    try {
        const response = await fetch('/cart/details/');
        const data = await response.json();
        let content = ``;
        data.items.forEach((item) => {
            content += `
            <tr>
                <td>${item.id}</td>
                <td>${item.article_name}</td>
                <td>${item.quantity}</td>
                <td>$${item.price}</td>
                <td>$${item.total_price.toFixed(2)}</td>
                <td class="text-center">
                    <button type="button" class="btn btn-danger btn-sm remove-from-cart" data-id="${item.id}"><i class="bi bi-trash3"></i></button>
                </td>
            </tr>
            `;
        });
        content += `
        <tr class="total">
            <td>Total</td>
            <td></td>
            <td>${data.total_items}</td>
            <td></td>
            <td>$${data.total_price.toFixed(2)}</td>
        </tr>
        `;
        document.getElementById('cart-items').innerHTML = content;

        // Añadir eventos click a los botones de eliminar del carrito
        document.querySelectorAll('.remove-from-cart').forEach(button => {
            button.addEventListener('click', async (event) => {
                const articleId = event.currentTarget.getAttribute('data-id');
                console.log('ID del artículo:', articleId); // Verifica el valor aquí

                if (!articleId) {
                    console.error('El ID del artículo es nulo.');
                    return;
                }

                try {
                    const response = await fetch(`http://127.0.0.1:8000/cart/remove/${articleId}/`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken') // Asegúrate de incluir el CSRF token
                        }
                    });
                    const data = await response.json();
                    if (data.status === 'success') {
                        mostrarMensaje('Artículo eliminado del carrito.', 'success');
                        await actualizarCarrito();
                    } else {
                        mostrarMensaje('Error al eliminar el artículo del carrito: ' + data.message, 'error');
                    }
                } catch (error) {
                    console.log(error);
                    mostrarMensaje('Error al eliminar el artículo del carrito.', 'error');
                }
            });
        });
    } catch (error) {
        console.log(error);
    }
};

// Función para mostrar mensajes
const mostrarMensaje = (mensaje, tipo) => {
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML = `<div class="alert alert-${tipo}">${mensaje}</div>`;
    setTimeout(() => {
        messagesDiv.innerHTML = '';
    }, 3000);
};

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

const cargaInicial = async () => {
    await listarArticulos();
    await actualizarCarrito();
};

window.addEventListener("load", async () => {
    await cargaInicial();
});
