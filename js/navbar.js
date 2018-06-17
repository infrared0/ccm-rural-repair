window.init = function() {
    var navElems = [ { name: 'Home', url: '/home.html' },
                     { name: 'People & Places', url: '/people.html' },
                     { name: 'Mozilla Challenge', url: '/mozilla.html' },
                     { name: 'Background', url: '/background.html' } ];
    for(var i in navElems) {
        e = navElems[i];
        $('#nav').append('<a href="' + e.url + '">' + e.name + '</a>');
    }
}
$(document).ready(window.init);
