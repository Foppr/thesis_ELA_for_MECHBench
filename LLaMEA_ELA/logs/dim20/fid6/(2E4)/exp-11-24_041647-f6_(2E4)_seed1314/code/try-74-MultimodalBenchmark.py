import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential decay radial term with adaptive scaling
        radial_term = np.sum(np.exp(-0.5 * x_normalized**2))
        
        # Sinusoidal modulation with exponentially varying frequencies
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 5) * (1 + 0.2 * np.sin(i * 0.3))
            amp = 1.0 / (1.0 + np.exp(-0.5 * i))
            modulated_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.7)
        
        # Adaptive curvature with exponential interaction
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling = np.exp(-distance * (1 + 0.5 * np.sin(i * 0.4)))
                curvature_term += coupling * (x_normalized[i]**2 + x_normalized[j]**2)
        
        # Chaotic gradient component with multi-directional perturbations
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 5 * (1 + 0.3 * np.cos(i * 0.6))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.3)
            chaotic_gradient += perturbation * np.exp(-0.1 * i)
        
        # Multi-scale interference with exponentially decaying weights
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + (i + j) * 0.1)
                interference_term += weight * np.sin(10 * x_normalized[i] * x_normalized[j]) * np.cos(8 * x_normalized[i] + 6 * x_normalized[j])
        
        # Combined function with dynamic weighting
        return (0.4 * radial_term + 
                0.3 * modulated_term + 
                0.2 * curvature_term + 
                0.1 * chaotic_gradient + 
                0.5 * interference_term)