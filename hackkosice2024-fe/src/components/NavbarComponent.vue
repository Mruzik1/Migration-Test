<template>
  <nav class="bg-pink-600 text-white p-4">
    <div class="container mx-auto flex justify-between items-center">
      <a class="text-xl font-semibold flex flex-row items-center gap-4" href="/">
        <img style="width: 35px" src="https://www.telekom.com/resource/blob/1002354/12f9f204ed4293439e1c93f7851ae186/dl-telekom-logo-01-data.jpg" />
        <span class="text-white-100">Deutsche Telekom IT Solutions</span>
      </a>
      <div>
        <a class="px-4 py-2 hover:bg-pink-700 rounded" href="/about">About</a>
        <a class="px-4 py-2 hover:bg-pink-700 rounded" href="/services">Services</a>
        <a class="px-4 py-2 hover:bg-pink-700 rounded" href="/contact">Contact</a>
        <a class="px-4 py-2 hover:bg-pink-700 rounded" href="/contact">Login</a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
};
</script>

<style scoped></style>
