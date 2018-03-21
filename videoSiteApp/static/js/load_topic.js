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
        }
    });
});

$(document).ready(function () {
    var $select_subject = $('select#select_subject');
    $select_subject.change()
});