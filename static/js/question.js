$(function(){
		$(".choose_area_title").click(function(){
			$(".choose_area_cont").slideToggle();
			$(".choose_subject_cont").slideUp();
			$(".choose_shcool_cont").slideUp();
			$('.choose_area_title img').toggleClass('on');
			$(".choose_shcool_title img").removeClass('on');
			$(".choose_subject_title img").removeClass('on');
			$(".choose_area_title h3").text('选择问题大类');
			$(".choose_shcool_title h3").text('选择问题子类');
			$('#sec_type').empty();
			$('#th_type').empty();
		});
		$(".choose_area_cont li h4").click(function(){
			$(".choose_shcool_title").attr('disabled',false);
			$(".choose_shcool_cont").slideDown();
			$(".choose_area_cont").slideUp();
			$(".choose_area_title img").removeClass('on');
			$(".choose_shcool_title img").addClass('on');
			$(".choose_area_title h3").text($(this).text())
			var main_type = {'main_type': $(this).text()}
			$.ajax({
				type: 'POST',
				url: '/question/sec/',
				data: main_type,
				dataType: 'json',
				success: function(ret){
					for (var i = 0, len = ret.sec_type.length; i < len; i++) {
						var $preview = $('<ul><li><h3>' + ret.sec_type[i] + '</h3></li></ul>');
						$('#sec_type').append($preview);
					}
                    $(".choose_shcool_cont li h3").click(function(){
						$(".choose_subject_title").attr('disabled',false);
						$(".choose_subject_cont").slideDown();
						$(".choose_shcool_cont").slideUp();
						$(".choose_shcool_title img").removeClass('on');
						$(".choose_subject_title img").addClass('on');
						$(".choose_shcool_title h3").text($(this).text())
						var sec_type = {'sec_type': $(this).text()}
						$.ajax({
							type: 'POST',
							url: '/question/th/',
							data: sec_type,
							dataType: 'json',
							success: function(ret){
								for (var i = 0, len = ret.th_type.length; i < len; i++) {
									var $preview = $('<ul><li><h4>' + ret.th_type[i] + '</h4></li></ul>');
									$('#th_type').append($preview);
								}
								$(".choose_subject_cont li h4").click(function(){
									$(".choose_subject_cont").slideUp();
									$(".choose_subject_title img").removeClass('on');
									var th_type = {'th_type': $(this).text()}
									console.log(th_type)
									$.ajax({
										type: 'POST',
										url: '/question/sol/',
										data: th_type,
										dataType: 'json',
										success: function(ret){
											console.log(ret.sol)
											var $question = $('<ul><li><h4>' + th_type.th_type + '</h4></li></ul>');
											var $preview = $('<ul><li><h4>' + ret.sol + '</h4></li></ul>');
											$('#sol').append($question);
											$('#sol').append($preview);
											$("#sol").slideDown();
                                        }
                                    });
								});
							}
						});
                    });
				}
			});
		});
		$(".choose_shcool_title").click(function(){
			$(".choose_shcool_cont").slideToggle();
			$(".choose_area_cont").slideUp();
			$(".choose_subject_cont").slideUp();
			$('.choose_shcool_title img').toggleClass('on');
			$(".choose_area_title img").removeClass('on');
			$(".choose_subject_title img").removeClass('on');
			$(".choose_shcool_title h3").text('选择问题子类');
			$('#th_type').empty();
		});
		$(".choose_subject_title").click(function(){
			$(".choose_subject_cont").slideToggle();
			$(".choose_shcool_cont").slideUp();
			$(".choose_area_cont").slideUp();
			$('.choose_subject_title img').toggleClass('on');
			$(".choose_area_title img").removeClass('on');
			$(".choose_shcool_title img").removeClass('on')
			$('#sol').empty();
		});
});
