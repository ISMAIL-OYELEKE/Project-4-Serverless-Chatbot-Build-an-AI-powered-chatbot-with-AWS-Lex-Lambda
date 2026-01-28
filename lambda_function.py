import json

def lambda_handler(event, context):
    # Log the event for debugging (visible in CloudWatch)
    print("Received event: " + json.dumps(event))
    
    # 1. Identify the Intent Name safely
    try:
        intent_name = event['sessionState']['intent']['name']
    except KeyError:
        intent_name = "FallbackIntent"

    # Default fallback response
    response_text = "I'm not sure about that. Try asking about Ismail's 'Projects', 'Skills', 'Certifications', or how to 'Contact' him!"

    # =================================================================
    # 2. THE BRAIN: LOGIC FOR EACH INTENT
    # =================================================================

    # Intent 1: BIO / INTRO (Updated with First Class & Engineering Bg)
    if intent_name == 'GetIntroduction':
        response_text = (
            "I am Oyeleke Ismail, a First Class Computer Science graduate (3.85/4.0 CGPA) and an AWS Solutions Architect based in Lagos. "
            "Unlike many in the field, I started with a strong foundation in Software Engineering (.NET), which allows me to deeply understand the application logic running on the cloud.\n\n"
            "I am driven by a 'builder's mindset'—whether it's architecting a fault-tolerant VPC or coding a complex API. I believe in clean code, automated infrastructure, and continuous learning."
        )
    
    # Intent 2: SKILLS / TECH STACK
    elif intent_name == 'GetSkills':
        response_text = (
            "Ismail's core technical stack includes:\n"
            "☁️ Cloud: AWS (EC2, RDS, VPC, Lambda, Lex, Auto Scaling)\n"
            "⚙️ Backend: .NET Core, C#, API Development\n"
            "🛠️ DevOps: CI/CD Pipelines, Linux, Bash Scripting, Git"
        )
        
    # Intent 3: PROJECTS (Updated with GitHub Links)
    elif intent_name == 'GetProjects':
        response_text = (
            "Here are Oyeleke's top featured projects (Click links to view code):\n\n"
            "1️⃣ Enterprise 3-Tier Web App\n"
            "A fault-tolerant architecture on AWS with Auto Scaling.\n"
            "🔗 https://github.com/ISMAIL-OYELEKE/Project-3-Enterprise-Multi-Tier-Web-App-Deployment\n\n"
            "2️⃣ Serverless AI Chatbot\n"
            "The bot you're talking to right now! (AWS Lex + Lambda).\n"
            "🔗 https://github.com/ISMAIL-OYELEKE/Project-4-Serverless-Chatbot-Build-an-AI-powered-chatbot-with-AWS-Lex-Lambda\n\n"
            "3️⃣ Serverless Static Web Hosting\n"
            "This portfolio website hosted on S3 with Route 53 & CloudFront.\n"
            "🔗 https://github.com/ISMAIL-OYELEKE/Project-1-Static-Website-Hosting-Host-a-website-on-S3-with-Route-53-CloudFront\n\n"
            "4️⃣ Secure WordPress on Lightsail\n"
            "A production-ready blog deployment.\n"
            "🔗 https://github.com/ISMAIL-OYELEKE/Project-2-WordPress-on-AWS-Lightsail-Deploying-a-WordPress-blog-on-AWS-Lightsail"
        )

    # Intent 4: CERTIFICATIONS (Updated with Credly Links)
    elif intent_name == 'GetCertifications':
        response_text = (
            "Ismail is a Certified Cloud Professional! 🏅\n\n"
            "✅ AWS Solutions Architect – Associate (SAA-C03)\n"
            "🔗 View Badge: https://www.credly.com/badges/e096149f-4db9-42ea-b5b8-d05a45a7a63a/public_url\n\n"
            "✅ AWS Cloud Practitioner (CLF-C02)\n"
            "🔗 View Badge: https://www.credly.com/badges/cedcaae3-7094-49f8-8736-f49bd2dbbeaf/public_url\n\n"
            "✅ Aviatrix Multi-Cloud Network Associate\n"
            "🔗 View Badge: https://www.credly.com/badges/ba098e8b-a21e-41f4-aba3-a549ef50a541/public_url\n\n"
            "To see his full verifiable profile, visit Credly here:\n"
            "👉 https://www.credly.com/users/ismail-oyeleke"
        )
        
    # Intent 5: CONTACT INFO (Fixed Links)
    elif intent_name == 'GetContact':
        response_text = (
            "You can reach Oyeleke directly via:\n\n"
            "📧 Email: ismailoyeleke2003@gmail.com\n"
            "🔗 LinkedIn: https://www.linkedin.com/in/ismail-oyeleke-6930b6317\n"
            "🐙 GitHub: https://github.com/ISMAIL-OYELEKE\n\n"
            "He is currently open to new opportunities!"
        )
        
    # Intent 6: GREETINGS 
    elif intent_name == 'GetGreetings':
        response_text = (
            "Hello! 👋 I'm Ismail's AI Assistant. I'm here to help you hire him!\n\n"
            "I can tell you about his:\n"
            "• 💼 Projects\n"
            "• 🛠️ Skills\n"
            "• 🏆 Certifications\n"
            "• 📧 Contact Info\n"
            "• 👨‍💻 Background\n\n"
            "What would you like to know first?"
        )
    
    # FALLBACK (When the bot doesn't understand)
    elif intent_name == 'FallbackIntent':
        response_text = (
            "I didn't quite catch that. As an AI assistant, I can tell you about Ismail's "
            "'Projects', 'Skills', 'Certifications', or his 'Contact Info'. What would you like to know?"
        )

    # =================================================================
    # 3. CONSTRUCT RESPONSE (LEX V2 FORMAT)
    # =================================================================
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": intent_name,
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": response_text
            }
        ]
    }
    
    return response
