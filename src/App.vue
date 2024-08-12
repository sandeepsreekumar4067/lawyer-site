<template>
  <NavBar/>
  <router-view/>
</template>

<script>
import 'bootstrap-icons/font/bootstrap-icons.css';
import '../src/style/app.css'
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
  }
}
</script>
