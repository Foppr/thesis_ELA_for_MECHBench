import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Self-similar fractal component with hierarchical scaling
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale periodic components with diminishing amplitude
            scale_factor = 2.0 ** (i % 3)
            freq = 2 * np.pi * scale_factor
            amplitude = 1.0 / (1.0 + 0.5 * i)
            fractal_term += amplitude * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.5)
        
        # Hierarchical curvature with recursive interaction
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive distance-based coupling with fractal scaling
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling_strength = 1.0 / (1.0 + distance ** (1.5 + 0.2 * np.sin(i * 0.3)))
                curvature_term += coupling_strength * (x_normalized[i]**4 + x_normalized[j]**4)
        
        # Multi-scale interference with fractal frequency modulation
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal frequency scaling based on dimension index
                freq_i = 2 ** (i % 4) * (1 + 0.3 * np.cos(i * 0.5))
                freq_j = 2 ** (j % 4) * (1 + 0.3 * np.sin(j * 0.5))
                interference_term += np.sin(freq_i * x_normalized[i] + freq_j * x_normalized[j]) * \
                                   np.cos(freq_i * x_normalized[i] * 0.7 + freq_j * x_normalized[j] * 0.7)
        
        # Scale-invariant radial component with fractal exponent
        radial_term = 0.0
        for i in range(self.dim):
            # Fractal-like radial term with varying exponents
            exponent = 1.5 + 0.5 * np.sin(i * 0.4)
            radial_term += x_normalized[i] ** exponent
        
        # Chaotic component with fractal perturbations
        chaotic_term = 0.0
        for i in range(self.dim):
            # Fractal perturbation with recursive scaling
            base_freq = 3 * (1 + 0.4 * np.sin(i * 0.6))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.4)
            chaotic_term += perturbation * (1.0 / (1.0 + 0.1 * i))
        
        # Combine all terms with dynamic weights
        return (0.3 * fractal_term + 
                0.25 * curvature_term + 
                0.2 * interference_term + 
                0.15 * radial_term + 
                0.1 * chaotic_term)