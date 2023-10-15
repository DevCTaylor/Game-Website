<template>
  <div id="body">
    <div>
        <div class="row">
            <h4 class="text-dark">Remaining: {{anagramsLeft}}</h4>
          <div class="row mt-1">
            <h2 class="text-dark">Guessed: {{anagramsGuessed.toString()}}</h2>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Anagrams',
    props: {
        anagramsGuessed: Array,
        anagramsLeft: Number 
    }
  }
</script>
