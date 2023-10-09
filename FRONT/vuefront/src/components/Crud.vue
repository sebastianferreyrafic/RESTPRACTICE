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
        user: '',
      },
    };
  },
  methods: {
    createItem() {
      console.log(localStorage.getItem('token'));
      const userId = localStorage.getItem('userId'); // Retrieve the user ID from localStorage
      this.newItem.user = userId; // Set the user field to the user ID

      axios.post('http://localhost:8000/api/items/', this.newItem, {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
        
      })
        .then(response => {
          
          // You might want to do something with the response here
          console.log(response.data);
        })
        .catch(error => {
          console.log(error.response.data);
        });

    },
  },
};
</script>