<template>
  <div id="equation" class="row display-3">
    <div class="col-8">{{question}}</div>
    <div class="col-4 text-start">{{answer}}</div>
  </div>
</template>

<script>
  export default {
    name: 'Equation',
    props: {
      question: String,
      answer: String,
      answered: Boolean
    }
  }
</script>
