goog.provide('game');

//get requirements
goog.require('lime.Director');
goog.require('lime.Scene');
goog.require('lime.Layer');

goog.require('lime.animation.MoveBy');
goog.require('lime.animation.Sequence');
goog.require('lime.animation.FadeTo');



game.inits = function(element, level) {

    this.Turn = function(direction) {
    lime.animation.Animation.call(this);
	this.direction = direction;
    };
    goog.inherits(this.Turn, lime.animation.Animation);

    this.Turn.prototype.update = function(t, target) {
	if (this.status_ == 0) return;

	var face_list = [
	    STATIC_URL + 'assets/guy_front.png',
	    STATIC_URL + 'assets/guy_right.png',
	    STATIC_URL + 'assets/guy_back.png',
	    STATIC_URL + 'assets/guy_left.png'
	]
	target.setFill(face_list[this.direction])
    };


    this.element = element;
    this.level = level;

    this.tile_w = element.width() / this.level[0].length;
    this.tile_h = this.tile_w * 1.7;
    this.tile_x = this.tile_w * 0.84;
    this.tile_y = this.tile_h * 0.585;

    this.position_y = this.tile_h - this.tile_h / 2;
    this.position_x = this.tile_w - this.tile_w / 2;

    this.animations = [
	this.move_down = new lime.animation.MoveBy(0, this.tile_h/2),
	this.move_right = new lime.animation.MoveBy(this.tile_w, 0),
	this.move_up = new lime.animation.MoveBy(0, -this.tile_h/2),
	this.move_left = new lime.animation.MoveBy(-this.tile_w, 0)
    ]

    this.element.height(this.tile_x * this.level.length + this.tile_w);

    this.director = new lime.Director($('#map').get(0));
    this.scene = new lime.Scene();

    // Static Layers
    this.ground_layer = new lime.Layer()
    	.setPosition(this.position_x, this.position_y);

    this.blocks_layer = new lime.Layer()
    	.setPosition(this.position_x, this.position_y - (this.tile_h * 0.24));

    // Shadows Layers
    this.shadows = new lime.Layer()
    	.setPosition(this.position_x, this.position_y);

    this.shadows_back = new lime.Layer()
    	.setPosition(this.position_x, this.position_y);

    this.scene.appendChild(this.ground_layer);
    this.scene.appendChild(this.shadows_back);
    this.scene.appendChild(this.blocks_layer);
    this.scene.appendChild(this.shadows);

    // Game Layers
    this.game_layer = new lime.Layer()
    	.setPosition(this.position_x, this.position_y - (this.tile_h * 0.24))

    this.scene.appendChild(this.game_layer)

    this.blocks_layer_top = new lime.Layer()
	.setPosition(this.position_x, this.position_y - (this.tile_h * 0.24));

    this.scene.appendChild(this.blocks_layer_top)

    this.guy = undefined;

    this.stars = []

    var self = this;
    $.each(this.animations, function(i, animation) {
	goog.events.listen(animation, lime.animation.Event.STOP, function(e){
	    self.animate_starts();
	});
    })
}

game.animate_starts = function() {
    var self = this;
    $.each(this.stars, function(i,star) {
	var distance = goog.math.Coordinate.distance(
	    star.getPosition(), self.guy.getPosition()
	)

	if (distance < self.tile_w/2) {
	    star.runAction(
		new lime.animation.FadeTo(0).setDuration(0.1)
	    );
	}
    });
}

game.put_block = function(tile_image, x, y) {
    return new lime.Sprite()
	.setFill(STATIC_URL + tile_image)
	.setSize(this.tile_w, this.tile_h)
	.setPosition(this.tile_y * y, this.tile_x * x);
}

game.put_top_block = function(tile_image, x, y) {
    return new lime.Sprite()
	.setFill(STATIC_URL + tile_image)
	.setSize(this.tile_w, this.tile_h * 0.47368421052631576)
	.setPosition(this.tile_y * y, this.tile_x * x - this.tile_h * 0.27368421052631576);
}


game.render_shadows = function() {

    var self = this;

    function is_field(i, j) {
	if ( 0 <= i && i < self.level.length && 0 <= j && j < self.level[0].length)  {
	    var element = self.level[i][j];

	    if ( $.inArray(element, ['.','u','o']) > -1 ) {
		return true
	    }
	}
	return false
    }

    function is_obstacle(i, j) {
	if ( 0 <= i && i < self.level.length && 0 <= j && j < self.level[0].length)  {
	    var element = self.level[i][j];

	    if ( $.inArray(element, ['*','-','#']) > -1 ) {
		return true
	    }
	}
	return false
    }

    $.each(this.level, function(i, line) {
    	$.each(line, function(j, element) {

	    if (is_field(i, j) && is_obstacle(i-1, j) ) {
	    	self.shadows.appendChild(
	    	    self.put_block('assets/Shadow North.png', i, j)
	    	)
	    }

	    if (is_field(i, j) && is_obstacle(i+1, j) ) {
	    	self.shadows_back.appendChild(
	    	    self.put_block('assets/Shadow South.png', i, j)
	    	)
	    }

	    if (is_field(i, j) && is_obstacle(i, j-1)) {
	    	self.shadows_back.appendChild(
	    	    self.put_block('assets/Shadow West.png', i, j)
	    	)
	    }

	    if (is_field(i, j) && is_obstacle(i, j+1)) {
	    	self.shadows_back.appendChild(
	    	    self.put_block('assets/Shadow East.png', i, j)
	    	)
	    }

	    if (is_field(i, j) && is_obstacle(i+1,j+1) && !is_obstacle(i,j+1) ) {
	    	self.shadows_back.appendChild(
	    	    self.put_block('assets/Shadow South East.png', i, j)
	    	)
	    }

	    if (is_field(i, j) && is_obstacle(i+1,j-1) && !is_obstacle(i,j-1)) {
	    	self.shadows_back.appendChild(
	    	    self.put_block('assets/Shadow South West.png', i, j)
	    	)
	    }

	    if (is_field(i, j) && is_obstacle(i-1,j-1) && !is_obstacle(i,j-1) && !is_obstacle(i-1,j)) {
	    	self.shadows_back.appendChild(
	    	    self.put_block('assets/Shadow North West.png', i, j)
	    	)
	    }

	    if (is_field(i, j) && is_obstacle(i-1,j+1) && !is_obstacle(i,j+1) && !is_obstacle(i-1, j) ) {
	    	self.shadows_back.appendChild(
	    	    self.put_block('assets/Shadow North East.png', i, j)
	    	)
	    }

	});
    });

}

