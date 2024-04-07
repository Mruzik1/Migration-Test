<template>
  <div>
    <!-- Navbar -->
    <NavbarComponent />

    <main class="container mx-auto px-48 mt-12 mb-12">
      <TabView>
        <TabPanel header="Repository Refactor">
          <div class="flex flex-col gap-6 items-center">
            <Message v-if="error" severity="error" class="w-full" :closable="false">{{ error }}</Message>

            <div class="flex flex-col w-full">
              <label for="commentInput" class="block text-sm font-semibold text-gray-700 mb-1"> Repository link </label>

              <InputText
                v-model="repoLink"
                placeholder="Enter repository link"
                class="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-magenta-500"
              />
            </div>

            <div class="w-full flex flex-row gap-10">
              <div class="flex flex-col space-y-2 w-full">
                <label for="fromFramework" class="font-semibold">From:</label>
                <Dropdown
                  inputId="fromFramework"
                  v-model="selectedFrom"
                  :options="frameworks"
                  optionLabel="name"
                  placeholder="Select a framework"
                  class="w-full border border-primary-900"
                />
              </div>

              <div class="flex flex-col space-y-2 w-full">
                <label for="toFramework" class="font-semibold">To:</label>
                <Dropdown
                  inputId="toFramework"
                  v-model="selectedTo"
                  :options="frameworks"
                  optionLabel="name"
                  placeholder="Select a framework"
                  class="w-full border border-primary-900"
                />
              </div>
            </div>

            <Button
              @click="submit"
              label="Submit"
              class="p-button-success px-12 py-2 bg-pink-500 hover:bg-pink-600 text-white font-semibold rounded"
            />

            <div class="w-full">
              <div v-for="code of codes" :key="code.value" class="flex flex-col gap-4 mb-4">
                <label class="font-semibold">{{ code.filename }}</label>
                <span>{{ code.description }}</span>
                <!-- <div v-if="!code.value" class="loader mt-4 mb-4"></div> -->
              </div>
            </div>
          </div>
        </TabPanel>

        <TabPanel header="Repository code" :disabled="!codes.length">
          <div v-for="code of $options.scripts" :key="code.code" class="flex flex-col gap-4">
            <label class="font-semibold">{{ code.filename }}</label>
            <VCodeBlock :code="code.code" highlightjs :lang="code.lang" theme="night-owl" class="mb-4" />
          </div>
        </TabPanel>
      </TabView>
    </main>
  </div>
</template>

<script>
import NavbarComponent from "./components/NavbarComponent.vue";
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import VCodeBlock from "@wdns/vue-code-block";
import Dropdown from "primevue/dropdown";
import Message from "primevue/message";

import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";

import migratedCode from "./migrated.json";
import scripts from "./scripts.js";

export default {
  name: "App",
  API_BASE: "http://10.0.5.217:7676",
  scripts,
  components: {
    NavbarComponent,
    InputText,
    Button,
    VCodeBlock,
    Dropdown,
    Message,
    TabView,
    TabPanel,
  },
  data() {
    return {
      frameworks: [
        { name: "Vue", value: "vue" },
        { name: "React", value: "react" },
        { name: "Angular", value: "angular" },
      ],
      selectedFrom: null,
      selectedTo: null,
      repoLink: null,
      error: null,
      //     codes: [
      //       {
      //         lang: "python",
      //         value: `def main():
      // print("World")`,
      //         filename: "main.py",
      //       },
      //       {
      //         lang: "javascript",
      //         value: "console.log('Hello World');",
      //         filename: "main.js",
      //       },
      //     ],
      codes: migratedCode,
    };
  },

  methods: {
    submit() {
      if (!this.selectedFrom || !this.selectedTo || !this.comment || !this.repoLink) {
        this.error = "All fields are required";
        return;
      }

      if (this.selectedFrom === this.selectedTo) {
        this.error = "Frameworks should be different!";
        return;
      }

      this.error = null;

      this.axios(`${this.$options.API_BASE}/code_migrator`, {
        method: "POST",
        data: {
          selectedFrom: this.selectedFrom,
          selectedTo: this.selectedTo,
          repoLink: this.repoLink,
        },
      }).then((data) => {
        console.log(migratedCode, data);
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.p-tabview::v-deep(.p-tabview-ink-bar) {
  background-color: rgb(219, 39, 119) !important;
}

.loader {
  width: 25px;
  aspect-ratio: 1;
  border-radius: 50%;
  border: 4px solid #514b82;
  animation: l20-1 0.8s infinite linear alternate, l20-2 1.6s infinite linear;
}
@keyframes l20-1 {
  0% {
    clip-path: polygon(50% 50%, 0 0, 50% 0%, 50% 0%, 50% 0%, 50% 0%, 50% 0%);
  }
  12.5% {
    clip-path: polygon(50% 50%, 0 0, 50% 0%, 100% 0%, 100% 0%, 100% 0%, 100% 0%);
  }
  25% {
    clip-path: polygon(50% 50%, 0 0, 50% 0%, 100% 0%, 100% 100%, 100% 100%, 100% 100%);
  }
  50% {
    clip-path: polygon(50% 50%, 0 0, 50% 0%, 100% 0%, 100% 100%, 50% 100%, 0% 100%);
  }
  62.5% {
    clip-path: polygon(50% 50%, 100% 0, 100% 0%, 100% 0%, 100% 100%, 50% 100%, 0% 100%);
  }
  75% {
    clip-path: polygon(50% 50%, 100% 100%, 100% 100%, 100% 100%, 100% 100%, 50% 100%, 0% 100%);
  }
  100% {
    clip-path: polygon(50% 50%, 50% 100%, 50% 100%, 50% 100%, 50% 100%, 50% 100%, 0% 100%);
  }
}
@keyframes l20-2 {
  0% {
    transform: scaleY(1) rotate(0deg);
  }
  49.99% {
    transform: scaleY(1) rotate(135deg);
  }
  50% {
    transform: scaleY(-1) rotate(0deg);
  }
  100% {
    transform: scaleY(-1) rotate(-135deg);
  }
}
</style>
