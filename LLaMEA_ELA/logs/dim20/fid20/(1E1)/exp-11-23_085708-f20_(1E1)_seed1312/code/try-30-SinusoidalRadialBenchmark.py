import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) * np.cos(7 * r))
        
        # Polynomial cross-terms with fractal-like scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i]**3 + x[j]**3) * np.sin((i + j + 1) * r) * (1 + 0.2 * np.cos(3 * (x[i] - x[j])))
                
        # Chaotic gradient modulation with multiple frequencies
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i]) * np.cos(x[i] * 0.7) * np.sin(x[i] * 0.3))
            
        # Fractal-like multimodal component with self-similar patterns
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 0.3 * np.sin(9 * x[i]) + 0.1 * np.sin(27 * x[i])) * (1 + 0.2 * np.cos(5 * x[i]))
            
        # Additional chaotic component with varying amplitude
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * np.pi * (i + 1)) * np.cos(x[i] * np.pi * (i + 1) * 0.5)
            
        # Combine all terms with adaptive weighting
        return radial_term + cross_term + grad_mod * multi_modal + 0.5 * chaotic_term + 5.0