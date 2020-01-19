// Search function, called each keypress to hide/show articles, filtering based on string search
function search() {
  console.log("function: search()");

  let searchString = $('#search').val().toLowerCase();
  $(".article-item").each(function () {
    let article_title = $(this).find(".card-header").text().toLowerCase();
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

  $('.collapse').on('show.bs.collapse', function () {
    $(this).prev().find(".icon-close").hide();
    $(this).prev().find(".icon-open").show();
  });
  
  $('.collapse').on('hidden.bs.collapse', function () {
    $(this).prev().find(".icon-close").show();
    $(this).prev().find(".icon-open").hide();
  });
});