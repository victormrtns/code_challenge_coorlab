import { createApp } from 'vue'
import './assets/main.css'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import Calendar from 'primevue/calendar';
import Button from 'primevue/button';
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
    cilHandPointRight
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
    cilTruck,
    cilHandPointRight
    }

const app = createApp(App);
app.use(PrimeVue);
app.provide('icons', icons)
app.component('CIcon', CIcon)
app.component('Calendar', Calendar);
app.component('Button', Button);
app.mount('#app');