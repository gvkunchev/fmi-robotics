function send_command(name, parameter){
    if (parameter !== undefined){
        console.log(name + '=' + parameter);
        $.get("command?name=" + name + '&parameter=' + parameter);
    }
    else {
        console.log(name);
        $.get("command?name=" + name);
    }
}

$(document).ready(function(){

    // Handle gear change from the select menu
    $('#gear').change(function(){
        var value = $(this).val();
        var gears = $(this).find('option').length;
        send_command('set_speed', value/gears);
    }).change();


    // Handle up/down arrow button events
    $('#button_up').mousedown(function(){
        $(this).addClass('pressed');
        send_command('fwd');
    });
    $('#button_down').mousedown(function(){
        $(this).addClass('pressed');
        send_command('bwd');
    });
    $('#button_up,#button_down').mouseup(function(){
        $(this).removeClass('pressed');
        send_command('stop');
    });


    // Handle left/right arrow button events
    $('#button_left').mousedown(function(){
        $(this).addClass('pressed');
        send_command('left');
    });
    $('#button_right').mousedown(function(){
        $(this).addClass('pressed');
        send_command('right');
    });
    $('#button_left,#button_right').mouseup(function(){
        $(this).removeClass('pressed');
        send_command('center');
    });


    // Trigger control events on keydowns
    $(window).keydown(function(event){
        if (event.originalEvent.repeat){
            return;
        }
        else if (event.key === "ArrowUp"){
            $('#button_up').trigger('mousedown');
        }
        else if (event.key === "ArrowDown"){
            $('#button_down').trigger('mousedown');
        }
        else if (event.key === "ArrowLeft"){
            $('#button_left').trigger('mousedown');
        }
        else if (event.key === "ArrowRight"){
            $('#button_right').trigger('mousedown');
        }
    })


    // Trigger control events on keyups
    $(window).keyup(function(event){
        if (event.key === "ArrowUp"){
            $('#button_up').trigger('mouseup');
        }
        else if (event.key === "ArrowDown"){
            $('#button_down').trigger('mouseup');
        }
        else if (event.key === "ArrowLeft"){
            $('#button_left').trigger('mouseup');
        }
        else if (event.key === "ArrowRight"){
            $('#button_right').trigger('mouseup');
        }
    })

    // Trigger control events on keypress
    $(window).keypress(function(event){
        if (event.code === "Digit1") {
            $('#gear').val(1).change();
        }
        else if (event.code === "Digit2") {
            $('#gear').val(2).change();
        }
        else if (event.code === "Digit3") {
            $('#gear').val(3).change();
        }
        else if (event.code === "Digit4") {
            $('#gear').val(4).change();
        }
    })

    setInterval(function(){
        $.get("get_distance", function(data, status){
            $('#distance').html(data['distance'].toFixed(1));
        });
    }, 1000);
    
})