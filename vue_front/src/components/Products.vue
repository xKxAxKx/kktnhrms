<template>
  <div class="products">
    <h2>Products</h2>
    <div v-for="item in products" class="items">
      <a :href="item.url" target="_blank">
        {{ item.name }}
      </a>
      <div v-html="item.detail"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Products',
  data () {
    return {
      products: []
    }
  },
  methods: {
    fetchProducts: function () {
      axios.get('http://127.0.0.1:8000/api/product/')
           .then((res) => {
             this.products = res.data
           }).catch(error => {
             console.log(error)
           })
    }
  },
  created: function () {
    this.fetchProducts()
  }
}
</script>

<style scoped>
/* .items {
  max-width: 550px;
  margin-bottom: 30px;
} */
</style>
