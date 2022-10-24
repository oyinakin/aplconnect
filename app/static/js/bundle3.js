/*
Web Development Page
*/
gsap.registerPlugin(ScrollTrigger);


gsap.to(['#path210','#path208','#path206','#path202','#path204','#path200','#path198','#path196','#path194','#path192','#path188','#path190'],2,
{scale:1.8,rotate: 360,transformOrigin:'6 6',stagger:0.2,repeat:-1})
gsap.to('#g2458',1.2,{y:-30,repeat:-1})
gsap.to('#g2468',1.5,{y:40,repeat:-1})
gsap.to('#g2463',1.0,{y:-30,repeat:-1})
gsap.to('#g2438',0.7,{y:40,repeat:-1})

gsap.to('#g2493',1.2,{y:-30,repeat:-1})
gsap.to('#g2478',0.8,{y:40,repeat:-1})
gsap.to('#g2453',1.0,{y:30,repeat:-1})
gsap.to('#g2483',1.5,{y:40,repeat:-1})

gsap.to('#g2473',1.2,{x:50,repeat:-1})
gsap.to('#g2443',0.8,{x:40,repeat:-1})
gsap.to('#g2488',1.0,{x:30,repeat:-1})
gsap.to('#g2448',1.5,{x:40,repeat:-1})


gsap.fromTo('#g3737',1.2,{scale:0.5},{scale:1,repeat:-1})
gsap.fromTo('#g3757',0.8,{scale:0.5},{scale:1,repeat:-1})
gsap.fromTo('#g3834',1.5,{scale:0.5},{scale:1,repeat:-1})
gsap.fromTo('#g3729',1.8,{scale:1.5},{scale:1,repeat:-1})
gsap.from('#g3741',0.7,{rotation:720, transformOrigin:'50 50',repeat:-1})
gsap.from('#g3798',1.0,{rotation:25, transformOrigin:'0 0',repeat:-1})

gsap.from('#g3733',1.1,{rotation:720, transformOrigin:'16 16',repeat:-1})
gsap.from('#g3794',1.3,{xPercent:20,repeat:-1})
gsap.from('#g3826',0.9,{xPercent:-20,repeat:-1})
gsap.from('#g3866',1.4,{yPercent:-20,repeat:-1})
gsap.to('#path2231',0.8,{"fill":"#0925c3",repeat:-1})
gsap.to('#path2201',1.7,{"fill":"#3eef47",repeat:-1})


/**Market Research Illustration Animation**/
gsap.to(['#path2425','#path2299','#path2317','#path2263','#path2389','#path2245','#path2227','#path2461','#path2353','#path2381'
	  ,'#path2335','#path2443','#path2209','#path2361','#path2379','#path2397'
	  ,'#path2417','#path2471','#path2435','#path2453','#path2429','#path2441'
	,'#path2189','#path2465','#path2165','#path2355','#path2373','#path2391'
	,'#path2187','#path2169','#path2175','#path2181','#path2373','#path2391'	],0.5,
			{
			"fill":"random([#3eef47,#dbde24,#0eef47,#aadf47,#db4724, ##de34eb,#fcfc4c])",

    		stagger: 0.05,
			repeat:-1,

			})

gsap.from('#g6384',1.3,{height:5 +'px' ,repeat:-1})
gsap.from('#g6389',0.9,{scaleY:1.1,repeat:-1})
gsap.from('#g6394',1.4,{scaleY:0.8,repeat:-1})
gsap.to(['#g3157','#g3145','#g3037'],0.5,
			{
			opacity:0.5,
    			stagger: 0.0,
			repeat:-1,
				
			})

/**Marketing Strategy Illustration Animation**/
gsap.from(['#g2094','#g1394'],{scale:0.5,stagger: 0.5,repeat:-1})
gsap.from(['#g1430','#g1435','#g1728','#g1713','#g1723','#g1733'],{scaleY:1.3,stagger: 0.25,repeat:-1})
gsap.from(['#g1358','#g1366','#g1373'],1.3,{rotation:360 , transformOrigin:'7 8',
    		stagger: 0.015,repeat:-1})

gsap.from(['#g1746','#g1407'],1.3,{rotation:360 , transformOrigin:'8 7',
    		stagger: 0.015,repeat:-1})
gsap.to('#path932',1.7,{"fill":"#d66855",repeat:-1})
gsap.to(['#path918','#path924','#path926','#path928','#path906','#path908','#path910','#path926','#path900'
	  ,'#path896','#path1578','#path1554','#path974','#path1722','#path938'
	  ,'#path1564','#path240','#path244','#path242','#path238','#path842'
	,'#path844','#path846','#path848','#path850','#path852','#path854'
	,'#path856','#path858','#path860'	],0.5,
			{
			"fill":"random([#3eef47,#dbde24,#0eef47,#aadf47,#db4724, ##de34eb,#fcfc4c])",
    		
    		stagger: 0.015,
			repeat:-1,
				
			})

gsap.from(['#g1348','#g1327','#g825','#g820','#g830','#g835'],{
	x:"random(-100, 100)",
		y:"random(-100, 100)",stagger: 0.2,repeat:-1})



var i=0;
var j=5;

