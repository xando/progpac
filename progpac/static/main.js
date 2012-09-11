$(function() {

    // Level View
    if( $("#level").length ) {

	function setup_code_counter() {
	    var $button = $('.move.btn');

	    var $code_size = $button.find('.code-size');
	    var $code_maxsize = $button.find('.code-maxsize');
	    var code = $('.editor textarea').val();

	    var code_length = $.map(code.split("\n"), function(element) {
		return element.replace(/[\s:]/g,"");
	    }).join("").length;

	    $code_size.html(code_length);

	    if (parseInt($code_size.html(),10) > parseInt($code_maxsize.html(),10)) {
		$button.removeClass('btn-success');
		$button.addClass('btn-warning');
	    } else {
		$button.addClass('btn-success');
		$button.removeClass('btn-warning');
	    }
	}

	setup_code_counter();

	$('.editor textarea').on('keyup', function() {
            setup_code_counter();
	});

	$('form').ajaxForm({
	    beforeSubmit: function(a, b, c) {
		game.render_dynamic();
		$('.alert-error').hide();
	    },
    	    success: function(response) {

    		if (response.errors.length) {
    		    $('.alert-error').show();

		    $.each(response.errors, function(i,e) {
			$('.alert-error .message').append($('<li>'+e+'</li>'));
		    })


    		} else {
		    if (response.success) {
			game.post_animate = function() {

			    $('#success-info a.next-level')
				.attr('href', response.next_level);

			    $('#success-info .result').text(response.code_length);

			    setTimeout(function() {
				$('#success-info').modal('show');
			    }, 500);

			}
		    } else {
			game.post_animate = function() {
			    var tooltip = game.guy_box.tooltip({
				'title': 'Ops, try again!',
				'placement': 'top',
				'trigger': 'manual'
			    });
			    tooltip.tooltip("show");
			}
		    }
    		    game.render_dynamic(response.code);

    		}
    	    }
	});

	$('.reset').on('click', function(e) {
	    e.preventDefault();
	    game.render_dynamic();
	    $('.move').removeAttr("disabled");
	});
    }

    // Results View
    if( $("#results").length ) {

	$('.nav-tabs a').click(function (e) {
	    e.preventDefault();
	    $(this).tab('show');
	});
    }
})
