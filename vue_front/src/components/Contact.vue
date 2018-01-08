<template>
  <div class="contact">
    <h2>Contact</h2>
    <form>
      <div class="form-group">
        <label>Name</label>
        <p v-if="confirm">
          {{ name }}
        </p>
        <input
          v-else
          v-model="name"
          type="text"
          class="form-control"
          placeholder="Your Name">
      </div>
      <div class="form-group">
        <label>Email</label>
        <p v-if="confirm">{{ email }}</p>
        <input
          v-else
          v-model="email"
          type="email"
          class="form-control"
          placeholder="example@example.com">
        <p v-if="validationErrorEmail" style="color:#ff0000;">
          {{ validationErrorEmail }}
        </p>
      </div>
      <div class="form-group">
        <label>Message</label>
        <div v-if="confirm">
          {{ message }}
        </div>
        <textarea
          v-else
          v-model="message"
          class="form-control"
          rows="3"
          placeholder="Message"></textarea>
      </div>
      <button v-on:click="sendMessage" v-if="confirm" class="btn btn-success">
        Send Message
      </button>
      <button v-if="confirm" v-on:click="canselConfirm" class="btn btn-danger">Cansel</button>
      <button v-else v-on:click="confirmMessage" class="btn btn-success" :disabled="canNotConfirm">
        Confirm
      </button>
    </form>
    <p v-if='thanksMessage'>{{ thanksMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Contact',
  data () {
    return {
      name: '',
      email: '',
      message: '',
      confirm: false,
      thanksMessage: '',
      validationErrorEmail: ''
    }
  },
  methods: {
    confirmMessage: function () {
      this.thanksMessage = ''
      if (this.checkEmail(this.email)) {
        this.confirm = true
      } else {
        this.confirm = false
      }
    },
    canselConfirm: function () {
      this.confirm = false
    },
    sendMessage: function () {
      axios.post(
        'http://127.0.0.1:8000/api/inquiry/',
        {
          name: this.name,
          email: this.email,
          message: this.message
        }
      )
      .then((res) => {
        this.confirm = false
        this.name = ''
        this.email = ''
        this.message = ''
        this.thanksMessage = 'Thanks for the message!'
      }).catch(error => {
        this.confirm = false
        this.thanksMessage = 'Sending message failed...'
        console.log(error)
      })
    },
    checkEmail: function (email) {
      if (email.match(/.+@.+\..+/) === null) {
        this.validationErrorEmail = 'Email is incorrect'
        return false
      } else {
        this.validationErrorEmail = ''
        return true
      }
    }
  },
  computed: {
    canNotConfirm: function () {
      if (this.name.length === 0 || this.email.length === 0) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style scoped>

</style>