gsap.utils.toArray(".clientslide").forEach(slide =>{
j =j+1

let tl = gsap.timeline()
let panelleft = slide.querySelector(".panel1")
let panelright = slide.querySelector(".panel2")
if(panelleft != null ){
  gsap.fromTo(panelleft, 2,
      {

        x: -100
      }, {
        opacity: 1,
        x: 0,
        scrollTrigger: {
           trigger:slide,
                pin:false,
           toggleActions:"play restart play reset"
        }
    });

}
if(panelright != null){
  gsap.fromTo(panelright, 2,
      {

        x: 100
      }, {
        opacity: 1,
        x: 0,
        scrollTrigger: {
           trigger:slide,
                pin:false,
           toggleActions:"play restart play reset"
        }
    });

}


});




gsap.utils.toArray(".slide").forEach(slide =>{
i==i+1;

let panel7 = slide.querySelector(".panel7")
let panel8 = slide.querySelector(".panel8")
let panel9 = slide.querySelector(".panel9")
let paneld = slide.querySelector(".paneld")
let panele = slide.querySelector(".panele")
let panelf = slide.querySelector(".panelf")
let questionleft = slide.querySelectorAll(".question-left")
let questionright = slide.querySelectorAll(".question-right")
let questioncenter = slide.querySelectorAll(".question-center")
let gridimage = slide.querySelectorAll(".grid-image")
let gridtext = slide.querySelectorAll(".grid-panel > h5")
let fillcard = slide.querySelectorAll(".fillcard")
let flipcard = slide.querySelectorAll(".flipcard")

if(flipcard != null ){
	gsap.from([flipcard],{
                duration: 2.5,
    		opacity: 0,
    		x:"random(-100, 100)",
		    y:"random(-100, 100)",
    		stagger: 0.015,
		    scrollTrigger: {
			trigger:slide,
			pin:false, toggleActions:"play complete restart reset"
			}			
		})
	}
if(panel7 != null ){

	gsap.from([panel7,panel8,panel9], {
    		duration: 2.5,
    		opacity: 0,
    		x:"random(-100, 100)",
		    y:"random(-100, 100)",
     		stagger: 0.015,
		    scrollTrigger: {
           	trigger:slide,
            pin:false,
			toggleActions:"play complete restart reset"}
		})
	}
if(paneld != null ){
	gsap.from([paneld,panele,panelf], {
    		duration: 2.5,
    		opacity: 0,
    		x:"random(-100, 100)",
		y:"random(-100, 100)",

    		stagger: 0.015,
		scrollTrigger: {
           	trigger:slide,
           	pin:false,
			toggleActions:"play complete restart reset"}

		})
	}

if(fillcard != null ){
	gsap.from(fillcard, {
    		duration: 2.5,
    		opacity: 0,
    		x:"random(-200, 200)",
		y:"random(-200, 200)",

    		stagger: 0.015,
		scrollTrigger: {
           	trigger:slide,
           	pin:false,
           	toggleActions:"play complete restart reset"}

		})
	}
if(questionleft != null ){
	gsap.from(questionleft, {
    		duration: 2.5,
    		opacity: 0,
    		x:"random(-50, -200)",
		stagger: 0.015,
		scrollTrigger: {
           	trigger:slide,
           	pin:false,
			toggleActions:"play complete restart reset"}

		})
	}
if(questionright != null ){
	gsap.from(questionright, {
    		duration: 2.5,
    		opacity: 0,
    		x:"random(50, 200)",
		stagger: 0.015,
		scrollTrigger: {
           	trigger:slide,
           	pin:false,
           	toggleActions:"play complete restart reset"}

		})
	}
if(gridimage != null ){
	gsap.from(gridimage, {
    		duration: 2.5,
    		opacity: 0,
    		x:"random(-100, 100)",
		y:"random(-100, 100)",
		rotation:"random(-180,180)",
		stagger: 0.015,
		scrollTrigger: {
           	trigger:slide,
           	pin:false,
           	toggleActions:"play complete restart reset"}

		})
	gsap.from(gridtext, {
    		duration: 2.5,
    		opacity: 0,
    		stagger: 0.015,
		scrollTrigger: {
           	trigger:slide,
           	pin:false,
           	toggleActions:"play complete restart reset"}

		})
	}
});

$(document).ready(function(){
var footerarray= []
var footertexth1 = $(".getintouch > h1")
var footertexth3 = $(".getintouch > h3")
var footera = $(".getintouch > a")

gsap.from([footertexth1,footertexth3 , footera], {
    		duration: 2.5,
    		opacity:0,
    		x:"random(-200, 200)",
		y:"random(-200, 200)",
				stagger: 0.05,
		scrollTrigger: {
           	trigger:"footer",
           	pin:false,
           	toggleActions:"play complete restart reset"}

		})

})

var tl = new gsap.timeline({repeat:-1})
  //grow the line
tl.from(".line", 3, {width:0})
  //increase size of clipPath to reveal text
  .from(".textreveal", 5, {height:0, ease:Linear.easeNone, repeat:-1, yoyo:true}, "reveal")
  //move line down at same speed at the same time
  .to(".line", 3, {top:"104px", ease:Linear.easeNone, repeat:-1, yoyo:true}, "reveal")
  //shrink the line
  .to(".line", 2, {width:0})
$(document).ready(function(){

$('.trigger').click(function() {
    $('.token-wrapper').toggleClass('open');
     return false;
 });

 var mq = window.matchMedia( "min-width:1000px" )
 if(mq.matches){
    $('.clickable-dropdown > a').click(function(){
        location.href = this.href;
    });
 }
 else{
  $(".dropdown-toggle").attr("data-bs-toggle","dropdown")
}
});

