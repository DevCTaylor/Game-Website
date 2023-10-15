<template>
  <div class="row mx-auto my-3">
    <label :for="id" class="col font-weight-bold text-center fs-5">{{label}}</label>
    <select class="col form-control" :id="id" :value="currentValue"
        @input="$emit('input', $event.target.value)">
      <option v-for="option in options" :key="option[1]"
        :value="option[1]">
        {{option[0]}}
      </option>
    </select>
  </div>
</template>

<script>
  export default {
    name: 'SelectInput',
    props: {
      id: String,
      label: String,
      options: Array,
      currentValue: String
    }
  }
</script>