// Fetch movie titles and list them in UL#list_movies
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Loop through each movie and append its title to the list
    $.each(data.results, function(index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
    });
});
