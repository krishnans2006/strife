function getContrastingBW(hex) {
    if (hex.indexOf('#') === 0) {
        hex = hex.slice(1);
    }
    // convert 3-digit hex to 6-digits.
    if (hex.length === 3) {
        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
    }
    if (hex.length !== 6) {
        throw new Error('Invalid HEX color.');
    }
    const r = parseInt(hex.slice(0, 2), 16),
        g = parseInt(hex.slice(2, 4), 16),
        b = parseInt(hex.slice(4, 6), 16);

    // https://stackoverflow.com/a/3943023/11317931
    return (r * 0.299 + g * 0.587 + b * 0.114) > 186
        ? '#000000'  // too bright
        : '#FFFFFF';  // too dark
}

$(document).ready(() => {
    $('.role-select-trigger').each(function() {
        const mainColor = $(this).data('role-color');
        const BW = getContrastingBW(mainColor);

        const roleSelected = $(this).data('role-selected');

        if (roleSelected) {
            console.log(mainColor, BW);
            $(this).css('background-color', mainColor);
            $(this).css('color', BW);
        } else {
            // background-color: bg-gray-600 (#4b5563)
            $(this).css('color', mainColor);
        }
    });
});
