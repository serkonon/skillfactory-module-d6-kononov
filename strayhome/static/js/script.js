function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function selectElement(id, valueToSelect) {
    let element = document.getElementById(id);
    element.value = valueToSelect;
}

let pt = getParameterByName("pet-type");
let pg = getParameterByName("pet-gender");

//console.log(pt, pg);

if (pt) {
    selectElement("pet-type", pt);
}
if (pg) {
    selectElement("pet-gender", pg);
}
