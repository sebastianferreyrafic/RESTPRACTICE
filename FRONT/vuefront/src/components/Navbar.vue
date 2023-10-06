<template>
  <nav>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/crud">Crud</router-link></li>
      <li v-if="!isLoggedIn"><router-link to="/login">Login</router-link></li>
      <li v-if="!isLoggedIn"><router-link to="/register">Sign Up</router-link></li>
      <li v-if="isLoggedIn"><button @click="logout">Logout</button></li>
    </ul>
    <div>
      <p v-if="isLoggedIn">Logged in as: {{ username }}</p>
      <p v-else>Not logged in</p>
    </div>
  </nav>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      isLoggedIn: !!localStorage.getItem('token'),
      username: localStorage.getItem('username') || ''
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      this.isLoggedIn = false;
      this.username = '';
      axios.defaults.headers.common["Authorization"] = "";
      this.$router.push('/login');
    }
  }
}
</script>

  
<style scoped>
nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 10px;
}
</style>
  