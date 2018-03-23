function onFirstModalSubmit() {
    var available = $('input[name=available]:checked').val();
    var relevant = $('input[name=relevant]:checked').val();
    var level = $('input[name=level]:checked').val();

    if (available == 0) {
        //If video not available - do not check other fields.
        //TODO send to server video not available
        showSuccessMessage();
    } else {
        if (available === undefined || relevant === undefined || level === undefined) {
            //Check that all fields are filled by user.
            showValidationErrorMessage();
            return
        }

        if (relevant == 0 || level == "university") {
            //TODO post data to server
            showSuccessMessage();
        } else {
            $('#secondSurveyModal').modal('show');
        }
    }

    $('#firstSurveyModal').modal('hide');
}

function onSecondModalSubmit() {
    var mistakes = $('input[name=mistakes]:checked').val();
    var presentation = $('input[name=presentation]:checked').val();
    var informative = $('input[name=informative]:checked').val();
    var quality = $('input[name=quality]:checked').val();

    //TODO Post values to server.
    showSuccessMessage();
    $('#secondSurveyModal').modal('hide');
}

function showValidationErrorMessage() {
    swal("Ошибка", "Не все поля были заполнены.", "warning");
}

function showSuccessMessage() {
    swal("Готово", "Данные были отправлены на сервер.", "success");
}

