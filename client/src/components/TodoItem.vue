<template>
  <div class="todo-item-container">
    <li @click="toggleTodo" v-bind:class="{ 'done-todo': todo.done }">{{todo.item}}</li>
    <button @click="deleteTodo">X</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Assignment",
  props: ["todo", "getAllTodos"],

  methods: {
    toggleTodo() {
      axios.patch("/todo", { id: this.todo.id }).then(() => this.getAllTodos());
    },
  },
};
</script>

<style>
</style>