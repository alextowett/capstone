// Search Bar START
function search() {
    const input = document.getElementById("search-input");
    const query = input.value;

    // Perform any necessary actions with the query, such as sending it to a Django backend

    input.value = ""; // Clear the input field after searching
}

const placeholderTexts = ["All Project...", "Live Projects...", "Complete Projects...", "Private Projects...", "Acquired Projects...",];

function animatePlaceholder() {
    const input = document.getElementById("search-input");
    let currentIndex = 0;

    setInterval(() => {
        input.placeholder = `Search ${placeholderTexts[currentIndex]}`;
        currentIndex = (currentIndex + 1) % placeholderTexts.length;
    }, 2000);
}

animatePlaceholder();

//Search Logic
function submitSearch() {
    const searchInput = document.getElementById('search-input');
    const query = searchInput.value.trim();

    if (query) {
        window.location.href = `/search/?q=${encodeURIComponent(query)}`;
    }
}

document.getElementById('search-input').addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        submitSearch();
    }
});

// Search Bar END



// Navigation Bar START
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

// Navigation Bar END

// Comments & Reviews START

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    var reviews = document.querySelectorAll(".review-card"); // Select all review cards
    var currentReview = 0; // Index of the currently displayed review

    // Function to show a specific review
    function showReview(index) {
        // Hide all reviews
        for (var i = 0; i < reviews.length; i++) {
            reviews[i].style.display = "none";
        }

        // Show the review at the specified index
        reviews[index].style.display = "grid";
    }

    // Function to show the next review
    function showNextReview() {
        currentReview++;
        if (currentReview >= reviews.length) {
            currentReview = 0; // Start from the beginning if the last review is reached
        }
        showReview(currentReview);
    }

    // Function to show the previous review
    function showPreviousReview() {
        currentReview--;
        if (currentReview < 0) {
            currentReview = reviews.length - 1; // Go to the last review if the first review is reached
        }
        showReview(currentReview);
    }

    // Show the initial review
    showReview(currentReview);

    // Set an interval to automatically show the next review every 5 seconds
    setInterval(showNextReview, 10000);

    // Add event listeners to the navigation buttons
    var previousButton = document.querySelector(".chevron.left");
    var nextButton = document.querySelector(".chevron.right");

    previousButton.addEventListener("click", showPreviousReview);
    nextButton.addEventListener("click", showNextReview);
});
// Comments & Reviews END

// Milestones Table START
$(document).ready(function () {
    // Prevent the default behavior of anchor tags when clicked inside #milestones-pagination
    $(document).on("click", "#milestones-pagination a", function (e) {
        e.preventDefault();
        var pageUrl = $(this).attr("href");
        var pageNumber = pageUrl.split("=")[1]; // Extract the page number from the URL
        pageNumber = parseInt(pageNumber); // Convert the page number to an integer

        // Fetch the paginated results using AJAX
        $.ajax({
            url: pageUrl,
            type: "GET",
            dataType: "html",
            success: function (data) {
                // Update the table body with the new data
                $("#milestones-tbody").html($(data).find("#milestones-tbody").html());

                // Update the URL in the address bar using the HTML5 History API
                history.pushState(null, null, pageUrl);
            },
            error: function (error) {
                console.error(error);
            }
        });
    });
});

// Milestones Table END

