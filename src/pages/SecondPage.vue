<template>
  <div class="secondPage-container">
    <div class="secondPage-first-container">
      <span class="animated-container-1">
        Advocacy
        <p>
          "Empowering clients through expert advocacy, we combine legal
          expertise and AI-driven insights to ensure your voice is heard and
          rights protected."
        </p>
      </span>
      <span class="animated-container-2">
        Consultation
        <p>
          "Access expert legal consultation with ease. Schedule personalized
          sessions to gain insights, answers, and solutions tailored to your
          needs."
        </p>
      </span>
      <span class="animated-container-3">
        Expertise
        <p>
          "Leverage our unparalleled expertise, combining legal proficiency and
          AI innovation, to deliver precise solutions and exceptional service
          for every challenge."
        </p>
      </span>
    </div>
    <div class="secondPage-second-container">
      Revolutionizing legal support through AI innovation and
      <span class="animated-span"> professional excellence</span>
    </div>
    <div class="secondPage-third-container">
      <div class="secondContainer-title">Representing Clients in</div>
      <div class="third-container-buttons">
        <span>Corporate Law</span>
        <span>Criminal Law</span>
        <span>Real Estate Law</span>
      </div>
    </div>
  </div>
</template>

<script>
import "../style/secondpage.css";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);
export default {
  name: "SecondPage",
  data() {
    return {};
  },
  mounted() {
    gsap.from(".animated-container-1", {
      scrollTrigger: {
        trigger: ".animated-container-1",
        start: "top 85%",
        toggleActions: "play pause resume reverse",
      },
      opacity: 0,
      duration: 0.7,
      stagger: 0.3,
      x: -100,
    });
    gsap.from(".animated-container-2", {
      scrollTrigger: {
        trigger: ".animated-container-2",
        start: "top 80%",
        toggleActions: "play pause resume reverse",
      },
      opacity: 0,
      duration: 1,
      delay: 0.4,
      x: -100,
      stagger: 0.4,
    });
    gsap.from(".animated-container-3", {
      scrollTrigger: {
        trigger: ".animated-container-3",
        start: "top 80%",
        toggleActions: "play pause resume reverse",
      },
      opacity: 0,
      duration: 1.1,
      delay: 0.6,
      x: -100,
      stagger: 0.6,
    });
    gsap.from(".secondPage-second-container", {
      scrollTrigger: {
        trigger: ".secondPage-second-container",
        start: "top 80%", // Start animation when element reaches 80% of the viewport
        toggleActions: "play pause resume reverse",
      },
      delay: 0.2,
      opacity: 0,
      x: -100,
      duration: 1,
      ease: "power3.out",
    });
    gsap.from(".animated-span", {
      scrollTrigger: {
        trigger: ".animated-span",
        start: "top 85%",
        toggleActions: "play pause resume reverse",
      },
      opacity: 0,
      x: -100,
      duration: 1,
      stagger: 0.3,
      delay: 0.4,
    });
    gsap.from('.secondContainer-title',{
        scrollTrigger:{
            trigger:'.secondContainer-title',
            start:'top 95%',
            toggleActions:"play pause resume reverse"
        },
        opacity:0,
        x:-100,
        duration:1,
        delay:0.3,
        stagger:0.3
    })
    gsap.from('.third-container-buttons span',{
        scrollTrigger:{
            trigger:'.third-container-buttons',
            start:'top 95%',
            toggleActions:"play pause resume reverse"
        },
        opacity:0,
        duration:1,
        stagger:0.3,
        delay:0.5,
        x:-100
    })
  },
};
</script>