export default [
  {
    filename: "hello_world.vue",
    lang: "html",
    code: `
<template>
  <h1>{{ message }}</h1>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('Hello World!')
</script>
    `,
  },
  {
    filename: "/hackkosice2024-fe/public/index.html",
    lang: "html",
    code: `
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="/favicon.ico" type="image/x-icon" />
    <title>IT Telekom Code Refactor</title>
</head>
<body>
    <div id="app"><!-- Vue.js application will be mounted here --></div>
    <div id="no-js">Users without JavaScript enabled</div>
</body>
</html>
    `,
  },
  {
    filename: "App.vue",
    lang: "js",
    code: `
import { defineComponent } from 'vue';
// Import other necessary components here
import NavbarComponent from './components/NavbarComponent.vue';
import InputText from './components/InputText.vue';
import Button from './components/Button.vue';
import VCodeBlock from './components/VCodeBlock.vue';
import Dropdown from './components/Dropdown.vue';
import Textarea from './components/Textarea.vue';
import Message from './components/Message.vue';
import TabView from './components/TabView.vue';
import TabPanel from './components/TabPanel.vue';
// Import PrimeVue components here
import 'primevue/resources/themes/nova-light/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

export default defineComponent({
  name: 'App',
  components: {
    NavbarComponent,
    InputText,
    Button,
    VCodeBlock,
    Dropdown,
    Textarea,
    Message,
    TabView,
    TabPanel,
    // Add other necessary PrimeVue components here
  },
  data() {
    return {};
  },
  template: "
    <div>
      <NavbarComponent />
      <InputText />
      <Button />
      <VCodeBlock />
      <Dropdown />
      <Textarea />
      <Message />
      <TabView>
        <TabPanel />
        <!-- Add more TabPanels as necessary -->
      </TabView>
    </div>
  ",
});
    `,
  },
  {
    filename: "main.scss",
    lang: "scss",
    code: `
@tailwind base;
@tailwind components;

:root {
  --primary-color: rgb(219, 39, 119); /* Magenta */
}

body {
  background-color: rgba(var(--primary-color), 0.03);
}
    `,
  },
];
