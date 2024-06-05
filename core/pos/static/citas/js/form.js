var input_fecha_cita, input_hora_cita;

$(function () {
    input_fecha_cita = $('input[name="fecha_cita"]');
    input_hora_cita = $('input[name="hora_cita"]');

    input_fecha_cita.datetimepicker({
        useCurrent: false,
        format: 'YYYY-MM-DD',
        locale: 'es',
        keepOpen: false
    });

    input_hora_cita.datetimepicker({
        useCurrent: false,
        format: 'HH:mm',
        locale: 'es',
        keepOpen: false
    });

    $('.select2').select2({
        language: 'es',
        theme: 'bootstrap4'
    });

    $('input[name="nombres"]').on('keypress', function (e) {
        return validate_text_box({'event': e, 'type': 'letters'});
    });

    $('input[name="telefono"]').on('keypress', function (e) {
        return validate_text_box({'event': e, 'type': 'numbers'});
    });

    $('input[name="correo_electronico"]').on('keypress', function (e) {
        return validate_text_box({'event': e, 'type': 'email'});
    });

    $('input[name="psicologo"]').on('keypress', function (e) {
        return validate_text_box({'event': e, 'type': 'letters'});
    });
});
