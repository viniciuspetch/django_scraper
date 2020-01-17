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

$(function () {
  console.log('index.js loaded.');
});