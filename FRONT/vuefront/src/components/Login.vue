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
import axios from 'axios'

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
                    console.log(response.data + 'this is the response data'); // Log the response data
                    const token = response.data.auth_token;
                    console.log(token + 'this is the token')
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem('token', token);
                    localStorage.setItem('username', this.username); // Store the username in the local storage
                    this.isLoggedIn = true; // Update the isLoggedIn data property
                    // this.$forceUpdate(); this did not work
                    this.$router.push('/');
                })
                .catch(error => {
                    console.error(error.response)
                    // Here you should handle the error
                })
        }
    }
}
</script>
  