<template>
  <HomePage/>
  <SecondPage/>
  <ThirdPage/>
  <FourthPage/>
</template>

<script>
import FourthPage from './FourthPage.vue';
import HomePage from './HomePage.vue';
import SecondPage from './SecondPage.vue';
import ThirdPage from './ThirdPage.vue';

export default {
    name:'HomeRender',
    components:{
        HomePage,
        SecondPage,
        ThirdPage,
        FourthPage
    }
}
</script>

