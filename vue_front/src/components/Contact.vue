<template>
  <div class="contact">
    <h2>Contact</h2>
    <form>
      <div class="form-group">
        <label>Name</label>
        <p v-if="confirm">{{ name }}</p>
        <input v-else v-model="name" type="text" class="form-control" placeholder="Your Name">
      </div>
      <div class="form-group">
        <label>Email</label>
        <p v-if="confirm">{{ email }}</p>
        <input v-else v-model="email" type="email" class="form-control" placeholder="example@example.com">
      </div>
      <div class="form-group">
        <label>Message</label>
        <div v-if="confirm">
          {{ message }}
        </div>
        <textarea v-else v-model="message" class="form-control" rows="3" placeholder="Message"></textarea>
      </div>
      <button v-on:click="sendMessage" v-if="confirm" class="btn btn-success">
        Send Message
      </button>
      <button v-on:click="canselConfirm" v-if="confirm" class="btn btn-danger">Cansel</button>
      <button v-on:click="confirmMessage" v-else class="btn btn-success" :disabled="name.length <= 0 || email.lenght <= 0">
        Confirm
      </button>
    </form>
    <p v-if='thanksMessage'>{{ thanksMessage }}</p>
  </div>
</template>

<script>
export default {
  name: 'Contact',
  data () {
    return {
      name: '',
      email: '',
      message: '',
      confirm: false,
      thanksMessage: ''
    }
  },
  methods: {
    confirmMessage: function () {
      this.confirm = true
    },
    canselConfirm: function () {
      this.confirm = false
    },
    sendMessage: function () {
      console.log(this.name, this.email, this.message)
      this.confirm = false
      this.name = ''
      this.email = ''
      this.message = ''
      this.thanksMessage = 'Thanks for the message!'
    }
  }
}
</script>

<style scoped>

</style>
