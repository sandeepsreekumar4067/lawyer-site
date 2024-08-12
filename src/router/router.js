import {  createRouter, createWebHistory } from "vue-router";
import BotselectionPage from "@/pages/BotselectionPage.vue";
import HomeRender from "@/pages/HomeRender.vue";


const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeRender,
    },
    {
        path:'/selection-page',
        name:'selection',
        component:BotselectionPage
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes,
  });
export default router