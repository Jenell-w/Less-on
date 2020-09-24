<template>
  <div id="app">
    <div>
      <button @click="handleNavClick">{{ buttonText }}</button>
    </div>
  </div>
</template>

<script>
//import TodoList from './components/TodoList.vue';

export default {
  name: "app",
  components: {},
  data() {
    return {
      showTodoList: false,
      buttonText: "Show Todo List",
    };
  },
  methods: {
    handleNavClick() {
      this.showTodoList = !this.showTodoList;
      if (this.buttonText === "Show Todo List") {
        this.buttonText = "Show Welcome Screen";
      } else {
        this.buttonText = "Show Todo List";
      }
    },
  },
};
</script>

<style>
</style>
