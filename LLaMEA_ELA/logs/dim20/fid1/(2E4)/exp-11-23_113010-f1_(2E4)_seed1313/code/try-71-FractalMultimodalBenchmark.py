import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like polynomial structure with recursive scaling
        result = 0.0
        for i in range(self.dim):
            # Recursive polynomial with varying degrees and scaling factors
            term = x_norm[i]**3 + 0.5 * x_norm[i]**5 + 0.2 * x_norm[i]**7
            # Add chaotic phase shift using prime numbers
            phase_shift = np.sin((i+1) * np.pi * x_norm[i] / (i+2))
            term *= (1 + 0.3 * phase_shift)
            result += term
            
        # Cross-dimensional fractal coupling with recursive interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling using nested trigonometric functions
                coupling = np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * \
                          np.cos(5 * np.pi * (x_norm[i] - x_norm[j])) * \
                          np.sin(7 * np.pi * (x_norm[i]**2 + x_norm[j]**2))
                cross_term += coupling
                
        # Adaptive noise modulation based on dimensionality
        noise = 0.01 * np.random.random() * (1 + 0.1 * self.dim)
        
        # Add fractal basin terms with self-similar structure
        basin = 0.0
        for i in range(self.dim):
            # Self-similar polynomial with diminishing coefficients
            basin += (0.1 * x_norm[i]**4 + 0.05 * x_norm[i]**6 + 0.02 * x_norm[i]**8)
            
        return 1.5 * result + 0.8 * cross_term + 0.6 * basin + noise