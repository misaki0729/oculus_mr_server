count = 0;
function reload() {
    var img = $('#canvas').attr('src','./movie/test' + count + '.jpg?');
    console.log(count);
    setTimeout(reload, 150);
    count++;
}

console.log("test");
reload();