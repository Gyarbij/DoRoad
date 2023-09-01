$(document).ready(function(){
  $('.menu').click(function(){
      $('.navbar').toggle();
      $('.menu .fa-bars').toggleClass('fa-times');
      $('section').toggleClass('nav-toggle');
  });

  $(window).on('load scroll',function(){
      $('.navbar').hide();
      $('.menu .fa-bars').removeClass('fa-times');
      $('section').removeClass('nav-toggle');
  });
});

function generateItinerary() {
  // Show the loading popup
  document.getElementById('loading-popup').style.display = 'flex';

  // Simulate the time taken to generate the itinerary (e.g., 2 seconds)
  setTimeout(function() {
      // Your itinerary generation code here...

      // Hide the loading popup
      document.getElementById('loading-popup').style.display = 'none';

      // Scroll to the itinerary section
      document.getElementById('about').scrollIntoView({ behavior: 'smooth' });
  }, 2000);
}
