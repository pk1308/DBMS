#  Summary of Lecture 7.5 - Application Design and Development5.pdf 
**Summary**
**Rapid Application Development**

Rapid Application Development (RAD) aims to accelerate application development. It employs techniques such as:

* Function libraries for generating user interface elements
* Drag-and-drop features in IDEs
* Automatic code generation from declarative specifications

RAD tools include G Suite, Google App Engine, Microsoft Azure, Amazon Elastic Compute Cloud (EC2), and AWS Elastic Beanstalk.

ASP.NET and Visual Studio provide drag-and-drop development using server-interpreted controls. Validators can be added to form input fields, and data can be displayed in tabular format using DataGrid.

**Application Performance and Security**

**Application Performance**

* Caching techniques are used to reduce the cost of serving pages by exploiting commonalities between requests.
* Caching can be implemented at the server site (e.g., JDBC connection pooling, query result caching, HTML caching) or at the client's network (e.g., page caching by Web proxy).

**Application Security**

* **SQL Injection:** Constructing queries using user inputs without proper parameterization can lead to SQL injection attacks.
* **Password Leakage:** Passwords should never be stored in clear text, and database access should be restricted by IP address.
* **Authentication:** Single-factor authentication (e.g., passwords) is risky. Two-factor authentication (e.g., password plus one-time password) is more secure.
* **Application-Level Authorization:** Current SQL standards do not allow fine-grained authorization. Workarounds include using views or extensions like Oracle Virtual Private Database (VPD).
* **Audit Trails:** Applications should log actions to detect security breaches and identify perpetrators. Audit trails are needed at both database and application levels.

**Challenges in Web Application Development**

* User Interface and User Experience
* Scalability
* Performance
* Knowledge of Framework and Platforms
* Security

**Mobile Apps**

**Definition:**

* Software applications designed for mobile devices (e.g., smartphones, tablets).

**Characteristics:**

* Designed for small, wireless devices
* Limited form factor, memory, computing power, power, and bandwidth
* May include sensors like accelerometers and touchscreens

**Types of Mobile Apps:**

* **Native Apps:** Written in the native language of a platform (e.g., Objective-C for iOS, Java for Android). Platform-specific.
* **Web Apps:** Run inside Web browsers. Feature HTML/CSS interfaces and are powered by Web programming languages. Portable across devices.
* **Hybrid Apps:** Combine attributes of both native and Web apps. Use common code across platforms while tailoring required attributes to the native system.

**Design Issues for Mobile Apps:**

* Determine device and resources
* Consider bandwidth
* Decide on architecture layers
* Select technology
* Define user interface
* Select navigation
* Maintain flow
