function setup() {
	createCanvas(600,600);
}

function draw() {
	background(220);
	noLoop();
	strokeWeight(2);
	for (let i=0; i<width; i+=width/20) {
		line(0,i,width,i);
	}
	for (let i=0; i<height; i+=height/20) {
		line(i,0,i,height);
	}

	let n = 4;
	const xs = [];
	const ys = [];

	beginShape();
	for (let i=0; i<n; i++) {
		x = int(random(20,width-20));
		y = int(random(20,height-20));
		vertex(x,y);
		xs.push(x);
		ys.push(y);
	}
	endShape(CLOSE);

	for (let i=0; i<n; i++) {
	}
}
