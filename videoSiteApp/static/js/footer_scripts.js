/**
 * Created by yulia on 21-Mar-18.
 */

$('select#select_subject').change(function () {
    var id = $(this).find(':selected')[0].id;
    $.ajax({
        type: 'GET',
        url: 'get_topic',
        data: {"idsubject": id},
        success: function (data) {
            var json = $.parseJSON(data);
            var $select_topic = $('select#select_topic');
            var $select_subtopic = $('select#select_subtopic');

            $select_topic.empty();
            $select_subtopic.empty();

            for (var i = 0; i < json.length; i++) {
                $select_topic.append('<option id=' + json[i].pk + ' value=' + json[i].fields.name + '>' + json[i].fields.name + '</option>');
            }

            $select_subtopic.append('<option value="">---</option>');

            $select_topic.change();
        }
    });
});

$('select#select_topic').change(function () {
    var id = $(this).find(':selected')[0].id;
    $.ajax({
        type: 'GET',
        url: 'get_subtopic',
        data: {"idtopic": id},
        success: function (data) {
            var json = $.parseJSON(data);
            var $select_subtopic = $('select#select_subtopic');

            $select_subtopic.empty();

            for (var i = 0; i < json.length; i++) {
                $select_subtopic.append('<option id=' + json[i].pk + ' value=' + json[i].fields.name + '>' + json[i].fields.name + '</option>');
            }

            $select_subtopic.change();
        }
    });
});

$('select#select_subtopic').change(function () {
    var id = $(this).find(':selected')[0].id;
    $.ajax({
        type: 'GET',
        url: 'get_video_url',
        data: {"idsubtopic": id},
        success: function (data) {
            var json = $.parseJSON(data);
            var $column = $('div#videos_column');

            $column.empty();

            for (var i = 0; i < json.length; i++) {
                var url = json[i].url;
                url = url.replace(/https:\/\/www.youtube.com\/watch.v=(.+)/, "https://www.youtube.com/embed/$1");
                $column.append('');
                $column.append('<div class="card">' +
                    '<iframe width="520" height="415" src="' + url + '" id="' + json[i].idvideo + '">' +
                    '</iframe>' +
                    '<button title="Оценить видео" data-toggle="modal" data-target="#firstSurveyModal" onclick="$(\'#current-video-id\').val(\'' + json[i].idvideo + '\')" style="cursor: pointer">' +
                    'Оценить видео' +
                    '</button>' +
                    '</div>');
            }
        }
    });
});

$(document).ready(function () {
    var $select_subject = $('select#select_subject');
    $select_subject.change()

    $('#firstSurveyModal').on('hidden.bs.modal', function () {
        $('#firstModalForm').trigger('reset');
    });

    $('#secondSurveyModal').on('hidden.bs.modal', function () {
        $('#secondModalForm').trigger('reset');
    });

    // Cache selectors for faster performance.
    var $window = $(window),
        $mainMenuBar = $('#mainMenuBar'),
        $mainMenuBarAnchor = $('#mainMenuBarAnchor');

    // Run this on scroll events.
    $window.scroll(function () {
        var window_top = $window.scrollTop();
        var div_top = $mainMenuBarAnchor.offset().top;
        if (window_top > div_top) {
            // Make the div sticky.
            $mainMenuBar.addClass('stick');
            $mainMenuBarAnchor.height($mainMenuBar.height());
        } else {
            // Unstick the div.
            $mainMenuBar.removeClass('stick');
            $mainMenuBarAnchor.height(0);
        }
    });

    function getCookie(c_name) {
        if (document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start, c_end));
            }
        }
        return "";
    }

    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            }
        });
    });

});

