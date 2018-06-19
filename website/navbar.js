window.init = function() {
    var navElems = [ { name: 'Home', url: '/index.html' },
                     { name: 'People', url: '/people.html' },
                     { name: 'Background', url: '/background.html' },
                     { name: 'Mozilla Challenge', url: '/mozilla.html' } ];
    for(var i in navElems) {
        var e = navElems[i];
        var url = window.location.href;
        if(url.indexOf(e.url) >= 0) {
            $('#nav').append('<div id="active-nav">' + e.name + '</div>');
        } else {
            $('#nav').append('<a href="./' + e.url + '">' + e.name + '</a>');
        }
    }
}
$(document).ready(window.init);
