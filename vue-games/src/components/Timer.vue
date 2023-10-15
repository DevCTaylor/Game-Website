<template>
  <strong>{{timeLeft}}</strong>
</template>

<script>
  export default {
    name: 'Timer',
    props: {
      timeLeft: Number
    }
  }
</script>