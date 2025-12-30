import json

def handler(request):
    # Simple serverless Python function for Vercel
    data = {
        "site_overview": {
            "name": "AI Web App (Vercel Python API)",
            "description": "Static frontend hosted on Vercel + Python serverless API."
        },
        "solutions_catalog": [
            {
                "category": "Cloud Services",
                "services": [
                    {
                        "title": "Cloud Migration",
                        "short_description": "Secure migration to scalable cloud platforms",
                    }
                ]
            }
        ]
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data)
    }