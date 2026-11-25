import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced exponential decay radial term with double exponential scaling
        radial_term = np.sum(np.exp(-0.3 * x_normalized**2) * np.exp(-0.7 * x_normalized**4))
        
        # Sinusoidal modulation with chaotic frequency variations and multi-harmonic components
        modulated_term = 0.0
        for i in range(self.dim):
            freq_base = 3 ** (i % 6) * (1 + 0.3 * np.sin(i * 0.5))
            freq_harmonic = 2 * freq_base + 0.5 * np.cos(i * 0.7)
            amp = 1.0 / (1.0 + np.exp(-0.4 * i)) * (1 + 0.2 * np.sin(i * 0.3))
            modulated_term += amp * np.sin(freq_base * x_normalized[i]) * np.cos(freq_harmonic * x_normalized[i] * 0.6)
        
        # Adaptive curvature with multi-dimensional coupling and dynamic interaction
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x_normalized[i] - x_normalized[j])**2 + 0.1 * np.sin(i * 0.5) * np.cos(j * 0.5))
                coupling = np.exp(-distance * (1.5 + 0.3 * np.sin(i * 0.4 + j * 0.3)))
                curvature_term += coupling * (x_normalized[i]**3 + x_normalized[j]**3)
        
        # Chaotic gradient component with multi-directional perturbations and time-delayed feedback
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 6 * (1 + 0.4 * np.cos(i * 0.7))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.4) * np.exp(-0.15 * i)
            chaotic_gradient += perturbation
        
        # Multi-scale interference with non-linear coupling and asymmetric weights
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (1.0 / (1.0 + (i + j) * 0.15)) * (1 + 0.3 * np.sin(i * 0.4))
                interference_term += weight * np.sin(12 * x_normalized[i] * x_normalized[j]) * np.cos(10 * x_normalized[i] + 8 * x_normalized[j])
        
        # Add a global periodic modulation to increase landscape complexity
        periodic_mod = np.sum(np.sin(0.5 * x_normalized) * np.cos(0.3 * x_normalized))
        
        # Combined function with dynamic weighting and additional noise component
        return (0.35 * radial_term + 
                0.25 * modulated_term + 
                0.2 * curvature_term + 
                0.15 * chaotic_gradient + 
                0.4 * interference_term + 
                0.1 * periodic_mod)