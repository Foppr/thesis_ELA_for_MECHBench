import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Time-varying frequency modulation with chaotic coupling
        result = 0.0
        for i in range(self.dim):
            # Dynamic frequency based on dimension index and position
            freq = (i + 1) * (1 + 0.3 * np.sin(x_norm[i] * np.pi)) * (2 + np.cos(i * 0.5))
            
            # Nested trigonometric components with varying amplitudes
            term1 = np.sin(freq * x_norm[i])
            term2 = np.cos(freq * x_norm[i]**2)
            term3 = np.sin(freq * x_norm[i]**3)
            term4 = np.cos(freq * x_norm[i]**4)
            
            # Exponential basin scaling with position-dependent factor
            scale = np.exp(-0.5 * np.abs(x_norm[i]))
            
            # Chaotic phase coupling between dimensions
            coupling = 1.0
            for j in range(i):
                coupling *= (1 + 0.2 * np.sin(x_norm[j] * (j + 1) * np.pi))
            
            result += scale * term1 * term2 * term3 * term4 * coupling
            
        # Add a global chaotic component with fractal-like behavior
        global_component = 0.0
        for i in range(self.dim):
            freq_global = 2**(i % 5 + 1) * (1 + 0.25 * np.sin(i * np.pi / self.dim))
            global_component += np.sin(freq_global * x_norm[i]) * np.cos(freq_global * x_norm[i]**2)
            
        # Combine components with dynamic weights
        weight1 = 0.7 + 0.3 * np.sin(self.dim * 0.1)
        weight2 = 0.3 + 0.7 * np.cos(self.dim * 0.15)
        
        return weight1 * result + weight2 * global_component