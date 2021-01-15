**Create recipe**
----
  Returns html data of recipe creation.

* **URL**

 http://127.0.0.1:5000/create

* **Method:**

  `GET`
  

*   **Required:**
`recipe_id=[integer]`

* **Success Response:**

  * **Code:** 200  
    **Content:** `{ title:'Red sauce pasta',suitable_for:4,is_vegetarian:'Yes',ingredients:'basil,onion,garlic,tomato',cooking_instructions: 'A great introduction to pasta for kids – loads of fun to eat, and a brilliant base for adding all kinds of other fresh ingredients,created_date:datetime.15-01-2021' }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND
    **Content:** `{ error : "Page doesn't exist" }`
  * **Code:** 302 NOT FOUND
    **Content:** `{ error : "HTTP_302_FOUND" }`

 

* **Sample Call:**

  ```HTML
  Request URL: http://127.0.0.1:5000/create
  Request Method: GET
  Status Code: 200 OK
  Remote Address: 127.0.0.1:5000
  Referrer Policy: strict-origin-when-cross-origin
  ```
