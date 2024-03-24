import { createApp } from 'vue'
import './assets/main.css'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import { CIcon } from '@coreui/icons-vue';
import {
    cilArrowBottom,
    cilArrowRight,
    cilArrowTop,
    cilBan,
    cilBasket,
    cilBell,
    cilCalculator,
    cilCalendar,
    cilTruck,
} from '@coreui/icons'
const icons = {
    cilArrowBottom,
    cilArrowRight,
    cilArrowTop,
    cilBan,
    cilBasket,
    cilBell,
    cilCalculator,
    cilCalendar,
    cilTruck
    }

const app = createApp(App);
app.use(PrimeVue);
app.provide('icons', icons)
app.component('CIcon', CIcon)
app.mount('#app');