game.render_static = function() {

    var self = this;
    $.each(this.level, function(i, line) {
    	$.each(line, function(j, element) {

    	    self.ground_layer.appendChild(
    	    	self.put_block('assets/Grass Block.png', i, j)
    	    );

    	    if (element == '*') {
    	    	self.blocks_layer.appendChild(
	    	    self.put_block('assets/Wall Block.png', i, j)
	    	)
    	    }

	    if (element == '-') {
    	    	self.blocks_layer.appendChild(
	    	    self.put_block('assets/Stone Block.png', i, j)
	    	)
		self.blocks_layer_top.appendChild(
	    	    self.put_top_block('assets/Stone Block_top.png', i, j)
	    	)
    	    }

    	});
    });

    this.render_shadows();
}

game.render_dynamic = function(code) {
    $('.tooltip').hide();
    $('.popover').hide();

    this.game_layer.removeAllChildren();

    this.stars = [];

    var self = this;
    $.each(this.level, function(i, line) {
    	$.each(line, function(j, element) {

	    if (element == 'o') {
		var star = self.put_block('assets/Star.png', i, j);

    	    	self.game_layer.appendChild(star);
		self.stars.push(star);

    	    } else if (element == 'u') {
		guy = self.put_block('assets/guy_front.png', i, j);
    	    	self.game_layer.appendChild(guy);
	    }

    	});
    });

    this.guy = guy;

    if (code) {
    	this.animate(code);
    }
};


game.get_real_direction = function(direction) {
    var e = direction%4;
    return (e < 0 ? e + 4 : e)
}

game.generate_animation = function(code) {
    var moves_list = [];
    var direction = 0;

    var self = this;
    $.each(code.replace("@",""), function(i, element) {

	if (element == 's') {
	    var animation = self.animations[self.get_real_direction(direction)];
	    animation.setDuration(0.2);
	    animation.setEasing(lime.animation.Easing.LINEAR);
	    moves_list.push(animation)
	}
	if (element == 'r') {
	    moves_list.push(
		new self.Turn(self.get_real_direction(--direction)).setDuration(0.1)
	    )
	}
	if (element == 'l') {
	    moves_list.push(
		new self.Turn(self.get_real_direction(++direction)).setDuration(0.1)
	    )
	}

    });

    if (moves_list.length == 1) {
	// LimeJS was having problems with
	// rendering single animation more then once
	moves_list.push(new lime.animation.MoveBy(0,0));
    }


    return moves_list;
}

game.animate = function(code) {
    this.animation_steps = this.generate_animation(code);

    if (this.animation) {
	this.animation.stop();
    }

    $('button.move').attr('disabled', 'disabled');
    this.animation = new lime.animation.Sequence(this.animation_steps);
    this.animation.addTarget(this.guy);
    this.animation.enableOptimizations();
    this.animation.play();

    var self = this;
    goog.events.listen(this.animation, lime.animation.Event.STOP, function(e){
	self.setup_guy_box();
	self.post_animate();
	$('button.move').removeAttr("disabled");
    });
}

game.setup_guy_box = function() {
    var box = this.guy.getBoundingBox();

    if ($("#guy-box").length) {
	$("#guy-box").remove();
    }

    var guy_box = $('<div/>', {
	id: 'guy-box'
    }).prependTo(this.element);

    guy_box.css('top', box.top + this.tile_h / 2 );
    guy_box.css('left', box.left + this.tile_w / 2);

    var $guy_speech = $('#guy-speech');

    if ($guy_speech.html().length != 0) {
	this.speech_buble = guy_box.popover({
    	    'content':$('#guy-speech').html(),
    	    'trigger': 'manual'
	});

	$('.popover').live("click", function(event){
    	    self.speech_buble.popover('hide');
	});

	var self = this;
	guy_box.click(function(event){
    	    self.speech_buble.popover('toggle');
	});
    }

    this.guy_box = guy_box;
}

game.show_speech_buble = function() {
    if(this.speech_buble)
    	this.speech_buble.popover('show');
}

game.post_render = function() {
    $('.editor textarea').height(game.element.height() - 112);

    this.setup_guy_box();
    this.show_speech_buble();
};

game.post_animate = function() {};

game.level_script = function () {};


goog.exportSymbol('game.start', game.start);

$(document).ready(function() {

    if (LEVEL) {
	game.inits($('#map'), LEVEL);

	game.render_static();
	game.render_dynamic();
	game.post_render();

	game.director.replaceScene(game.scene);
	game.director.makeMobileWebAppCapable();
    }

});
