<template>
    <main>
        <div class="mt-1">
            <form id="contact-form" method="post" action="javascript:alert('Form Submitted')" class="mx-3 border rounded-3 border-secondary bg-primary bg-gradient bg-opacity-10" novalidate>
                <h2 class="text-center m-3">Contact Us</h2>
            <div class="col-6 ms-5 mt-3">
                <label for="contactFormEmail" class="form-label">Email address:</label>
                <input type="email" class="form-control" id="contactFormEmail">
            </div>
            <div class="col-6 ms-5">
                <label for="contactFormSubject" class="form-label">Subject:</label>
                <input type="text" class="form-control" id="contactFormSubject">
            </div>
            <div class="col-6 ms-5">
                <label class="form-label" for="message">Message:</label>
                <textarea class="form-control" name="message" id="message" cols="40" rows="3" required
                minlength="1" maxlength="200"></textarea>
            </div>
            <button type="submit" class="btn btn-primary ms-5 my-3">Submit</button>
            </form>
        </div>
        <h2 id="message-sent" class="invisible">Your message has been sent. Thank You!</h2>
    </main>
</template>

<script>
  export default {
    name: 'Contact'
  }
</script>