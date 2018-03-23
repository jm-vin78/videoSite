function onFirstModalSubmit() {
    var inputAvailable = $('input[name=available]:checked');
    var inputRelevant = $('input[name=relevant]:checked');
    var inputLevel = $('input[name=level]:checked');

    var available = inputAvailable.val();
    var relevant = inputRelevant.val();
    var level = inputLevel.val();

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

    inputAvailable.prop("checked", false);
    inputRelevant.prop("checked", false);
    inputLevel.prop("checked", false);
}

function onSecondModalSubmit() {
    var inputMistakes = $('input[name=mistakes]:checked');
    var inputPresentation = $('input[name=presentation]:checked');
    var inputInformative = $('input[name=informative]:checked');
    var inputQuality = $('input[name=quality]:checked');

    var mistakes = inputMistakes.val();
    var presentation = inputPresentation.val();
    var informative = inputInformative.val();
    var quality = inputQuality.val();


    //TODO Read values and post them to server.
    showSuccessMessage();
    $('#secondSurveyModal').modal('hide');

    inputMistakes.prop("checked", false);
    inputPresentation.prop("checked", false);
    inputInformative.prop("checked", false);
    inputQuality.prop("checked", false);
}

function showValidationErrorMessage() {
    swal("Ошибка", "Не все поля были заполнены.", "warning");
}

function showSuccessMessage() {
    swal("Готово", "Данные были отправлены на сервер.", "success");
}

function clearFirstModal() {

}

