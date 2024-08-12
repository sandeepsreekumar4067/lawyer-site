<template>
  <div class="thirdPage-container">
    <div class="thirdPage-title">
      Law Definitions
    </div>
    <div class="case-card-container">
      <div class="card c1" @mouseenter="rotateCard($event)" @mouseleave="reverseRotateCard($event)">
        <div class="case-cards">
          <img :src="corporate" alt="Corporate Law" class="card-image" />
          <div class="case-content">
            <div class="case-title">Corporate Law</div>
            <div class="case-image">
              <img :src="corporateIcon" alt="" />
            </div>
            <div class="case-description">
              " Corporate law oversees the formation, operation, and regulation
              of businesses, focusing on compliance, governance, and protecting
              stakeholder interests. "
            </div>
          </div>
        </div>
      </div>
      <div class="card c2" @mouseenter="rotateCard($event)" @mouseleave="reverseRotateCard($event)">
        <div class="case-cards">
          <img :src="criminal" alt="Corporate Law" class="card-image" />
          <div class="case-content">
            <div class="case-title">Criminal Law</div>
            <div class="case-image">
              <img :src="CriminalIcon" alt="" />
            </div>
            <div class="case-description">
              " Criminal law governs offenses against the state, focusing on
              prosecution, defense, and upholding justice for all involved. "
            </div>
          </div>
        </div>
      </div>
      <div class="card c3" @mouseenter="rotateCard($event)" @mouseleave="reverseRotateCard($event)">
        <div class="case-cards">
          <img :src="realEstate" alt="Corporate Law" class="card-image" />
          <div class="case-content">
            <div class="case-title">Real Estate Law</div>
            <div class="case-image">
              <img :src="realEstateIcon" alt="" />
            </div>
            <div class="case-description">
              " Real estate law governs property transactions, covering buying,
              selling, and leasing while ensuring legal rights and compliance. "
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="booking-button" @click="()=>{this.$router.push('/selection-page')}">
    book now
  </div>
  </div>
</template>

<script>
import "../style/thirdpage.css";
import corporate from "../assets/corporateLaw2.jpeg";
import criminal from "../assets/criminalLaw.jpg";
import realEstate from "../assets/realEstate.jpg";
import corporateIcon from "../assets/corporateIcon.png";
import CriminalIcon from "../assets/criminalLawIcon.png";
import realEstateIcon from '../assets/realEstateIcon.png'
import { gsap } from "gsap";
export default {
  data() {
    return {
      corporate: corporate,
      criminal: criminal,
      realEstate: realEstate,
      corporateIcon: corporateIcon,
      CriminalIcon: CriminalIcon,
      realEstateIcon:realEstateIcon
    };
  },
  methods: {
    rotateCard(event) {
      const target = event.currentTarget;
      const card = target.querySelector(".case-cards");
      const image = target.querySelector(".card-image");
      const title = target.querySelector(".case-content");
      gsap.to(image, { display: "none", duration: 0.8 });
      gsap.to(card, {
        rotateY: 360,
        duration: 1.5,
        ease: "power3.inOut",
      });
      gsap.to(title, { opacity: 1, duration: 0.7 });
    },
    reverseRotateCard(event) {
      const target = event.currentTarget;
      const card = target.querySelector(".case-cards");
      const image = target.querySelector(".card-image");
      const title = target.querySelector(".case-content");
      gsap.to(title, { opacity: 0, delay:0.6, duration:0.6});
      gsap.to(card, {
        rotateY: 0,
        duration: 1.5,
        ease: "power3.inOut",
      });
      gsap.to(image, { display: "flex", delay: 0.7 });
    },
  },
  mounted(){
    gsap.from('.thirdPage-title',{
      scrollTrigger:{
        trigger:'.thirdPage-title',
        start:'top 80%',
        end:'top 30%',
        toggleActions:'play none none none',
        scrub:1
      },
      letterSpacing:0,
      duration:0.8,
      opacity:0,
      ease:'power3.inOut'
    })
    // Animate .c1 container out of the viewport on scroll upwards and reverse it on scroll downwards
    gsap.from('.c1',{
      scrollTrigger:{
        trigger:'.c1',
        scrub:1,
        toggleActions:'play none none none',
        start:'top 90%',
        end:'top 40%'
      },
      xPercent:-100,
      opacity:0,
    })
    gsap.from('.c2',{
      scrollTrigger:{
        trigger:'.thirdPage-title',
        start:'top 90%',
        end:'top 10%',
        toggleActions:'play none none none',
        scrub:1
      },
      borderRadius:'50%',
      scale:0
    })
    gsap.from('.c3',{
      scrollTrigger:{
        trigger:'.c3',
        scrub:1,
        toggleActions:'play none none none',
        start:'top 90%',
        end:'top 40%'
      },
      xPercent:100,
      opacity:0
    })
   gsap.from('.booking-button',{
    scrollTrigger:{
      trigger:'.card',
      scrub:1,
      toggleActions:'play none none none',
      start:'top 30%',
      end:'bottom 70%'
    },
    yPercent:100,
    opacity:0.4
   })
  }
};
</script>
