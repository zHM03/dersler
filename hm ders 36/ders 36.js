$(document).ready(function () {
    var tasks = $(".task");
    tasks.on("dragstart", function (event) {
        event.originalEvent.dataTransfer.setData(
            "text/plain",
            event.target.innerText
        );
        $(this).addClass("dragging");
    });
    tasks.on("dragend", function () {
        $(this).removeClass("dragging");
    });
    $(".column").on("dragover", function (event) {
        event.preventDefault();
    });
    $(".column").on("drop", function (event) {
        event.preventDefault();
        var data = event.originalEvent.dataTransfer.getData("text/plain");
        var taskText = data.replace(" X", "");
        if($(this).attr("id") !== "todo") {
            $("#todo.task").each(function () {
                if($(this).text().trim() === taskText) {
                    $(this).remove();
                }
            });
        }
        $(this)
        .find(".add-task")
        .before(
            '<div class="task" draggable="true">' +
            taskText +
            ' <span class="remove">X</span></div>'
        );
    });
    $(".add-task button").on("click", function () {
        var taskText = $(this).prev("input").val();
        if(taskText) {
            $(this)
            .parent(".add-task")
            .before(
                '<div class="task" draggable="ture"' +
                taskText +
                ' <span class="remove">X</span></div>'
            );
            $(this).prev("input").val("");
        }
    });
    $(document).on("click", ".remove", function () {
        $(this).parent(".task").remove();
    });
});