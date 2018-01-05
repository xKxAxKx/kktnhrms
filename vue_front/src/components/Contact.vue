<template>
  <div class="contact">
    <h2>Contact</h2>
    <form>
      <div class="form-group inquiry">
        <input type="text" class="form-control" placeholder="Your Name">
        <br>
        <input type="email" class="form-control" placeholder="Your Email">
        <br>
        <textarea class="form-control" rows="3"></textarea>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Contact',
  data () {
    return {
    }
  }
}
</script>

<style scoped>
.inquiry {
  max-width: 550px;
  display: inline-block;
  text-align: center;
}
</style>
