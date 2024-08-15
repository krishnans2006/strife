$(document).ready(() => {
    // Style input boxes
    inputSelector = 'input[type="text"], input[type="password"], input[type="email"], input[type="number"], input[type="tel"], input[type="search"], input[type="url"], input[type="date"], input[type="file"]';
    inputBoxStyle = 'bg-gray-800 text-white border border-gray-600 rounded-md p-2 focus:outline-none focus:border-blue-500';
    $(inputSelector).addClass(inputBoxStyle);
})
