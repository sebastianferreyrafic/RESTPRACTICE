<template>
    
    <div>
        <h1>API TEST</h1>
    <div v-for="item in items" :key="item.id">
      <h2>{{ item.name }}</h2>
      <p>{{ item.description }}</p>
      <p>Created by: {{ item.user }}</p>
      <button @click="deleteItem(item.id)">Delete</button>
    </div>
  </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
  name: 'Home',
  data() {
    return {
      items: [],
    };
  },
  created() {
    this.fetchItems();
  },
  methods: {
    fetchItems() {
  axios.get('http://localhost:8000/api/items/', {
    headers: {
      'Authorization': `Token ${localStorage.getItem('token')}`
    }
  })
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    deleteItem(itemId) {
      axios.delete(`http://localhost:8000/api/items/${itemId}`)
        .then(response => {
          console.log(response.data);
          // Remove the deleted item from the items array
          this.items = this.items.filter(item => item.id !== itemId);
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
};
</script>