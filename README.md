# AutGPT-Instagram
A plugin for AutoGPT which enables access to Instagram.

### Plugin Installation Steps

1. **Clone or download the plugin repository:**
   Clone the plugin repository, or download the repository as a zip file.
  
   ![Download Zip](https://raw.githubusercontent.com/BillSchumacher/Auto-GPT/master/plugin.png)

2. **Install the plugin's dependencies (if any):**
   Navigate to the plugin's folder in your terminal, and run the following command to install any required dependencies:

   ``` shell
      pip install -r requirements.txt
   ```

3. **Package the plugin as a Zip file:**
   If you cloned the repository, compress the plugin folder as a Zip file.

4. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

5. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ``` shell
   ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3
   ```

6. **Add Instagram cretentials to env file: **
   ```
   INSTAGRAM_USERNAME=username
   INSTAGRAM_PASSWORD=password
   ```
