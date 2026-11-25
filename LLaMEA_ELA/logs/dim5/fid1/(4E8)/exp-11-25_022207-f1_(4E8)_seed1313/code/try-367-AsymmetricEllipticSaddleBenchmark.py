import numpy as np

class AsymmetricEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define asymmetric elliptic parameters
        self.elliptic_axes = np.logspace(0.5, 3.5, min(20, dim))
        self.saddle_strengths = np.random.uniform(0.5, 3.0, min(15, dim))
        self.conditioning_gradients = np.linspace(1.0, 10.0, min(25, dim))
        # Asymmetric coupling factors
        self.asymmetry_factors = np.random.uniform(-0.5, 0.5, min(20, dim))
        # Dynamic modulation frequencies
        self.modulation_frequencies = np.logspace(1.0, 4.0, min(15, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Elliptic contour component
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_axes), self.dim)):
            axis = self.elliptic_axes[i]
            elliptic_term += axis * (x_norm[i] ** 2)
            
        # Asymmetric saddle points
        saddle_term = 0.0
        for i in range(min(len(self.saddle_strengths), self.dim)):
            strength = self.saddle_strengths[i]
            asymmetry = self.asymmetry_factors[i]
            saddle_term += strength * (x_norm[i] ** 2) * (1.0 + asymmetry * np.sin(2.0 * x_norm[i]))
            
        # Dynamic conditioning gradients
        condition_term = 0.0
        for i in range(min(len(self.conditioning_gradients), self.dim)):
            gradient = self.conditioning_gradients[i]
            condition_term += gradient * np.abs(x_norm[i])
            
        # Modulated interaction terms
        modulation_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                freq_i = self.modulation_frequencies[i % len(self.modulation_frequencies)]
                freq_j = self.modulation_frequencies[j % len(self.modulation_frequencies)]
                modulation_term += np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j])
                
        # Combined landscape
        result = 0.5 * elliptic_term + 0.3 * saddle_term + 0.2 * condition_term + 0.1 * modulation_term
        
        return result