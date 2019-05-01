// here is my java script event, which prevent closing dropdown menu after choosing options inside the menu

$('.dropdown-menu').on('click', function(e) {
  e.stopPropagation();
});