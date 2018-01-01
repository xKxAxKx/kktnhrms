<template>
  <div class="top">
    <h2>Link</h2>
    <ul>
      <li v-for="item in snsList">
        <a :href="item.url" target="_blank">
          {{ item.name }}
        </a>
      </li>
    </ul>
    <h2>Other</h2>
    <ul>
      <li><router-link to="/profile">Profile</router-link></li>
      <li><router-link to="/products">Products</router-link></li>
      <li><router-link to="/contact">Contact</router-link></li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Top',
  data () {
    return {
      snsList: []
    }
  },
  methods: {
    fetchLinks: function () {
      axios.get('http://127.0.0.1:8000/api/sns/')
           .then((res) => {
             this.snsList = res.data
           }).catch(error => {
             console.log(error)
           })
    }
  },
  created: function () {
    this.fetchLinks()
  }
}
</script>
