from django.db import models
from django.contrib.auth.models import User
import requests

class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prescription_details = models.TextField()
    verification_status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected')
    ), default='pending')
    verification_notes = models.TextField(blank=True, null=True)

    def verify_prescription(self, prescription):
        # Construct the API request based on the prescription details
        api_url = 'https://state-healthcare-office-api.com/verify'
        api_key = 'your-api-key'  # Replace with your actual API key
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'prescription_details': prescription.prescription_details}

        # Make a POST request to the API
        response = requests.post(api_url, headers=headers, json=data)

        # Process the API response
        if response.status_code == 200:
            verification_data = response.json()
            verification_status = verification_data.get('status')
            verification_notes = verification_data.get('notes')

            # Update the prescription verification status and notes
            prescription.verification_status = verification_status
            prescription.verification_notes = verification_notes
            prescription.save()
        else:
            # Handle API errors
            print(f"Error: Failed to verify prescription (Status code: {response.status_code})")

    def __str__(self):
        return f"Prescription #{self.id} for {self.user.username} - Status: {self.verification_status}"
