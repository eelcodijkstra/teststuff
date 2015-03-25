postxy = 0.5;
postheight = 1.001;
postseparation = 1.5;
membranethickness = 0.05;
membrane_xseparation = 1;
membrane_yseparation = 1;
xslab = 9.5;
yslab = 6;
zslab = 1;

module post(size,height) {
  color("Red") cube(size=[size,size,height],center=false);
}

module slab(x,y,z) {
	cube(size=[x,y,z],center=false);
}

module membrane(postxy,postheight,postseparation,membranethickness) {
	post(postxy,postheight);
	translate([postseparation+postxy,0,0]) post(postxy,postheight);
	translate([0,postseparation+postxy,0]) post(postxy,postheight);
	translate([postseparation+postxy,postseparation+postxy,0]) post(postxy,postheight);
	translate([0,0,postheight]) cube([postseparation+2*postxy,postseparation+2*postxy,membranethickness]);
}

xsep = membrane_xseparation+(postseparation+2*postxy);
ysep = membrane_yseparation+(postseparation+2*postxy);

translate([0,0,zslab]) membrane(postxy,postheight,postseparation,membranethickness);
translate([xsep,0,zslab]) membrane(postxy,postheight,postseparation,membranethickness);
translate([2*xsep,0,zslab]) membrane(postxy,postheight,postseparation,membranethickness);

translate([0,ysep,zslab]) membrane(postxy,postheight,postseparation,membranethickness);
translate([xsep,ysep,zslab]) membrane(postxy,postheight,postseparation,membranethickness);
translate([2*xsep,ysep,zslab]) membrane(postxy,postheight,postseparation,membranethickness);

slab(xslab,yslab,zslab);

