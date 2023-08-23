// JavaScript to toggle display
document.addEventListener('DOMContentLoaded', function() {
    const flashWrapper = document.querySelector('.flash-wrapper');
    if (flashWrapper) {
        flashWrapper.style.display = 'block'; // Show initially
        flashWrapper.classList.add('flash-fade');
        
        // Add event listener to hide the wrapper after animation ends
        flashWrapper.addEventListener('animationend', function() {
            flashWrapper.style.display = 'none'; // Hide after animation
        });
    }
});

