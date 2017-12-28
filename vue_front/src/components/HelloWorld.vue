<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Links(ここにSNSのリンクをforする)</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">Blog</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">Twitter</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>
    <h2>Other</h2>
    <ul>
      <li><router-link to="/profile">Profile</router-link></li>
      <li><router-link to="/products">Products</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'kktnhrms.com'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
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
}
</style>
