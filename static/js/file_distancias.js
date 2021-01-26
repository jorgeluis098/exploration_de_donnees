$(document).ready(function (){
	$("#button_distancias").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_distancias')[0]);
		formData.append('distances', $('#select_distancias').val() )
		$.ajax({
			url: '/read_distancias',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				$('#matrizDistancias').html(response['keyDistancias'])	
				$('#matrizDistanciass').DataTable();			
			},
			error: function(error){
				console.log(error);
				event.preventDefault();
			}
		});    
	});


});


