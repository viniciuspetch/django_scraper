// Search function, called each keypress to hide/show articles, filtering based on string search
function search() {
  console.log("function: search()");

  let searchString = $('#search').val().toLowerCase();
  $(".article-item").each(function () {
    let article_title = $(this).find(".card-body").text().toLowerCase();
    if (article_title.includes(searchString)) {
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