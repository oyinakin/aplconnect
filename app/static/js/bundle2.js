gsap.registerPlugin(ScrollTrigger)
let revealContainers = document.querySelectorAll(".firstpanel");
revealContainers.forEach((container) => {
let image = container.querySelector("div");

  let tl = gsap.timeline({
    scrollTrigger: {
      trigger: container,
      toggleActions: "play none none reset"
    }
  });

  tl.set(container, { autoAlpha: 1 });
  tl.from(container, 1.5, {
    xPercent: -100,
	ease: Power2.out
  });
  tl.from(image, 1.5, {
    xPercent: 100,
    scale: 1.5,
    delay: -1.5,
    ease: Power2.out
  });
	tl.to(container, 1.5, {
    yPercent: 10,
	scale: 1,
    delay: 2,

  });

});


$(document).ready(function(){



document.querySelectorAll(".fourthpanel").forEach((elem) => {
   tl = gsap.timeline({
      scrollTrigger: {
      trigger: elem,
      toggleActions: "play none none reset"
    }
  });
  tl.fromTo(".fourthpaneldiv1",2, {x: 100,  autoAlpha: 0}, {
    x: 0,
    autoAlpha: 1,
    ease: "back",
    overwrite: "auto", delay:2
  });
  tl.fromTo(".fourthpaneldiv2",2, {x: -100,  autoAlpha: 0}, {

    x: 0,
    autoAlpha: 1,
    ease: "back",
    overwrite: "auto", delay:2
  });
 });



let panels = document.querySelectorAll("section");
panels.forEach((panel) => {


let leftelements = panel.querySelectorAll(".fadeInLeft");

leftelements.forEach((elem) => {

	let scrollTriggerTimeline = gsap.timeline({
		scrollTrigger: {
			trigger : panel,
			pin:false,
			toggleActions:"play restart play reset"

		},
		defaults:{}
	});
    scrollTriggerTimeline.from(elem,2,{
		xPercent:-100, opacity:0
	})
    scrollTriggerTimeline.to(elem,2,{
		xPercent:0, opacity:1
	})

	 })

let righttelements = panel.querySelectorAll(".fadeInRight");


righttelements.forEach((elem) => {
const tl = gsap.timeline();
const endVals = [5000,500,11];
const wrapIndex = gsap.utils.wrap(0, endVals.length);

const elems = elem.querySelectorAll('.counter');
const curVals = [];
// Get the initial values

let scrollTriggerTimeline = gsap.timeline({
		scrollTrigger: {
			trigger : panel,
			pin:false,
		       	toggleActions:"play restart play reset"
		},
		
	});
    scrollTriggerTimeline.from(elem,2,{
		xPercent:100, opacity:0
	})
    scrollTriggerTimeline.to(elem,2,{
		xPercent:0, opacity:1,
	})
 if(elems){
      elems.forEach(elem => curVals.push({val: parseInt(elem.innerText)}));

       }
scrollTriggerTimeline.to(curVals, 2,{
  val: i => endVals[wrapIndex(i)],
  snap: {val: 1},
  onUpdate: function() {
    this.targets().forEach((target, i) => elems[i].innerText = target.val);
  }
},-0.4);
})


let fadeupelements = panel.querySelectorAll(".fadeInUp");
fadeupelements.forEach((elem) => {
const tl = gsap.timeline();
const endVals = [11,500];
const wrapIndex = gsap.utils.wrap(0, endVals.length);
const elems = elem.querySelectorAll('.counter');
const curVals = [];

const endVals2 = [5000];
const wrapIndex2 = gsap.utils.wrap(0, endVals2.length);
const elems2 = elem.querySelectorAll('.counter-2');
const curVals2 = [];

// Get the initial values
let scrollTriggerTimeline = gsap.timeline({
		scrollTrigger: {
			trigger : panel,
			pin:false,
		       	toggleActions:"play restart play reset"
		},
		
	});
    scrollTriggerTimeline.from(elem,2,{
		yPercent:100, opacity:0
	})
    scrollTriggerTimeline.to(elem,2,{
		yPercent:0, opacity:1,
	})
if(elems){
      elems.forEach(elem => curVals.push({val: parseInt(elem.innerText)}));
       }
scrollTriggerTimeline.to(curVals, 2,{
  val: i => endVals[wrapIndex(i)],
  snap: {val: 1},
  onUpdate: function() {
    this.targets().forEach((target, i) => elems[i].innerText = target.val);
  }
},-0.4);

if(elems2){
      elems2.forEach(elem => curVals2.push({val: parseInt(elem.innerText)}));
       }
scrollTriggerTimeline.to(curVals2, 2,{
  val: i => endVals2[wrapIndex2(i)],
  snap: {val: 1},
  onUpdate: function() {
    this.targets().forEach((target, i) => elems2[i].innerText = target.val);
  }
},-0.4);
let parll1 = panel.querySelectorAll(".parallax1inner");
let parll3 = panel.querySelectorAll(".parallax3inner");
let parll2 = panel.querySelectorAll(".parallax2inner");
let parll4 = panel.querySelectorAll(".parallax4inner");
let parll5 = panel.querySelectorAll(".parallax5inner");

if(parll1 != null ){
	gsap.from([parll1,parll2,parll3,parll4,parll5], {
    		duration: 2.5,
    		opacity: 0,
    		x:"random(-500, 500)",
		y:"random(-500, 500)",
                rotation:"random(-360, 360)",
    		stagger: 0.015,
		scrollTrigger: {
           	trigger:panel,
           	pin:false,
           	toggleActions:"play complete restart reset"}

		})
	}

/***
let panel2 = document.querySelectorAll(".sectionpanel.panel2");
panel2.forEach((elem) => {
	let scrollTriggerTimeline = gsap.timeline({
		scrollTrigger: {
			trigger : panel2,
			pin:false,
		        toggleActions:"play reset play reset",
		},
		
	});
        scrollTriggerTimeline.from(elem,3,{xPercent:100, opacity:0.5})

	scrollTriggerTimeline.to(elem,3,{xPercent:0, opacity:1})
	 })
****/

let pathright = panel.querySelectorAll(".pathRight");
pathright.forEach((elem) => {
	let scrollTriggerTimeline = gsap.timeline({
		scrollTrigger: {
			trigger : panel,
			pin:false,
			scrub:1,
			start:"top",
			toggleActions:"play restart play reset"

		},
		defaults:{stagger:0.5}
	});
    scrollTriggerTimeline.from(elem,2,{
		xPercent:75,
		yPercent:25, scale:0.5
	})

	scrollTriggerTimeline.to(elem,2,{
		xPercent:0,
		yPercent:0, scale:1
	})
	 })

	let pathcenter = panel.querySelectorAll(".fadeInCenter");
pathcenter.forEach((elem) => {
	let scrollTriggerTimeline = gsap.timeline({
		scrollTrigger: {
			trigger : panel,
			pin:true,
			scrub:5,
			end: ()=> elem.parentNode.offsetLeft +
                elem.parentNode.getBoundingClientRect().width/2,

			toggleActions:"play restart play reset"

		},
		defaults:{stagger:0.5}
	});
    scrollTriggerTimeline.from(elem,5,{
		 scale:0.1
	})

   scrollTriggerTimeline.to(elem,5,{
		scale:0.3
	})
	 })

let fillcard = panel.querySelectorAll(".fillcard");
if(fillcard != null ){
	gsap.from(fillcard, {
    		duration: 2.5,
    		opacity: 0,
    		x:"random(-200, 200)",
		y:"random(-200, 200)",

    		stagger: 0.015,
		scrollTrigger: {
           	trigger:panel,
           	pin:false,
           	toggleActions:"play complete restart reset"}

		})
	}

let panel5 = panel.querySelector(".panel5animate1");
if (panel5){
let scrollTriggerTimeline = gsap.timeline({

		scrollTrigger: {
			trigger : panel,
			pin:false,
      			toggleActions:"play restart play reset"

		}

	});
    scrollTriggerTimeline.from([".panel5animate1",".panel5animate2",".panel5animate3", ".panel5animate4", ".panel5animate5",
				".panel5animate6", ".panel5animate7",".panel5animate8",".panel5animate9"],2,{
		yPercent:"random(300,-300)",
		opacity:0,
		stagger:0.05
	})
}	

	

});



});
});
/**
const counters = document.querySelectorAll('.counter');
if(counters){
const speed = 1000; // The lower the slower
counters.forEach(counter => {
	const updateCount = () => {
		const target = +counter.getAttribute('data-target');
		const count = +counter.innerText;

		// Lower inc to slow and higher to slow
		const inc = target / speed;

		// console.log(inc);
		// console.log(count);

		// Check if target is reached
		if (count < target) {
			// Add inc to count and output in counter
			counter.innerText = count + inc;
			// Call function every ms
			setTimeout(updateCount, 1);
		} else {
			counter.innerText = target;
		}
	};

	updateCount();
});

}
**/
/**
Web Development Page


gsap.fromTo([".panel1", ".panel2", ".panel3"],
      {
        opacity: 0,
        y: -50
      }, {
        duration: 1,
        opacity: 1,
        y: 0,
        stagger: {
          each: .6
        },
        scrollTrigger: {
          start: 1500,
        }
    });

**/
