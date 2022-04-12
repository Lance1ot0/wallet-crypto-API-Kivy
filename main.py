from coin_market_cap_API import *
from json_functions import *

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp

class CryptoTable(BoxLayout):

    tokens_records = get_tokens_records() # Récupère les données du fichier json dans le dict tokens_records
    selected_wallet = "All"

    # Récupère le cours des crypto actuel
    BTC_current_value = number_max_length(get_token_price(BTCparameters, BTC_path_number), 8)
    ETH_current_value = number_max_length(get_token_price(ETHparameters, ETH_path_number), 8)
    SLP_current_value = number_max_length(get_token_price(SLPparameters, SLP_path_number), 8)

    # Pas encore récupéré avec l'API
    AXS_current_value = "49"

    # Calcule la valeur en $ du montant de token dans le fichier avec le prix du cours actuelle
    BTC_wallet_value_label = str(number_max_length(float(BTC_current_value) * float(tokens_records[selected_wallet]["BTC"]), 8))
    ETH_wallet_value_label = str(number_max_length(float(ETH_current_value) * float(tokens_records[selected_wallet]["ETH"]), 8)) 
    SLP_wallet_value_label = str(number_max_length(float(SLP_current_value) * float(tokens_records[selected_wallet]["SLP"]), 8))
    AXS_wallet_value_label = str(number_max_length(float(AXS_current_value) * float(tokens_records[selected_wallet]["AXS"]), 8))

    wallet_total_value_label = number_max_length(float(BTC_wallet_value_label) + float(ETH_wallet_value_label) + float(SLP_wallet_value_label) + float(AXS_wallet_value_label), 8)
    

    def token_amount_validate(self, widget, token, alter_token_function, token_amount_value, token_current_value, token_wallet_value):

        #Vérifie que l'input est bien un int
        try:
            float(widget.text)
        except ValueError:
            widget.text = ""
            return
        else:
            amount = widget.text # Récupère la valeur du texte input

            if token == "BTC":
                self.tokens_records["Binance"][token] = float(amount)
            else:
                self.tokens_records[self.selected_wallet][token] = float(amount) # Change la valeur du token dans le fichier json

            self.tokens_records["All"][token] = self.tokens_records["Binance"][token] + self.tokens_records["Ronin"][token] # Change la des tokens totaux dans le fichier json

            alter_tokens_records(self.tokens_records) # Modifie le fichier json avec la nouvelle valeur
            alter_token_function(amount, token_amount_value, token_current_value, token_wallet_value) # Appel de la fonction pour modifier les valeurs des labels liée aux tokens

            self.ids.wallet_total_value.text = number_max_length(float(self.ids.BTC_wallet_value.text) + float(self.ids.ETH_wallet_value.text) + float(self.ids.SLP_wallet_value.text), 8)
            widget.text = ""


    def alter_token_data(self, amount, token_amount_value, token_current_value, token_wallet_value):
        token_amount_value.text = amount # Change le texte du label par la donnée entré
        new_wallet_value = number_max_length(float(token_current_value) * float(amount), 8) # Calcule la valeur en $ du montant de token entrer
        token_wallet_value.text = str(new_wallet_value) # Affiche # Change le txt du label par le resultat du calcule


    def selected_wallet_toggle_button(self, selected_wallet, token, token_txt_input, token_amount_value, token_current_value, token_wallet_value, self_toggle, B_toggle, C_toggle):
        self.selected_wallet = selected_wallet

        token_txt_input.disabled = False
        token_txt_input.size = (0, dp(30))
        token_txt_input.background_color = (1,1,1,1)
        token_amount_value.text = str(self.tokens_records[self.selected_wallet][token])
        token_wallet_value.text = str(number_max_length(float(token_current_value) * self.tokens_records[self.selected_wallet][token], 8))

        # Passe les autres toggle au normal state
        self_toggle.state = "down"
        B_toggle.state = "normal"
        C_toggle.state = "normal"
        
        self.ids.wallet_total_value.text = number_max_length(float(self.ids.BTC_wallet_value.text) + float(self.ids.ETH_wallet_value.text) + float(self.ids.SLP_wallet_value.text) + float(self.ids.AXS_wallet_value.text), 8)
        
        

    def all_wallet__toggle_button(self, token, token_txt_input, token_amount_value, token_current_value, token_wallet_value, self_toggle, B_toggle, C_toggle):
        self.selected_wallet = "All"

        token_txt_input.disabled = True
        token_txt_input.size = (0, 5)
        token_txt_input.background_color = (0,0,0,1)


        token_amount_value.text = str(self.tokens_records[self.selected_wallet][token])
        token_wallet_value.text = str(number_max_length(float(token_current_value) * self.tokens_records[self.selected_wallet][token], 8))

        # Passe les autres toggle au normal state
        self_toggle.state = "down"
        B_toggle.state = "normal"
        C_toggle.state = "normal"


        # Set le label total 
        self.ids.wallet_total_value.text = number_max_length(float(self.ids.BTC_wallet_value.text) + float(self.ids.ETH_wallet_value.text) + float(self.ids.SLP_wallet_value.text) + float(self.ids.AXS_wallet_value.text), 8)



class TableApp(App): # Déclaration de la class App
    pass

TableApp().run()