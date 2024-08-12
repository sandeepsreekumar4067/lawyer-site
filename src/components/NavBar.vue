<template>
  <div class="navbar-container">
    <div class="icon-container">
        <img :src="logoIcon" alt="">
    </div>
    <div class="navbar-components">
        <span class="navbar-component" @click="()=>{this.$router.push('/')}">Home</span>
        <span class="navbar-component">About</span>
        <span class="navbar-component">practice area</span>
        <span class="navbar-component">Case Result</span>
        <span class="navbar-component">packages</span>
        <span class="navbar-component">Blog</span>
    </div>
    <div class="consulation-container" @click="()=>{this.$router.push('/selection-page')}">
        <span>Get Consulation</span>
    </div>
  </div>
</template>

<script>
import '../style/navbar.css'
import logoIcon from '../assets/logoicon.svg'
import {gsap} from 'gsap'
export default {
    name:'NavBar',
    data(){
        return{
            logoIcon:logoIcon
        }
    },
    mounted(){
        gsap.from('.navbar-component',{
            opacity:0,
            duration:1,
            ease:'expo.inOut',
            x:0,
            stagger:{amount:1,from:'center'}
        })
    }
}
</script>

<style>

</style>