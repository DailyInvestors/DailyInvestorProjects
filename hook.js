// This file contains the JavaScript functionality for the Google search homepage.
// It handles the search button click events and redirects the user to the search results page based on the input.

document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.search-buttons button:first-child');
    const luckyButton = document.querySelector('.search-buttons button:last-child');
    const inputField = document.createElement('input');

    // Create an input field for the search
    inputField.type = 'text';
    inputField.placeholder = 'Search Google or type a URL';
    document.querySelector('.container').insertBefore(inputField, searchButton);

    searchButton.addEventListener('click', function() {
        const query = inputField.value;
        if (query) {
            window.location.href = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
        }
    });

    luckyButton.addEventListener('click', function() {
        const query = inputField.value;
        if (query) {
            window.location.href = `https://www.google.com/search?btnI=I%27m+Feeling+Lucky&q=${encodeURIComponent(query)}`;
        }
    });
});