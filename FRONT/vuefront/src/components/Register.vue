<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <label>
          Username:
          <input type="text" v-model="username" required>
        </label>
        <label>
          Email:
          <input type="email" v-model="email" required>
        </label>
        <label>
          Password:
          <input type="password" v-model="password" required>
        </label>
        <label>
          Confirm Password:
          <input type="password" v-model="password2" required>
        </label>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    
    data() {
      return {
        username: '',
        email: '',
        password: '',
        password2: ''
      }
    },
    methods: {
      register() {
        if (this.password !== this.password2) {
          alert('Passwords do not match!')
          return
        }
  
        axios.post('http://localhost:8000/auth/users/', {
          username: this.username,
          email: this.email,
          password: this.password
        })
        .then(response => {
          console.log(response.data)
          
          

          this.$router.push('/login');
        })
        .catch(error => {
          console.error(error)
          // Here you should handle the error
        })
      }
    }
  }
  </script>
  