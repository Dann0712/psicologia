var cita = {
    list: function () {
        $('#data').DataTable({
            autoWidth: true,
            destroy: true,
            deferRender: true,
            responsive: true, // Agregado para DataTables Responsive
            rowReorder: { // Agregado para RowReorder
                selector: 'td:nth-child(2)'
            },
            ajax: {
                url: pathname,
                type: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    'action': 'search'
                },
                dataSrc: ""
            },
            columns: [
                {data: "id"},
                {data: "nombres"},
                {data: "telefono"},
                {data: "correo_electronico"},
                {data: "fecha_cita"},
                {data: "hora_cita"},
                {data: "psicologo"},
                {data: "proposito"},
                {data: "id"},
            ],

            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    render: function (data, type, row) {
                        var buttons = '<a href="' + pathname + 'update/' + row.id + '/" data-bs-toggle="tooltip" title="Editar" class="btn btn-warning btn-sm"><i class="fas fa-edit"></i></a> ';
                        buttons += '<a href="' + pathname + 'delete/' + row.id + '/" data-bs-toggle="tooltip" title="Eliminar" class="btn btn-danger btn-sm"><i class="fas fa-trash"></i></a>';
                        return buttons;
                    }
                },
            ],
            rowCallback: function (row, data, index) {
            },
            initComplete: function (settings, json) {
                enable_tooltip();
            }
        });
    }
};

$(function () {
    cita.list();
});