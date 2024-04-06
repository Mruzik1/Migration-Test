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

            <div class="flex flex-col w-full">
              <label for="commentInput" class="block text-sm font-semibold text-gray-700 mb-1"> Comment </label>

              <Textarea
                v-model="comment"
                rows="5"
                cols="30"
                autoResize
                placeholder="Enter comment for AI"
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
              <VCodeBlock
                v-for="code of codes"
                :code="code.value"
                highlightjs
                :key="code.value"
                :label="code.filename"
                :lang="code.lang"
                theme="night-owl"
                class="mb-4"
              />
            </div>
          </div>
        </TabPanel>

        <TabPanel header="Structure recommendation" :disabled="!codes.length">
          <div class="w-full flex flex-col items-center">
            <p>
              Based on your repository you sent me I can create a project structure for you. If you want you can give me more details about your
              project.
            </p>

            <div class="w-full flex flex-col mt-4">
              <label for="structureMessage" class="block text-sm font-semibold text-gray-700 mb-1"> Prompt for structure </label>

              <Textarea
                id="structureMessage"
                v-model="structureMessage"
                rows="5"
                cols="30"
                autoResize
                placeholder="Enter your prompt"
                class="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-magenta-500"
              />
            </div>

            <Button
              @click="Structure"
              label="Submit"
              class="p-button-success mt-4 px-12 py-2 bg-pink-500 hover:bg-pink-600 text-white font-semibold rounded"
            />
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
import Textarea from "primevue/textarea";
import Message from "primevue/message";

import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";

export default {
  name: "App",
  API_BASE: "http://10.0.4.174/",
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
      comment: null,
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
      codes: [],
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
    },
  },
};
</script>

<style lang="scss" scoped>
.p-tabview::v-deep(.p-tabview-ink-bar) {
  background-color: rgb(219, 39, 119) !important;
}
</style>
