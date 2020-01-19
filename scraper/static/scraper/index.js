// Search function, called each keypress to hide/show articles, filtering based on string search
function search() {
  console.log("function: search()");

  let searchString = $('#search').val();
  console.log(searchString);
  $(".article-item").each(function () {
    if ($(this).find(".card-body").text().includes(searchString)) {
      $(this).show();
    } else {
      $(this).hide();
    }
  });
}

// Just to show the JS was loaded
$(function () {
  console.log('index.js loaded.');
});