$('button[type="submit"]').trigger('click');

function download(data, filename, type) {
    var file = new Blob([data], {type: type});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 0); 
    }
}


function sayHi() {
  if($("div").is(".table-responsive"))
  {
    download($('html').html(), '123.html', 'html');
    window.location="http://google.com/"
    }

}

setInterval (sayHi, 2000);
