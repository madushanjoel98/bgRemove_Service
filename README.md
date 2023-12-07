# Flask Background Removing Rest Service
<img src="https://hotpot.ai/images/site/ai/background_remover/teaser.jpg" width="350px">

---

**Image Processing Service**

This service allows users to upload binary-encoded images in BASE64 format and receive binary output. The implementation is done using the Flask library, providing a simple and efficient web interface for image processing tasks. Before running the program, it is essential to ensure that the 'rgm' library is up-to-date. To do so, please check for the latest version of the 'rgm' library before executing the program. This ensures compatibility and incorporates any potential updates or improvements. For detailed instructions on how to run the service and ensure library compatibility, please refer to the documentation below.


Starting the Application
<ul>
  <li ><a href="process/app.py">Run the app,py</a></li>
    <li> Run this end point on Post man http://127.0.0.1:5000/bas64remover </li>
</ul>

   ```javascript
//Run this json body on POSTMAN 
{"base": "your Base 64 text"}
```



 
