var deployments = (function() {
    var cluster = null;
    var timeRange = getTimeRange();

    var getTimeRange = function () {
        var parts, i,
            qs = window.location.search.substr(1).split('&'),
            ret = {};
        for (i = 0; i < qs.length; i++) {
            parts = qs[i].split('=');
            if (parts[0] === 'from') {
                ret[parts[0]] = parts[1];
            } else if (parts[0] === 'until') {
                ret[parts[0]] = parts[1];
            } else if (parts[0] === 'tz') {
                ret[parts[0]] = parts[1].replace(/\//g, '%2F');
            }
        }
        return ret;
    };

})();
