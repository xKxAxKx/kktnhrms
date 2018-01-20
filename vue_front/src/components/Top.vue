<template>
  <div class="top">
    <h2>Link</h2>
    <ul>
      <span v-for="(item, index) in snsList">
        <li>
          <a :href="item.url" target="_blank">
            {{ item.name }}
          </a>
        </li>
        <span v-if="(index+1) % 4 == 0">
          <br><br>
        </span>
      </span>
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
      axios.get(process.env.API_ENDPOINT + '/api/sns/')
           .then((res) => {
             this.snsList = res.data
           }).catch(error => {
             console.log(error)
           })
    }
  },
  created: function () {
    this.fetchLinks()

    console.log(process.env.API_ENDPOINT + '/api/product/')
  }
}
</script>
