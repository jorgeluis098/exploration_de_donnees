$(document).ready(function (){

	$("#button_regresion").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_regresion')[0]);
		$.ajax({
			url: '/regresion',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				$('#resultao').val(response['keyRL'])	
				// $('#cen').DataTable();			
			},
			error: function(error){
				console.log(error);
				event.preventDefault();
			}
		});    
	});


});


