import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulations with dynamic frequencies
        chaotic_modulation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * x[i] + 0.3) * np.cos(0.7 * x[i]**2)
            amp = 1.0 + 0.8 * np.sin(0.6 * x[i] + 0.4)
            phase = 0.2 * np.sin(1.5 * x[i] + 0.1) * np.cos(0.9 * x[i]**2)
            chaotic_modulation += amp * np.sin(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Dynamic Gaussian peak structures with cross-dimensional interactions
        gaussian_peaks = 0.0
        for i in range(self.dim):
            center = -3.0 + 6.0 * np.sin(0.4 * x[i] + 0.2) / (1.0 + np.abs(x[i]))
            variance = 0.8 + 0.6 * np.cos(0.5 * x[i])
            height = 1.5 + 0.5 * np.sin(0.8 * x[i] + 0.3)
            gaussian_peaks += height * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional polynomial couplings with adaptive exponents
        polynomial_coupling = 0.0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.3 * np.sin(0.6 * x[i] + 0.5)
            poly_term = 0.0
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.5 + 0.5 * np.cos(0.4 * (x[i] - x[j]))
                poly_term += weight * (x[i]**2 + x[j]**2)**exp_factor
            polynomial_coupling += poly_term
        
        # Adaptive conditioning with dimensionally varying stiffness
        conditioning = 0.0
        for i in range(self.dim):
            stiffness = 1.0 + 0.8 * np.sin(0.7 * x[i] + 0.3) * np.cos(0.5 * x[i]**2)
            conditioning += 0.5 * stiffness * x[i]**4
        
        # Saddle-point interactions with complex phase couplings
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                phase_coupling = np.sin(0.5 * (x[i] + x[j]) + 0.2) * np.cos(0.3 * (x[i] - x[j]))
                saddle_interaction += phase_coupling * (x[i]**3 + x[j]**3)
        
        # Multi-scale harmonic potential with exponential modulation
        harmonic_potential = 0.0
        for i in range(self.dim):
            scale = 2.0 + np.sin(0.8 * x[i] + 0.4) * np.cos(0.6 * x[i]**2)
            harmonic_potential += scale * np.sin(3.0 * x[i]) * np.exp(-0.2 * np.abs(x[i]))
        
        # Dimensionally adaptive normalization
        norm_factor = 1.5 + 0.4 * np.log(self.dim + 1) * np.exp(-0.03 * self.dim)
        
        return (0.25 * chaotic_modulation + 0.23 * gaussian_peaks + 
                0.20 * polynomial_coupling + 0.15 * conditioning + 
                0.12 * saddle_interaction + 0.05 * harmonic_potential) * norm_factor