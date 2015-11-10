# notifyr-listner

While the original purpose was to listen to a specific event, this app can be used to listen to any event that is pushed to the particle cloud.

## Things you'll need

  - A Heroku account
  - An environment with heroku toolbelt and git installed
  - This repo
  - A google spreadsheet

## Getting Started

### Setting up your spread sheet
The quickest way to get a properly formated spreadsheet is to create a form with a text questions titled with the column names. Once the form creates the spreadsheet, you can delete the form and rename the spreadsheet to a single word name (-'s are ok). If you want to use the base code from this repo, use Core_ID and Core_Data as the two questions.

Still in the spreadsheet, click share in the top right corner then click the sharable link button and ensure all with the link can edit. Save this link. Go to the script editor under the tools tab.

Once a scripting project is open, rename the project, then copy the code from `google-script.txt` and paste it into the script. Replace the following variables:
  - On line 37, add your spreadsheet name
  - On line 39, add the sharable url copied previously
  - Add the cases for the columns (See comment on line 49)

Once you've added your vars, click save, then click the deploy button.
  - Under "Project version", leave "New" selected and tpye your description.
  - Under "Who has access to the app:", specifiy "Anyone, even anonymous"

Click deploy, then follow the authorization links.

Click the deploy button again and copy the web app url. Cancel out of that pop-up. Use that url as the google-sheet-url variable.

### Setting up your app

Clone this repo to your environment:

```bash
git clone https://github.com/emcpacnwlabs/notifyr-listener.git
```

Create a heroku app:

```bash
heroku create
```

Add in the variables needed, feel free to change the event as well
Note:
  - you'll need to add your personal vars when specified
  - the url you put here is the script url that's tied to your spreadsheet

```bash
heroku config:set PARTICLE-URL=https://api.particle.io/v1/events
heroku config:set TOKEN=<your particle token>
heroku config:set GOOGLE-SHEET-URL=<URL for your google form>
heroku config:set EVENT=notifyr/announce
```
### Optional: Adding your columns

If you are using your own columns, you'll need to adjust the payload to reflect those columns.

### Deploying the app

Almost done, let's actually push the app to the cloud.

```bash
git push heroku master
```

Once it's done, you need to scale the app:

```bash
heroku ps:scale worker=1
```

Congrats, you now have your very own particle cloud listener.
