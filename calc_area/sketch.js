let n_vertex = 4;
let n_throwings = 0;

let area = 0
let tot_area = 0;

let padding = 40;

// arrays that will store the random coordinates of the figures
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
		// create random coordinates and draw the figure
		let fig_x = int(random(padding,width-padding));
		let fig_y = int(random(padding,height-padding));
		vertex(fig_x,fig_y);

		// store the coordinates in arrays
		xs.push(fig_x);
		ys.push(fig_y);
	}
	endShape(CLOSE);

	stroke(255,0,0);
	strokeWeight(4);

	// draw the rectangle that contains the figure
	line(0,min(ys),width,min(ys));
	line(0,max(ys),width,max(ys));

	line(min(xs),0,min(xs),height);
	line(max(xs),0,max(xs),height);

	let tot_area = (max(xs)-min(xs))*(max(ys)-min(ys));
	n_throwings = tot_area; 

	for (let i=0; i<n_throwings; i++) {
		// get random coordinate
		let x = int(random(min(xs),max(xs)));
		let y = int(random(min(ys),max(ys)));

		// get the color of a pixel at that coordinates
		let color = get(x,y)[0];

		// check if x and y are in the figure by checking the color
		if (color == 255 || color == 0)
			area++;
	}
	
	textSize(18);
	stroke(220);
	fill(0);

	// display area of the figure and percentage of the red rectangle occupied by it
	text("Area: " + area + "px" + " (" + round(area*100/tot_area,1) + "%)", width-200, height-23);
}
