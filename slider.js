document.addEventListener('DOMContentLoaded', function () {
    const rightArrow = document.getElementById('right');
    const leftArrow = document.getElementById('left');
    const carousel = document.querySelector('.carousel');

    // Function to handle clicking on the right arrow
    rightArrow.addEventListener('click', function () {
        carousel.scrollBy({
            left: 250,
            behavior: 'smooth'
        });
    });

    // Function to handle clicking on the left arrow
    leftArrow.addEventListener('click', function () {
        carousel.scrollBy({
            left: -250,
            behavior: 'smooth'
        });
    });
});
