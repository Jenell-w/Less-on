<template>
  <div id="app">
    <h1>Welcome to Create Your Own Lesson</h1>
    <h3>
      Where you can simply create your child a quick, fun, mini quiz for your
      child while you are waiting, or are out or your child complains there is
      <i>nothing to do</i>. Happy Creating!
    </h3>

    <div>
      <button @click="showCreateAssignment = !showCreateAssignment">
        {{ buttonTextCreate }}
      </button>
      <CreateAssignment v-model="CreateAssignment"> </CreateAssignment>
    </div>
  </div>
</template>

<script>
import CreateAssignment from "./components/CreateAssignment.vue";

export default {
  name: "app",
  components: {},
  data() {
    return {
      showTodoList: false,
      buttonTextCreate: "Create New Assignment",
      CreateAssignment: false,
    };
  },
  methods: {
    handleNavClick() {
      this.CreateAssignment = true;
    },
  },
};
</script>

<style></style>
