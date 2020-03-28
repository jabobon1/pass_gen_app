function requestPassGen() {
    var symbols = document.getElementById('symbolsCheck');
    var register = document.getElementById('registerCheck');
    var readable = document.getElementById('readableCheck');
    var numeric = document.getElementById('numericCheck');
    var length = document.getElementById('myRange');
    const data = {
        'symbols': !symbols.checked,
        'register': !register.checked,
        'readable': !readable.checked,
        'numeric': !numeric.checked,
        'length': length.value,

    };


    fetch( '/get_pass', {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then((data) => {
            document.getElementById("result-password").value = data.password;
        })
        .catch(function (error) {
            console.log(error)
        });
}

function copyText() {
    var copyText = document.getElementById("result-password");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");

    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copied: " + copyText.value;
}

function outFunc() {
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copy to clipboard";
}

var slider = document.getElementById("myRange");
var output = document.getElementById("length_pass");
output.innerHTML = slider.value;

slider.oninput = function () {
    output.innerHTML = this.value;
};


