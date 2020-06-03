<template>
  <div id="app">
    <div>
      <Header/>
    </div>
    <!--<img alt="Geiser Limpiezas" src="./assets/geiserLogo.jpeg">-->
    <div class="text-center">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Header from "./components/Header";

export default {
  name: 'App',
  components: {
      Header
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background: #EEF1F4;
}
</style>
