# Generative AI World Cup 2024 hakhathon project

TRON Motor Company: A Digital Dream, Realized

Company Philosophy:

TRON Motor Company is a visionary automotive manufacturer inspired by the iconic film, TRON: Legacy. We blend cutting-edge technology with timeless design, creating vehicles that are not just modes of transport but experiences. Our mission is to redefine the future of mobility, pushing the boundaries of innovation and aesthetics.

Core Values:

Innovation: We embrace technological advancements to create revolutionary products.
Design: We prioritize sleek, futuristic designs that turn heads.
Performance: We deliver exhilarating driving experiences.
Sustainability: We strive for eco-friendly solutions in our manufacturing processes and vehicle technologies.
Vehicle Lineup:

Light Cycle:

Inspired by: The iconic light cycles from the film.
Key Features:
Sleek, aerodynamic design with customizable light patterns
Lightweight, high-performance electric motors
Advanced stability control and regenerative braking
Integrated augmented reality display for navigation and entertainment
Son of Flynn:

Inspired by: Sam Flynn's sleek, futuristic motorcycle.
Key Features:
Powerful electric engine for rapid acceleration
Adaptive suspension for optimal handling
Futuristic cockpit with holographic displays
Integrated AI assistant for personalized driving experience
Grid Cruiser:

Inspired by: The futuristic cars of the Grid.
Key Features:
Self-driving capabilities for autonomous travel
Sleek, minimalist design with customizable lighting
Spacious interior with advanced comfort features
Integrated renewable energy systems for sustainable power

Additional Offerings:

TRON Gear: A range of merchandise, including apparel, accessories, and collectibles.   
TRON Experience Centers: Immersive showrooms where customers can experience the brand firsthand.
TRON Community: A platform for enthusiasts to connect, share experiences, and participate in exclusive events.
Future Vision:

Usecase:
Use Case: TRON Service Manager's Customer Support Challenge
Primary Actor: TRON Service Manager

Goal: To efficiently respond to customer inquiries related to TRON vehicles and their technical specifications.

Precondition: The service manager has access to a customer support system and a database containing vehicle information.

Basic Flow:

Customer Inquiry: A customer contacts the service manager via phone, email, or chat with a query about their TRON vehicle.
Query Analysis: The service manager analyzes the query to identify the specific issue or information required.
Database Query: The service manager accesses the database to retrieve relevant vehicle information, such as model specifications, maintenance history, or troubleshooting guides.
Response Formulation: The service manager formulates a response based on the retrieved information and customer's query.
Response Delivery: The service manager delivers the response to the customer via the appropriate channel.

Solution: 

Alita is our dedicated AI assistant, designed to provide seamless support for all your TRON vehicle and accessory needs. Powered by advanced language models, Alita can:

Understand Your Queries: Alita can interpret your questions, no matter how complex, to provide accurate and relevant information.
Access Real-time Data: Stay up-to-date with the latest product information, promotions, and technical specifications.
Provide Personalized Assistance: Alita can tailor its responses to your specific needs, offering personalized recommendations and advice.
Resolve Issues Efficiently: Whether it's a simple query or a complex technical issue, Alita can help you find solutions quickly.
Learn and Adapt: Alita continuously learns from customer interactions, improving its ability to understand and assist you over time.

Steps to Run:
1. Setup rasa instance
2. clone the project
3. setup OpenAI credentials in your local
4. run below command to start the bot:
rasa run -m models --enable-api --cors "*" --debug
5. run actions in seperate terminal
rasa run actions
6. open indes.html from Chatbot-Widget-main folder to start comminicating with the bot
7. Setup sqlitestudio to add or remove data
