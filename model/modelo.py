import numpy as np
import pickle
import joblib

class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um mulher com base no modelo treinado
        """
        X_input = np.array([form.rad_mean,
                            form.tex_mean,
                            form.perim_mean, 
                            form.area_mean, 
                            form.smoo_mean, 
                            form.comp_mean,
                            form.concav_mean,
                            form.cp_mean,
                            form.sym_mean,
                            form.fd_mean
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])