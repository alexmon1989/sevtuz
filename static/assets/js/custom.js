var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};


$(document).ready(function () {
    $('input[name="play_type"]').change(function() {
        var s = '';

        var age = getUrlParameter('age');
        if (age) {
            s += 'age=' + age;
        }

        var play_types = $('input[name="play_type"]:checked').serialize();
        if (play_types) {
            if (age) {
                s = s + '&';
            }
            s += play_types;
        }

        if (s) {
            s = '?' + s;
        }

        window.location = s;
    });
});