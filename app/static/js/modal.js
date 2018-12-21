$(document).ready(function () {
    $('body').bootstrapMaterialDesign();
  });
  $('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })