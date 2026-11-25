import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quantum harmonic oscillator components with adaptive frequencies
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 1.2 + 0.6 * np.sin(0.4 * x[i]) + 0.3 * np.cos(0.5 * x[i]) + 0.1 * np.sin(0.9 * x[i])
            amplitude = 1.1 + 0.4 * np.sin(0.6 * x[i])
            quantum_harmonic += amplitude * (x[i]**2) * np.cos(freq * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Enhanced dynamic coupling terms with nonlinear interaction coefficients
        dynamic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear coupling coefficient based on coordinates and dimension
                coeff = 0.7 + 0.4 * np.sin(0.3 * (x[i] + x[j])) * np.cos(0.2 * (x[i] - x[j]))
                dynamic_coupling += coeff * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Fractal-based radial basis functions with chaotic center modulation
        fractal_rbf = 0
        for i in range(self.dim):
            center = 2.5 * np.sin(0.5 * x[i]) + 1.0 * np.cos(0.7 * x[i]) + 0.3 * np.sin(0.9 * x[i]) + 0.2 * np.cos(1.1 * x[i])
            width = 0.6 + 0.4 * np.sin(0.4 * x[i]) + 0.2 * np.cos(0.6 * x[i])
            fractal_rbf += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(0.8 * x[i]) * np.sin(0.3 * x[i])
        
        # Adaptive saddle-point structure with enhanced curvature and dimension scaling
        adaptive_saddle = 0
        for i in range(self.dim):
            a = 1.3 + 0.5 * np.sin(0.4 * x[i])
            b = 0.9 + 0.3 * np.cos(0.6 * x[i])
            adaptive_saddle += (x[i]**2 - a) * (x[i]**2 - b) * np.sin(0.7 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Chaotic sine-cosine interactions with enhanced fractal modulation
        chaotic_interaction = 0
        for i in range(self.dim):
            mod_freq = 1.8 + 0.7 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.4 * x[i])
            mod_amp = 1.0 + 0.5 * np.sin(0.6 * x[i]) + 0.2 * np.cos(0.5 * x[i])
            chaotic_interaction += mod_amp * np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i]) * np.exp(-0.08 * x[i]**2)
        
        # Enhanced global conditioning factor with dimension scaling
        condition_factor = 1.2 + 0.3 * np.sin(0.6 * self.dim) + 0.2 * np.cos(0.4 * self.dim) + 0.1 * np.sin(0.8 * self.dim)
        
        # Combine all components with optimized weights for improved fitness
        return condition_factor * (0.25 * quantum_harmonic + 0.3 * dynamic_coupling + 
                                  0.25 * fractal_rbf + 0.15 * adaptive_saddle + 0.05 * chaotic_interaction)