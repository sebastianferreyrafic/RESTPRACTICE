<template>
    <form @submit.prevent="createItem">
      <input v-model="newItem.name" placeholder="Name">
      <input v-model="newItem.description" placeholder="Description">
      <button type="submit">Create</button>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'CreateItem',
    data() {
      return {
        newItem: {
          name: '',
          description: '',
        },
      };
    },
    methods: {
      createItem() {
        axios.post('http://localhost:8000/api/items/', this.newItem)
          .then(response => {
            // You might want to do something with the response here
            console.log(response.data);
          })
          .catch(error => {
            console.log(error);
          });
        
      },
    },
  };
  </script>