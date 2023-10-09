<template>
    <div>
        <h2>Login</h2>
        <form @submit.prevent="login">
            <label>
                Username:
                <input type="text" v-model="username" required>
            </label>
            <label>
                Password:
                <input type="password" v-model="password" required>
            </label>
            <button type="submit">Login</button>
        </form>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      axios.defaults.headers.common["Authorization"] = ""
      const formData = {
        username: this.username,
        password: this.password
      }

      axios.post('http://localhost:8000/auth/token/login/', formData)
        .then(response => {
          const token = response.data.auth_token;
          axios.defaults.headers.common["Authorization"] = "Token " + token
          localStorage.setItem('token', token);
          localStorage.setItem('username', this.username);

          // Store the user ID in localStorage
          axios.get('http://localhost:8000/auth/users/me/', {
            headers: {
              'Authorization': `Token ${token}`
            }
          })
            .then(response => {
              const userId = response.data.id;
              localStorage.setItem('userId', userId);
              this.$router.push('/');
            })
            .catch(error => {
              console.error(error.response);
            });
        })
        .catch(error => {
          console.error(error.response);
        });
    }
  }
}

</script>
  