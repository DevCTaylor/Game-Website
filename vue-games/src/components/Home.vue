<template>
    <main class="text-center">
        <section class="row pb-4" id="gamessection">
            <article class="col-sm col-md border rounded-3 shadow mx-4" id="article1">
                <h2>Math Facts</h2>
                <p>This is a simple game for practicing addition, subtraction, multiplication, and division. The equation appears with a text field below it. Enter values using the keyboard or the buttons on the screen, and solve the problems.</p>
                <button class="btn btn-success mb-2 border border-dark border-rounded"><router-link to="/games/math-facts" class="nav-link mx-3 h3">Play Now!</router-link></button>
            </article>

            <article class="col-sm col-md border rounded-3 shadow mx-4" id="article2">
                <h2>Anagram Hunt</h2>
                <p>An anagram is a word made by rearranging the letters of another word. For example, post, pots, opts, tops, and spot are all anagrams of stop. The object of the Anagram Hunt game is to find all the anagrams for a given word.</p>
                <button class="btn btn-success mb-2 border border-dark border-rounded"><router-link to="/games/anagram-hunt" class="nav-link mx-3 h3">Play Now!</router-link></button>
            </article>
        </section>
    </main>
</template>

<script>
  export default {
    name: 'Home',
  }
</script>
