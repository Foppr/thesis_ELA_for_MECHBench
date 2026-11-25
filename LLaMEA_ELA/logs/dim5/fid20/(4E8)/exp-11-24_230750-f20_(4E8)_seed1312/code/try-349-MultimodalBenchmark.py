import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulations with adaptive frequency and amplitude
        chaotic_modulation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * x[i] + 1.0)
            amp = 1.0 + 0.8 * np.cos(0.3 * x[i]**2 + 0.7)
            phase = 0.4 * np.sin(1.3 * x[i] + 0.2)
            chaotic_modulation += amp * np.sin(freq * x[i] + phase) * np.exp(-0.05 * x[i]**2)
        
        # Dynamic Gaussian peak structures with cross-dimensional interactions
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -3.0 + 1.5 * j + 0.6 * np.sin(0.8 * x[i] + 0.4)
                variance = 0.8 + 0.4 * np.cos(0.6 * x[i])
                gaussian_peaks += np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional polynomial couplings with adaptive exponents
        polynomial_coupling = 0.0
        for i in range(self.dim):
            exponent = 2.0 + 1.0 * np.sin(0.7 * x[i])
            polynomial_coupling += x[i]**exponent
        
        # Saddle-point interactions with varying weights and phases
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.5 + 0.3 * np.cos(0.4 * (x[i] - x[j]))
                saddle_interaction += weight * (x[i]**2 - x[j]**2)
        
        # Adaptive conditioning with exponential scaling and dimensionality effects
        conditioning = 1.0 + 0.5 * np.log(self.dim + 1) * np.exp(-0.1 * self.dim)
        
        return (0.3 * chaotic_modulation + 0.3 * gaussian_peaks + 
                0.2 * polynomial_coupling + 0.2 * saddle_interaction) * conditioning