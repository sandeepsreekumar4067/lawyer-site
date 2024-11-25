<template>
  <div class="fourthpage-container" id="pin-container">
    <div class="circle-container" id="pin-circle">
        <span :class="['title title1',{active:containerActive}]"></span>
        <span :class="['title title2',{active:containerActive}]"></span>
        <span :class="['title title3',{active:containerActive}]"></span>
        <span :class="['title title4',{active:containerActive}]"></span>
        <div class="inside-circle" @click="()=>{this.containerActive=!this.containerActive}"></div>
    </div>
  </div>
</template>

<script>
import "../style/Fourthpage.css";
import { gsap } from "gsap";

export default {
  name: "FourthPage",
  data() {
    return {
      containerActive: false,
    };
  },
  mounted() {
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: "#pin-circle",
        scrub: 1,
        start: "top 40%", // Start the animation when the top of the container hits 20% of the viewport height
        endTrigger: "#pin-container",
        end: "bottom bottom", // End the animation when the bottom of the container hits 80% of the viewport height
        markers: false, // Optional: Add markers to visualize the start and end points (remove in production)
        pin: true, // Pin the container during the scroll
        },
    });

    tl.to("#pin-circle", {
      xPercent: 260, // Move the circle to the right edge of the screen
      ease: "none", // Linear easing for consistent motion
      rotate: 240,
      borderRadius:'50%'
    });
    tl.to('.title',{
      opacity:1
    })
  },
};
</script>
    