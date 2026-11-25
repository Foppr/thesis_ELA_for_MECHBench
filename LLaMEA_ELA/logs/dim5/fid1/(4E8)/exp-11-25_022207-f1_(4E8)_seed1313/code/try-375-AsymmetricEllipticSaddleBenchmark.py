import numpy as np

class AsymmetricEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define asymmetric elliptic parameters
        self.elliptic_axes = np.logspace(0.5, 4.0, min(25, dim))
        self.saddle_strengths = np.random.uniform(0.8, 4.0, min(20, dim))
        self.conditioning_gradients = np.linspace(1.0, 15.0, min(30, dim))
        # Asymmetric coupling factors
        self.asymmetry_factors = np.random.uniform(-0.7, 0.7, min(25, dim))
        # Dynamic modulation frequencies
        self.modulation_frequencies = np.logspace(1.0, 5.0, min(20, dim))
        # Additional chaotic components
        self.chaotic_amplitudes = np.random.uniform(0.5, 2.5, min(15, dim))
        self.noise_levels = np.random.uniform(0.1, 0.5, min(10, dim))
        
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
                
        # Chaotic interaction terms
        chaotic_term = 0.0
        for i in range(min(len(self.chaotic_amplitudes), self.dim)):
            amp = self.chaotic_amplitudes[i]
            chaotic_term += amp * np.sin(3.0 * x_norm[i]) * np.cos(5.0 * x_norm[i])
            
        # Cross-dimensional coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling_term += (x_norm[i] ** 3) * (x_norm[j] ** 2) * np.sin(2.0 * x_norm[i] + x_norm[j])
                
        # Combined landscape
        result = 0.4 * elliptic_term + 0.3 * saddle_term + 0.2 * condition_term + 0.05 * modulation_term + 0.05 * chaotic_term + 0.05 * coupling_term
        
        return result