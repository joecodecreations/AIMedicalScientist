# AI Medical Scientist
![Image description](src/images/header.jpg)

<div style="color:red; background:red; padding:10px; text-align:center; font-weight:bold;">
  <h2> This repo is NOT ready for use yet. </h2>
</div>

## Summary

This repository aims to revolutionize the way information about diseases—both curable and incurable—is rapidly collected and analyzed. Leveraging the power of Large Language Models (LLMs), the system is designed to swiftly aggregate data, treatment options, and emerging scientific insights about specified medical conditions. By providing a comprehensive and robust analysis, this automated platform serves as a valuable resource for medical professionals, researchers, and anyone seeking in-depth knowledge on a range of diseases.

## Thesis

The extensive body of medical research generated in academic settings frequently goes unnoticed by overburdened clinicians who could benefit from these advancements. Utilizing artificial intelligence—particularly sophisticated language models—and engineering automation techniques, we can develop a streamlined, highly effective system to seamlessly disseminate crucial medical information to healthcare professionals, thereby enhancing patient care and treatment outcomes.

## Instructions

1. Clone the repository `git clone git@github.com:joecodecreations/AIMedicalScientist.git`
2. Install requirements `pip install -r requirements.txt`
3. Move .env.sample to .env to store environment variables `mv .env.sample .env`
4. Add your openAI token into the `.env` file and save the file
5. Set the subject `RESEARCH_TOPIC` in the `.env` file
6. Run `python main.py` to execute the program and gather research details

Now your files should be contained within the `/data/` subfolder broken down by category and topics within each category.




## Disclaimer & Disclosure

This system / code is intended to serve as a supplementary resource for medical professionals, researchers, and individuals interested in obtaining a broad overview of diseases and related treatments. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. The data and analysis provided by this automated platform are sourced from Large Language Models and curated databases, and while we strive for accuracy, we cannot guarantee the completeness or timeliness of the information presented.

Users are advised to consult qualified healthcare providers for personalized medical advice and treatment. We disclaim any liability for any damages or adverse effects arising from the use or reliance on the information provided by this system. Furthermore, the system does not endorse any specific medication, treatment, or therapy, and the inclusion of such information does not imply its effectiveness or suitability for any particular condition or individual.

By using this system, you acknowledge and agree to these limitations and assume all responsibility and risk associated with the use of the information provided.