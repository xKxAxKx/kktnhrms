<template>
  <div id="app" class="row">
    <h1><router-link class="top-link" to="/">kktnhrms.com</router-link></h1>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 900px;
  margin: auto;
}
h1, h2, h3 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
  text-decoration: none;
}
.top-link:link {
  color: #2c3e50;
  text-decoration: none;
}
.top-link:hover {
  color: #2c3e50;
  text-decoration: none;
}
.top-link:visited {
  color: #2c3e50;
  text-decoration: none;
}
.top-link:active {
  color: #2c3e50;
  text-decoration: none;
}
</style>
