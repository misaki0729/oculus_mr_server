count = 0;
function reload() {
    var img = $('#canvas').attr('src','./movie/image' + count + '.jpg?');
    console.log(count);
    setTimeout(reload, 150);
    count++;

    if(count > 1000) {
        count = 0;
    }
}

reload();