let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: 'centered', targets: [0, 1, 2, 3, 4, 5] },
        { orderable: false, targets: [1, 2, 5] },
        { searchable: false, targets: [4, 5] },
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
    await listArticles();
    dataTable = $('#datatable-articles').DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const listArticles = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/articles/');
        const data = await response.json();

        // Obtener las URLs del contenedor de datos
        const container = document.getElementById('datatable-articles');
        const urlArticleTemplate = container.getAttribute('data-url-article').replace('0', '{id}');
        const urlEditArticleTemplate = container.getAttribute('data-url-edit-article').replace('0', '{id}');

        let content = ``;
        data.forEach((article, index) => {
            const urlArticle = urlArticleTemplate.replace('{id}', article.id);
            const urlEditArticle = urlEditArticleTemplate.replace('{id}', article.id);

            content += `
            <tr>
                <td class="centered">${article.article_code}</td>
                <td class="centered">${article.article_name}</td>
                <td class="centered">${article.category.name}</td>
                <td class="centered">$ ${article.cost}</td>
                <td class="centered">% ${article.margin}</td>
                <td class="centered">$ ${article.price}</td>
                <td class="centered">${article.stock} u</td>
                <td class="centered">${article.updated_at}</td>
                <td class="text-center">
                    <div>
                        <a onclick="modal_open('${urlArticle}')" class="btn btn-success btn-sm me-3"><i class="bi bi-eye"></i></a>
                        <a href="${urlEditArticle}" class="btn btn-warning btn-sm me-3"><i class="bi bi-pencil"></i></a>
                    </div>
                </td>
            </tr>
            `;
        });

        const body = document.getElementById('tableBody-articles');
        body.innerHTML = content;
    } catch (error) {
        alert(error);
    }
};

window.addEventListener('load', async () => {
    await initDataTable();
});

// Función para abrir el modal
function modal_open(url) {
    $('#modalDetail').load(url, function () {
        $(this).modal('show');
    });
}
