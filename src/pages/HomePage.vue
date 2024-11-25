<template>
  <div class="homePage-container">
    <div class="homePage-title-container">
      <div class="homePage-title">
        <span class="title">Providing top-tier</span>
        <span id="greyTitle" class="title">legal services.</span>
        <span id="subtitle" >
          Bravery courage fear and love in times of war
        </span>
        <div class="contact-container">
          <span class="contact-info">
            <i class="bi bi-telephone-fill"></i>
            <p>Call us : 0123456789</p>
          </span>
          <span class="contact-info">
            <i class="bi bi-envelope-fill"></i>
            <p>email : someone@gmail.com</p>
          </span>
        </div>
      </div>
    </div>
    <div class="homepage-image-container">
      <img :src="homeImage" alt="Portrait of Digital Nomads" />
    </div>
  </div>

</template>

<script>
import "../style/homepage.css";
import homeImage from "../assets/lawyer3.jpeg";
import {gsap} from "gsap"
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger)
export default {

  name: "HomePage",
  data() {
    return {
      homeImage: homeImage,
    };
  },
  mounted() {
    gsap.from('.title',{
      opacity:0,
      duration:1,
      stagger:0.3,
      y:50,
      ease:'power3.inOut',
    })
    gsap.from('#subtitle',{
      delay:0.4,
      duration:1,
      opacity:0,
      y:50,
      ease:'power3.inOut'
    })
    gsap.from('.contact-info',{
      y:50,
      stagger:0.3,
      duration:1,
      ease:'power3.inOut',
      opacity:0,
      delay:0.6
    })
    gsap.from('.homepage-image-container img',{
      duration:1.5,
      delay:0.5,
      opacity:0,
      x:100,
      ease:'power3.inOut'
    })
    gsap.to('.homePage-title',{
      scrollTrigger:{
        trigger:'homePage-title',
        start:'top 40%',
        end:'bottom 98%',
        toggleActions:'play none none none',
        scrub:1,
      },
      xPercent:-100,
      opacity:0,
      duration:1,
      ease:'power3.inOut'
    })
    gsap.to('.homepage-image-container',{
      scrollTrigger:{
        trigger:'.homePage-title',
        start:'top 40%',
        toggleActions:'play none none none',
        scrub:1
      },
      xPercent:100,
      opacity:0,
      duration:1,
      ease:'power3.inOut'
    })
  }
};
</script>

