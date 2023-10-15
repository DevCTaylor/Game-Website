<template>
  <div class="row">
    <button class="btn btn-success col-6 mx-auto d-grid gap-2 my-3 p-3 fs-3" @click="$emit('play-button-click')">
      Play!
    </button>
  </div>
</template>

<script>
  export default {
    name: 'PlayButton'
  }
</script>