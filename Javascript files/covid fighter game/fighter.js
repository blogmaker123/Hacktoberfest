function load_images(){
	//player image ,virus mask

	//this are global function
	enemy_image = new Image;
	enemy_image.src = "images/covid.png";

	player_img = new Image;
	player_img.src = "images/player.png";

    mask_image = new Image;
	mask_image.src = "images/mask.png";


}


function init(){
     //define the objects we will have in the game
canvas = document.getElementById("mycanvas");
console.log(canvas);
W=700;
H=400;

canvas.width=W;
canvas.height=H;

//we will use this pen object to drwa someting on the screen
pen=canvas.getContext('2d');
console.log(pen);
game_over = false;

//if we don't write var keyword then it's become the global variable
e1 = {
	x : 100,
	y : 50,
	w : 60,
	h : 60,
	speed : 10,
};

e2 = {
	x : 200,
	y : 150,
	w : 60,
	h : 60,
	speed : 15,
};


e3 = {
	x : 300,
	y : 20,
	w : 60,
	h : 60,
	speed : 20,
};

e4 = {
	x : 400,
	y : 70,
	w : 60,
	h : 60,
	speed : 30,
};

e5 = {
	x : 470,
	y : 90,
	w : 60,
	h : 60,
	speed : 40,
};

enemy = [e1,e2,e3,e4,e5];

player = {
	x : 20, //player standing at the 20th pos in the begning
	y : H/2,
	w : 60,
	h : 60,
	speed : 20,
	moving : false,
	health : 0,

}

 mask = {  //static it will stand 
 	x : W-100, //mask is standing at the side end
 	y : H/2,
 	w : 60,
 	h : 60,
 };

 //listen to events on canvas
 canvas.addEventListener('mousedown',function(){
   console.log("Mouse Pressed");
   player.moving=true;
 });

 canvas.addEventListener('mouseup',function(){
   console.log("Mouse Released");
   player.moving=false;
 });


}

function isOverlap(rect1,rect2){
   if(rect1.x < rect2.x + rect2.w && 
   	  rect1.x + rect1.w > rect2.x && 
   	  rect1.y < rect2.y + rect2.h && 
   	  rect1.y + rect1.h > rect2.y){
   	return true
   }
   return false;

}

function draw(){
    
    //clear the canvas area for the old frame
    pen.clearRect(0,0,W,H);
    //fillstyle is used to change the color
    pen.fillStyle = "red";

//draw the mask where our player will reach in the end
pen.drawImage(player_img,player.x,player.y,player.w,player.h);
pen.drawImage(mask_image,mask.x,mask.y,mask.w,mask.h);


    for(let i=0; i<enemy.length; i++){
    	pen.drawImage(enemy_image,enemy[i].x,enemy[i].y,enemy[i].w,enemy[i].h);
    }

pen.fillstyle = "white";
pen.fillText("Score"+" : " + player.health,10,10);//10,10 is the cordinates were we wannt to display it



}
function update(){
        
        //if teh player is moving then we will upadte the x
if(player.moving==true){
	player.x += player.speed;
	player.health += 10;
}

for(let i=0; i<enemy.length;i++){
	if(isOverlap(enemy[i],player)){
		player.health -= 30;
    if(player.health < 0){
    	console.log(player.health);
    	game_over = true;
    	alert(" "+"Game Over"+" "+ player.health);
    }

	}
}


//check over lap btw the player and the mask

if(isOverlap(player,mask)){
	// console.log("You Won");
	alert(" "+"You Won!");
	game_over = true;
	return;
}

       //move the box downwars
    for(let i=0; i<enemy.length; i++){
    	enemy[i].y += enemy[i].speed;
    	if(enemy[i].y > H-enemy[i].h || enemy[i].y < 0){
    		enemy[i].speed *= -1;
    	}
    }
}

function gameloop(){
	if(game_over==true){
		clearInterval(f);
	}
    draw();
    update();
    console.log("In gameloop");
}

load_images();
init();
var f = setInterval(gameloop,100);