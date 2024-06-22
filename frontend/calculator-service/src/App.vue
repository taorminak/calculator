<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink :to="`/${currentForm.toLowerCase()}`">{{ currentForm }}</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import { mapState, mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters('user', ['isLoggedIn', 'currentForm'])
  }
}
</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 20vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
  color: rgba(41, 168, 255, 1);
  font-size: 1em;
}

.logout-button {
  padding: 0 1rem;
  border: none;
  color: rgb(16, 16, 16);
  background-color: transparent;
  font-size: 1em;
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  nav {
    display: flex;
    justify-content: center;
    align-items: center;

    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
