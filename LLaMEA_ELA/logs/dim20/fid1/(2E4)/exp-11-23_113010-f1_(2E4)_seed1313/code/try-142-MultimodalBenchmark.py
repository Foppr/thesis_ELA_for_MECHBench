import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic frequency modulation with adaptive coupling
        result = 0.0
        for i in range(self.dim):
            # Adaptive frequency based on dimension and position with enhanced chaos
            freq = (i + 1) * (1 + 0.4 * np.sin(x_norm[i] * np.pi)) * (1.5 + 0.5 * np.cos(i * 0.3))
            
            # Modified nested trigonometric components with different exponents
            term1 = np.sin(freq * x_norm[i])
            term2 = np.cos(freq * x_norm[i]**1.5)
            term3 = np.sin(freq * x_norm[i]**2.5)
            term4 = np.cos(freq * x_norm[i]**3.5)
            
            # Enhanced exponential basin scaling with position-dependent factor
            scale = np.exp(-0.3 * np.abs(x_norm[i])) * (1 + 0.2 * np.sin(x_norm[i] * np.pi))
            
            # Improved chaotic phase coupling between dimensions
            coupling = 1.0
            for j in range(i):
                coupling *= (1 + 0.15 * np.sin(x_norm[j] * (j + 2) * np.pi) * np.cos(x_norm[j] * (j + 1)))
            
            result += scale * term1 * term2 * term3 * term4 * coupling
            
        # Enhanced global component with modified fractal behavior
        global_component = 0.0
        for i in range(self.dim):
            freq_global = 3**(i % 4 + 1) * (1 + 0.3 * np.sin(i * np.pi / self.dim))
            global_component += np.sin(freq_global * x_norm[i]) * np.cos(freq_global * x_norm[i]**1.8)
            
        # Dynamic weighting with improved balance
        weight1 = 0.6 + 0.25 * np.sin(self.dim * 0.12)
        weight2 = 0.4 + 0.35 * np.cos(self.dim * 0.18)
        
        return weight1 * result + weight2 * global_component