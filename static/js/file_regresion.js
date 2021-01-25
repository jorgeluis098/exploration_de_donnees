$(document).ready(function (){
	// $("#button_apriory").click(function(){
	// 	console.log("Hola bebe");
	// 	event.preventDefault();
	// });

	$("#button_regresion").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_regresion')[0]);
		console.log("Hola bebe entre a leer el archivo");
		$.ajax({
			url: '/regresion',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				console.log(response)
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


