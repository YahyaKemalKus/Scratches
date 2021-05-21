After starting server,you should go to localhost.At the index page you will see a button named register.When you are at registering page,

you must create an account with admin checkbox active.Because normal users are not allowed to interact with some database tables and some special pages.
(Register button creates new account but not logs in.)

Authorization and authentication processes are controlled by customauth app.

For more detailed information about these features,https://github.com/YahyaKemalKus/Scratches/tree/master/Django/Session.

Chat application is entegrated to customauth application.

Dont forget to login with admin account after created one.You can go there from main page->log in button.Then you will see that new links and pages are available at main page.

If you are wondering what admin can do and users can do,log out and create new account with admin checkbox inactive.Not only redirectings are special to admin,also urls too.

For example you can't view localhost/admin/ page with normal user account.

After you created new accounts,log in to your admin account.You should go to room creating page and create a room.

Then you should go to room permission page to give accounts permissions to make them able to join chat rooms.

When all is done,log out from your admin account and switch to one of your normal accounts.(You dont have to log out.)

If you did everything correct your accounts will be able to send messages to each other(only the room they are in).

You will be informed by your browser if connection is established or not.

Messages will be saved in database Room-chat_log and deliver to everyone in the room via websocket.

If you disconnect from a chat room and then come back,you will be able to see every message sent while you weren't there.
