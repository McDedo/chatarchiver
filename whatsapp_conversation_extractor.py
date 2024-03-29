from fpdf import FPDF

# Fonction pour lire le fichier de sauvegarde WhatsApp et extraire les conversations
def extract_whatsapp_conversations(file_path):
    try:
        # Ouvrir le fichier de sauvegarde WhatsApp en mode lecture
        with open(file_path, 'r', encoding='utf-8') as file:
            # Lire le contenu du fichier
            content = file.read()
            # Vous pouvez ajouter du code pour analyser le contenu du fichier et extraire les conversations ici
            # Par exemple, vous pourriez utiliser des expressions régulières pour rechercher des modèles de messages
            # Ensuite, vous pouvez traiter les données extraites et les convertir en PDF
            convert_to_pdf(content)
    except Exception as e:
        print(f"Erreur lors de l'extraction des conversations WhatsApp : {e}")

# Fonction pour convertir les données extraites en PDF
def convert_to_pdf(content):
    try:
        # Créer une nouvelle instance de FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        # Ajouter les données extraites au PDF
        pdf.multi_cell(0, 10, content)
        # Enregistrer le PDF sous forme de fichier
        pdf.output("whatsapp_conversations.pdf")
        print("Conversion en PDF réussie !")
    except Exception as e:
        print(f"Erreur lors de la conversion en PDF : {e}")

# Chemin vers le fichier de sauvegarde WhatsApp
file_path = "whatsapp_backup.txt"

# Appeler la fonction pour extraire les conversations WhatsApp
extract_whatsapp_conversations(file_path)
