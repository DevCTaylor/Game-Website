<template>
  <div class="row">
    <button class="btn btn-success col-3 mx-auto d-grid gap-2 my-3 p-3 fs-5" @click="$emit('is-anagram')">
      Enter
    </button>
  </div>
</template>

<script>
  export default {
    name: 'InputButton'
  }
</script>