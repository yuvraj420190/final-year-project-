
import streamlit as st
import tensorflow as tf
import numpy as np
import streamlit as st

# Function to provide solutions for diseases
import streamlit as st
import tensorflow as tf
import numpy as np

# Function to provide solutions for diseases
def provide_solution(disease_name, language):
    solutions = {
        'Apple___Apple_scab': {
            'english': ("Apple scab is a fungal disease that affects leaves, stems, and fruit. "
                        "To control it, remove infected leaves and debris from the ground. "
                        "Apply fungicides like captan or mancozeb at the first sign of the disease to protect healthy tissue."),
            'tamil': ("ஆப்பிள் புழுக்கம் என்பது இலைகள், அடிக்கேது மற்றும் பழங்களை பாதிக்கும் பூஞ்சை நோயாகும். "
                      "இதை கட்டுப்படுத்த, தொற்றான இலைகளை மற்றும் பூமியில் உள்ள கழிவுகளை அகற்றவும். "
                      "தொற்றின் முதல் அடையாளத்தில் கேப்டன் அல்லது மாண்கோசிப் போன்ற பூஞ்சைநாசிகளைப் பயன்படுத்தவும்."),
            'hindi': ("सेब का पत्तों का दाग एक कवक रोग है जो पत्तियों, तने और फलों को प्रभावित करता है। "
                      "इस पर काबू पाने के लिए, संक्रमित पत्तियों और मलबे को हटा दें। "
                      "रोग के पहले संकेत पर स्वस्थ ऊतकों की रक्षा के लिए कैप्टन या मैनकोज़ेब जैसे कवकनाशक का प्रयोग करें।")
        },
        'Apple___Black_rot': {
            'english': ("Black rot causes dark lesions on the fruit and leaves, leading to decay. "
                        "Prune infected branches and destroy any infected fruit. "
                        "Ensure good air circulation and apply fungicides like thiophanate-methyl."),
            'tamil': ("கறுப்பு சுருங்குதல் என்பது பழங்களின் மற்றும் இலைகளின் மீது கறுப்பு அடர்த்திகளை ஏற்படுத்துகிறது, "
                      "இது உதிர்ச்சிக்கு வழிவகுக்கிறது. தொற்றான கிளைகளை வெட்டி, தொற்றான பழங்களை அழிக்கவும். "
                      "நன்றாக காற்றோட்டத்தை உறுதி செய்யவும் மற்றும் தியோபனேட்-மெதில்போன்ற பூஞ்சைநாசிகளைப் பயன்படுத்தவும்."),
            'hindi': ("काले सड़न से फल और पत्तियों पर गहरे धब्बे बनते हैं, जो सड़न का कारण बनते हैं। "
                      "संक्रमित शाखाओं को छांटें और संक्रमित फलों को नष्ट करें। "
                      "अच्छी वायु परिसंचरण सुनिश्चित करें और थियोक्लोरोथेलोनिल जैसे कवकनाशक का उपयोग करें।")
        },
        'Apple___Cedar_apple_rust': {
            'english': ("This disease is caused by a fungus that requires both apple and cedar trees to complete its life cycle. "
                        "Apply fungicides and remove nearby juniper trees to prevent the spread."),
            'tamil': ("இந்த நோய் ஒரு பூஞ்சையால் ஏற்படுகிறது, இது ஆப்பிள் மற்றும் செடர் மரங்களை தனது வாழ்க்கைச் சுற்றுக்கு தேவைப்படுத்துகிறது. "
                      "பூஞ்சைநாசிகளை தெளியவும் மற்றும் அருகிலுள்ள செடர் மரங்களை அகற்றவும்."),
            'hindi': ("यह रोग एक कवक के कारण होता है जिसे सेब और सेडर के पेड़ों की आवश्यकता होती है। "
                      "कवकनाशी लगाएं और पास के जुनिपर के पेड़ों को हटा दें ताकि प्रसार को रोका जा सके।")
        },
        'Apple___healthy': {
            'english': "Your apple tree is healthy. No action needed!",
            'tamil': "உங்கள் ஆப்பிள் மரம் ஆரோக்கியமாக உள்ளது. எதுவும் செய்ய வேண்டாம்!",
            'hindi': "आपका सेब का पेड़ स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं है!"
        },
        'Blueberry___healthy': {
            'english': "Your blueberry plant is healthy. No action required.",
            'tamil': "உங்கள் நீலமணி செடி ஆரோக்கியமாக உள்ளது. எந்த நடவடிக்கையும் தேவையில்லை.",
            'hindi': "आपका ब्लूबेरी पौधा स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं।"
        },
        'Cherry_(including_sour)___Powdery_mildew': {
            'english': ("Powdery mildew is a fungal disease characterized by white powdery spots on leaves. "
                        "Use sulfur or neem oil to treat powdery mildew and improve air circulation around the plants."),
            'tamil': ("பவுடர்மில்டியுவென்று அழைக்கப்படும் இந்த பூஞ்சை நோய், இலைகளின் மீது வெள்ளை தூசி போன்ற இடங்கள் ஏற்படுத்துகிறது. "
                      "பவுடர்மில்டியுவுக்கு சல்பர் அல்லது நீம் எண்ணெய் பயன்படுத்தவும் மற்றும் செடிகளின் சுற்றுப்புறத்தில் காற்றோட்டத்தை மேம்படுத்தவும்."),
            'hindi': ("पाउडरी मिल्ड्यू एक कवक रोग है जो पत्तियों पर सफेद पाउडर जैसे धब्बे बनाता है। "
                      "पाउडरी मिल्ड्यू के इलाज के लिए सल्फर या नीम के तेल का उपयोग करें और पौधों के चारों ओर हवा के प्रवाह में सुधार करें।")
        },
        'Cherry_(including_sour)___healthy': {
            'english': "Your cherry plant is healthy. No action required.",
            'tamil': "உங்கள் செர்ரி செடி ஆரோக்கியமாக உள்ளது. எந்த நடவடிக்கையும் தேவையில்லை.",
            'hindi': "आपका चेरी पौधा स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं।"
        },
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
            'english': ("Cercospora leaf spot is caused by a fungus and appears as grayish-brown spots on leaves. "
                        "Apply fungicides and ensure proper crop rotation to reduce disease spread."),
            'tamil': ("சர்கோஸ்போரா இலைக்குழம்பல் ஒரு பூஞ்சை காரணமாக ஏற்படுகிறது மற்றும் இலைகளில் இளஞ்சிவப்பு-தூய்மையான இடங்களாக தோன்றுகிறது. "
                      "பூஞ்சைநாசிகளைப் பயன்படுத்தவும் மற்றும் நோயின் பரவலைக் குறைக்க சரியான பயிர் சுழற்சியை உறுதி செய்யவும்."),
            'hindi': ("सर्कोस्पोरा पत्तों का धब्बा एक कवक के कारण होता है और पत्तियों पर धूसर-ब्राउन धब्बों के रूप में प्रकट होता है। "
                      "कवकनाशी लगाएं और रोग के प्रसार को कम करने के लिए उचित फसल चक्र सुनिश्चित करें।")
        },
        'Corn_(maize)___Common_rust_': {
            'english': ("Common rust is a fungal disease that appears as reddish-brown pustules on the leaves. "
                        "Use resistant hybrids and fungicides like mancozeb or chlorothalonil."),
            'tamil': ("பொது சுருங்குதல் என்பது இலைகளில் சிவப்பு-சிகப்பு பூஞ்சை நோயாகக் காணப்படுகிறது. "
                      "எதிர்ப்பு உள்ள ஹைபிரிட்களைப் பயன்படுத்தவும் மற்றும் மாண்கோசிப் அல்லது கிளோரோத்தாலோனில் போன்ற பூஞ்சைநாசிகளைப் பயன்படுத்தவும்."),
            'hindi': ("सामान्य जंग एक कवक रोग है जो पत्तियों पर लाल-भूरे फुंसी के रूप में प्रकट होता है। "
                      "प्रतिरोधी हाइब्रिड और मैनकोज़ेब या क्लोरोथालोनिल जैसे कवकनाशक का उपयोग करें।")
        },
        'Corn_(maize)___Northern_Leaf_Blight': {
            'english': ("Northern leaf blight appears as long, elliptical grayish lesions on leaves. "
                        "Apply fungicides and plant disease-resistant varieties."),
            'tamil': ("வடக்கு இலைக் குழம்பல் இலைகளில் நீளமான, முட்டையாக தோன்றும் இடமாக காணப்படுகிறது. "
                      "பூஞ்சைநாசிகளைப் பயன்படுத்தவும் மற்றும் நோய்தொற்று எதிர்ப்புடைய வகைகளை நடவும்."),
            'hindi': ("उत्तर पत्तों की धुंध पत्तियों पर लंबे, अंडाकार धूसर धब्बों के रूप में प्रकट होती है। "
                      "कवकनाशी लगाएं और रोग प्रतिरोधी किस्मों को लगाएं।")
        },
        'Corn_(maize)___healthy': {
            'english': "Your corn is healthy. No action required.",
            'tamil': "உங்கள் மக்காச்சோளம் ஆரோக்கியமாக உள்ளது. எந்த நடவடிக்கையும் தேவையில்லை.",
            'hindi': "आपका मक्का स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं।"
        },
        'Grape___Black_rot': {
            'english': ("Black rot causes dark spots on grapes and can lead to fruit decay. "
                        "Prune infected vines, apply fungicides like myclobutanil, and maintain proper hygiene in the vineyard."),
            'tamil': ("கறுப்பு சுருங்குதல் திராட்சைகளில் கறுப்பு இடங்களை ஏற்படுத்துகிறது மற்றும் பழம் துர்நாற்றத்திற்கு வழிவகுக்கிறது. "
                      "தொற்றான கொடியை வெட்டி, மைக்ளோபுடனில் போன்ற பூஞ்சைநாசிகளைப் பயன்படுத்தவும், மற்றும் தோட்டத்தில் நன்றாக சுத்தம் செய்யவும்."),
            'hindi': ("काले सड़न अंगूर पर काले धब्बे डालता है और फल सड़ने का कारण बन सकता है। "
                      "संक्रमित बेलों को छांटें, माइक्लोब्यूटेनिल जैसे कवकनाशक का उपयोग करें और अंगूर के बाग में उचित स्वच्छता बनाए रखें।")
        },
        'Grape___healthy': {
            'english': "Your grape vine is healthy. No action needed!",
            'tamil': "உங்கள் திராட்சை கொடி ஆரோக்கியமாக உள்ளது. எதுவும் செய்ய வேண்டாம்!",
            'hindi': "आपकी अंगूर की बेल स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं है!"
        },
        'Peach___Bacterial_spot': {
            'english': ("Bacterial spot causes dark lesions on leaves and fruit. "
                        "Prune infected branches and apply copper-based bactericides."),
            'tamil': ("பாக்டீரியல் புள்ளி தொற்றான இலைகள் மற்றும் பழங்களில் கறுப்பு இடங்களை ஏற்படுத்துகிறது. "
                      "தொற்றான கிளைகளை வெட்டி, நக்சைனின் அடிப்படையில் உள்ள பாக்டீரியாசிடுகளைப் பயன்படுத்தவும்."),
            'hindi': ("बैक्टीरियल स्पॉट पत्तियों और फलों पर काले धब्बे बनाता है। "
                      "संक्रमित शाखाओं को छांटें और तांबे आधारित बैक्टीरियाशोधक लगाएं।")
        },
        'Peach___healthy': {
            'english': "Your peach tree is healthy. No action needed!",
            'tamil': "உங்கள் பூசணிக்காய் மரம் ஆரோக்கியமாக உள்ளது. எதுவும் செய்ய வேண்டாம்!",
            'hindi': "आपका पीच का पेड़ स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं है!"
        },
        'Pepper,_bell___Bacterial_spot': {
            'english': ("Bacterial spot causes dark, water-soaked lesions on leaves. "
                        "Ensure good air circulation and use copper fungicides for treatment."),
            'tamil': ("பாக்டீரியல் புள்ளி இலைகளில் கறுப்பு, நீர் செரிந்து போகும் இடங்களை உருவாக்குகிறது. "
                      "நன்றாக காற்றோட்டத்தை உறுதி செய்யவும் மற்றும் சோப்புக்கூற்று பூஞ்சைநாசிகளைப் பயன்படுத்தவும்."),
            'hindi': ("बैक्टीरियल स्पॉट पत्तियों पर काले, पानी से भरे धब्बे बनाता है। "
                      "अच्छी हवा के प्रवाह को सुनिश्चित करें और उपचार के लिए तांबे के कवकनाशक का उपयोग करें।")
        },
        'Pepper,_bell___healthy': {
            'english': "Your bell pepper plant is healthy. No action needed!",
            'tamil': "உங்கள் வெண்குழி மிளகாய் செடி ஆரோக்கியமாக உள்ளது. எதுவும் செய்ய வேண்டாம்!",
            'hindi': "आपका शिमला मिर्च का पौधा स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं है!"
        },
        'Potato___Early_blight': {
            'english': ("Early blight appears as dark spots on the leaves and can cause significant yield loss. "
                        "Apply fungicides like chlorothalonil and practice crop rotation."),
            'tamil': ("முன்னணி குழம்பல் இலைகளில் கறுப்பு இடங்களாக காணப்படுகிறது மற்றும் அதிக வருவாய் இழப்புக்கு காரணமாக இருக்கலாம். "
                      "கிளோரோத்தாலோனில் போன்ற பூஞ்சைநாசிகளைப் பயன்படுத்தவும் மற்றும் பயிர் சுழற்சியை நடைமுறைப்படுத்தவும்."),
            'hindi': ("प्रारंभिक धब्बा पत्तियों पर काले धब्बों के रूप में प्रकट होता है और महत्वपूर्ण उपज हानि का कारण बन सकता है। "
                      "क्लोरोथालोनिल जैसे कवकनाशक का उपयोग करें और फसल चक्र का अभ्यास करें।")
        },
        'Potato___healthy': {
            'english': "Your potato plant is healthy. No action needed!",
            'tamil': "உங்கள் உருளைக்கிழங்கு செடி ஆரோக்கியமாக உள்ளது. எதுவும் செய்ய வேண்டாம்!",
            'hindi': "आपका आलू का पौधा स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं है!"
        },
        'Strawberry___Leaf_scorch': {
            'english': ("Leaf scorch is caused by high temperatures and drought stress, leading to browning at the leaf edges. "
                        "Ensure adequate watering and mulching to maintain soil moisture."),
            'tamil': ("இலைகள் கொசிக்கும் நோய் வெப்பநிலை அதிகரிக்கும் போது ஏற்படுகிறது, இது இலை எல்லைகளில் சிவப்பாகவும் நிறத்தை இழக்கச் செய்கிறது. "
                      "மண் ஈரப்பதத்தை உறுதிப்படுத்த, போதுமான நீர்ப்பாசனத்தை மற்றும் மூடி செயல்படுத்தவும்."),
            'hindi': ("पत्तों की जलन उच्च तापमान और सूखे के तनाव के कारण होती है, जो पत्तियों के किनारों पर भूरापन लाती है। "
                      "मिट्टी की नमी बनाए रखने के लिए उचित पानी और मल्चिंग सुनिश्चित करें।")
        },
        'Strawberry___healthy': {
            'english': "Your strawberry plant is healthy. No action needed!",
            'tamil': "உங்கள் ஸ்ட்ரோபெர்ரி செடி ஆரோக்கியமாக உள்ளது. எதுவும் செய்ய வேண்டாம்!",
            'hindi': "आपका स्ट्रॉबेरी का पौधा स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं है!"
        },
        'Tomato___Bacterial_spot': {
            'english': ("Bacterial spot causes dark, water-soaked lesions on leaves and stems. "
                        "Use resistant varieties and apply copper-based fungicides."),
            'tamil': ("பாக்டீரியல் புள்ளி இலைகள் மற்றும் அடிக்கேதுகளில் கறுப்பு, நீர் செரிந்து போகும் இடங்களை உருவாக்குகிறது. "
                      "எதிர்ப்பு வகைகளைப் பயன்படுத்தவும் மற்றும் காம்பர் அடிப்படையிலான பூஞ்சைநாசிகளைப் பயன்படுத்தவும்."),
            'hindi': ("बैक्टीरियल स्पॉट पत्तियों और तनों पर काले, पानी से भरे धब्बे बनाता है। "
                      "प्रतिरोधी किस्मों का उपयोग करें और तांबे आधारित कवकनाशक लगाएं।")
        },
        'Tomato___healthy': {
            'english': "Your tomato plant is healthy. No action needed!",
            'tamil': "உங்கள் தக்காளி செடி ஆரோக்கியமாக உள்ளது. எதுவும் செய்ய வேண்டாம்!",
            'hindi': "आपका टमाटर का पौधा स्वस्थ है। कोई कार्रवाई की आवश्यकता नहीं है!"
        },
        'not_applicable': {
            'english': {
                'symptoms': "N/A",
                'prevention': "N/A",
                'treatment': "Sorry, this disease cannot be predicted."
            },
            'tamil': {
                'symptoms': "தரவரிசை இல்லை.",
                'prevention': "தரவரிசை இல்லை.",
                'treatment': "மன்னிக்கவும், இந்த நோயை கணிக்க முடியவில்லை."
            },
            'hindi': {
                'symptoms': "N/A",
                'prevention': "N/A",
                'treatment': "क्षमा करें, इस बीमारी की भविष्यवाणी नहीं की जा सकती।"
            }
        }
    }
    return solutions.get(disease_name, solutions['not_applicable'])[language]


# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # convert single image to batch
    predictions = model.predict(input_arr)
    
    predicted_index = np.argmax(predictions)
    confidence = np.max(predictions)  # Get confidence score
    return predicted_index, confidence  # return index and confidence score

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# Main Page
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "home_page.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!
    """)

elif app_mode == "About":
    st.header("About")
    st.markdown("""
    This system helps in identifying plant diseases by analyzing leaf images using machine learning techniques.
    """)

# Prediction Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    
    if test_image is not None:
        st.image(test_image, use_column_width=True)
    
    # Language selection using selectbox
    st.subheader("Choose your preferred language:")
    selected_language = st.selectbox("Select language", ['english', 'tamil', 'hindi'])
    
    if st.button("Predict"):
        if test_image is not None:
            st.snow()
            st.write("Analyzing the image...")
            
            # Predict the result
            result_index, confidence = model_prediction(test_image)
            
            class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                          'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                          'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                          'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                          'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                          'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                          'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',  
                          'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                          'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                          'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                          'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                          'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                          'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                          'Tomato___healthy']
            
            if result_index >= len(class_name) or confidence < 0.5:
                # If the confidence of prediction is low or index is out of class range, treat it as unrecognized
                st.error("Sorry, this cannot predict the disease.")
                disease_name = 'not_applicable'
            else:
                disease_name = class_name[result_index]
                st.success(f"The model predicts the disease is: {disease_name}")
            
            # Get the solution based on the selected language
            solution = provide_solution(disease_name, selected_language)
            
            st.write("**Solution:**")
            st.write(solution)
        else:
            st.error("Please upload an image before prediction!")