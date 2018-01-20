<template>
  <div class="profile">
    <h2>Profile</h2>
    <div class="detail">
      <span v-html="profile"></span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Profile',
  data () {
    return {
      profile: ''
    }
  },
  methods: {
    fetchProfile: function () {
      axios.get(process.env.API_ENDPOINT + '/api/about/')
           .then((res) => {
             this.profile = res.data.detail
           }).catch(error => {
             console.log(error)
           })
    }
  },
  created: function () {
    this.fetchProfile()
  }
}
</script>

<style scoped>
/* .detail {
  max-width: 550px;
  display: inline-block;
  text-align: left;
} */
</style>
