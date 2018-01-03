<template>
  <div class="profile">
    <h2>Profile</h2>
    <div class="detail">
      <span v-html="profile.detail"></span>
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
    fetchProfile: function() {
      axios.get('http://127.0.0.1:8000/api/about/')
           .then((res) => {
             console.log(res.data)
             this.profile = res.data
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
.detail {
  display: inline-block;
  text-align: left;
}
</style>
