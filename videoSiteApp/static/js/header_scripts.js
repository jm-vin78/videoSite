function onFirstModalSubmit() {
    var available = $('input[name=available]:checked').val();
    var relevant = $('input[name=relevant]:checked').val();
    var level = $('input[name=level]:checked').val();
    var video_id = $('#current-video-id').val();

    if (available == 0) {
        //If video not available - do not check other fields.
        $.ajax({
            type: 'POST',
            url: 'set_video_not_available',
            data: {
                "video_id": video_id
            },
            success: function () {
                showSuccessMessage();
                $('#firstSurveyModal').modal('hide');
            },
            error: function () {
                showErrorMessage()
            }
        });
    } else {
        if (available === undefined || relevant === undefined || level === undefined) {
            //Check that all fields are filled by user.
            showValidationErrorMessage();
            return
        }

        if (relevant == 0 || level == "university") {
            $.ajax({
                type: 'POST',
                url: 'set_video_not_appropriate',
                data: {
                    "video_id": video_id,
                    "relevant": relevant,
                    "level": level
                },
                success: function () {
                    showSuccessMessage();
                    $('#firstSurveyModal').modal('hide');
                },
                error: function () {
                    showErrorMessage()
                }
            });
        } else {
            $('#firstSurveyModal').modal('hide');
            $('#secondSurveyModal').modal('show');
        }
    }
}

function onSecondModalSubmit() {
    var mistakes = $('input[name=mistakes]:checked').val();
    var presentation = $('input[name=presentation]:checked').val();
    var informative = $('input[name=informative]:checked').val();
    var quality = $('input[name=quality]:checked').val();
    var video_id = $('#current-video-id').val();

    if (mistakes === undefined || presentation === undefined || informative === undefined || quality === undefined) {
        showValidationErrorMessage();
        return;
    }

    $.ajax({
        type: 'POST',
        url: 'set_video_survey_result',
        data: {
            "mistakes": mistakes,
            "presentation": presentation,
            "informative": informative,
            "quality": quality,
            "video_id": video_id
        },
        success: function () {
            showSuccessMessage();
            $('#secondSurveyModal').modal('hide');
        },
        error: function () {
            showErrorMessage()
        }
    });
}

function showValidationErrorMessage() {
    swal("Ошибка", "Не все поля были заполнены.", "warning");
}

function showSuccessMessage() {
    swal("Готово", "Данные были отправлены на сервер.", "success");
}

function showErrorMessage() {
    swal("Ошибка", "Не удалось отправить данные на сервер. Пожалуйста, повторите попытку позже.", "error");
}

