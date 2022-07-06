let n_vertex = 4;
let n_throwing = 10000;
let area = 0
let padding = 40;
let point_sz = 4;

const xs = [];
const ys = [];

function setup() {
	createCanvas(600,600);
}

function draw() {
	background(220);
	noLoop();

	strokeWeight(2);
	stroke(0);

	beginShape();
	for (let i=0; i<n_vertex; i++) {
		let fig_x = int(random(padding,width-padding));
		let fig_y = int(random(padding,height-padding));
		vertex(fig_x,fig_y);

		xs.push(fig_x);
		ys.push(fig_y);
	}
	endShape(CLOSE);

	stroke(255,0,0);
	strokeWeight(4);

	line(0,min(ys),width,min(ys));
	line(0,max(ys),width,max(ys));

	line(min(xs),0,min(xs),height);
	line(max(xs),0,max(xs),height);

	stroke(0,0,255,50);
	strokeWeight(point_sz);
	for (let i=0; i<n_throwing; i++) {
		let x = int(random(min(xs),max(xs)));
		let y = int(random(min(ys),max(ys)));
		let color = get(x,y)[0];
		if (color == 255 || color == 0)
			area++;
		point(x,y);
	}
	// console.log("The area of the white figure: " + area + "px" + " (" + round(area*0.07,3) + " mmˆ2)");
	// console.log("Percentage of area occupied by the figure: " +  round(area*100/n_throwing) + "%");
	
	textSize(18);
	fill(0);
	text("Area: " + area + "px" + " (" + round(area*0.07,3) + " mmˆ2)",width-235,height-23);
}
