<script setup lang="ts">
import 'primeicons/primeicons.css'
import logoUrl from '../logo.png'
import Fieldset from 'primevue/fieldset';
import Dropdown from 'primevue/dropdown';
import * as icon from '@coreui/icons';
import { onMounted, ref } from "vue";
import axios from 'axios';
const date = ref();
onMounted(() => {
  axios.get('http://localhost:3000/destinies')
    .then(response => console.log(response))
})
const selectedCity = ref();
const cities = ref([
    { name: 'New York'},
    { name: 'Rome'},
    { name: 'London'},
    { name: 'Istanbul'},
    { name: 'Paris'}
]);


  function span(){
    if(selectedCity.value != undefined){
      console.log(selectedCity.value.name)
    }
    else{
      alert('Você deve escolher um destino')
    }
  }

</script>

<template>
<div class="flex">
  <div style="height: 100svh" class="bg-gray-800 w-1/4 text-white" >
    <img :src="logoUrl" class="pt-10 pl-6 pr-5 h-fit w-8/12"  />
    <Fieldset class="my-20 ml-7">
      <CIcon :icon="icon.cilCalculator" class="w-6 inline-grid" />
      <p class="inline-grid text-xl ml-2 pt-2 font-semibold">Calculadora de Viagem</p>
    </Fieldset>
  </div>
  <div class="w-3/4 items-center">
    <Fieldset class="my-20 ml-12 mr-24 text-white bg-gray-800 p-5 rounded-t-lg">
      <CIcon :icon="icon.cilTruck" class="w-6 inline-grid" />
      <p class="inline-grid text-xl ml-2 font-bold">Calculadora de Viagem</p>
    </Fieldset>
    <div class="ml-12 mr-24 text-black bg-slate-200 p-5 w-1/3 h-8/12">
        <Fieldset class=" text-gray-800 pt-12 rounded-t-lg">
          <CIcon :icon="icon.cilHandPointRight" class="w-6 inline-grid" />
          <p class="inline-grid text-xl ml-2 font-semibold">Calcule o valor da viagem</p>
        </Fieldset>
        <p class="inline-grid ml-2 mt-10 font-semibold text-sm mb-4">Destino</p>
        <Dropdown v-model="selectedCity" :options="cities" optionLabel="name" placeholder="Selecione o destino" class="bg-white flex pl-8 pr-11 py-2 justify-between rounded-md border-black" />
        <div class="center">
          <p class="ml-2 mt-10 font-semibold text-sm mb-4">Data</p>
          <Calendar v-model="date" class="bg-white flex pl-8 pr-11 py-2 justify-between rounded-md border-black" />
        </div>
          <div class="justify-items-center content-center items-center flex">
            <Button v-on:click="span()" label="Buscar" class="bg-teal-600 flex my-10  pl-8 pr-11 py-2 justify-items-center content-center items-center  rounded-md border-black"/>
          </div>
      </div>
  </div>
</div>
</template>

<style scoped>

</style>
