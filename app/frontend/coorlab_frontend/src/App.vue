<script setup lang="ts">
import 'primeicons/primeicons.css'
import logoUrl from '../logo.png'
import Fieldset from 'primevue/fieldset';
import * as icon from '@coreui/icons';
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
  </div>
</div>
</template>

<style scoped>

</style>
