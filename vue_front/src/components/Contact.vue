<template>
  <div class="contact">
    <h2>Contact</h2>
    <form>
      <div class="form-group">
        <label>Name</label>
        <input type="text" class="form-control" placeholder="Your Name">
      </div>
      <div class="form-group">
        <label>Email</label>
        <input type="email" class="form-control" placeholder="example@example.com">
      </div>
      <div class="form-group">
        <label>Message</label>
        <textarea class="form-control" rows="3"></textarea>
      </div>
      <button type="submit" class="btn btn-success">Submit</button>
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

</style>
