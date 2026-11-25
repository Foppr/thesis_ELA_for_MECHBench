import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced exponential decay radial term with adaptive scaling
        radial_term = np.sum(np.exp(-0.3 * np.abs(x_normalized)**2.5))
        
        # Sinusoidal modulation with exponentially varying frequencies and phase shifts
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 3 ** (i % 4) * (1 + 0.3 * np.sin(i * 0.4))
            amp = 1.0 / (1.0 + np.exp(-0.7 * i))
            phase_shift = 0.5 * np.cos(i * 0.2)
            modulated_term += amp * np.sin(freq * x_normalized[i] + phase_shift) * np.cos(freq * x_normalized[i] * 0.6)
        
        # Enhanced adaptive curvature with multi-scale coupling
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling = np.exp(-distance * (1.5 + 0.3 * np.sin(i * 0.5) * np.cos(j * 0.3)))
                curvature_term += coupling * (x_normalized[i]**3 + x_normalized[j]**3)
        
        # Chaotic gradient component with multi-directional perturbations and dynamic scaling (modified)
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 7 * (1 + 0.4 * np.cos(i * 0.5))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.4) * np.tan(0.5 * x_normalized[i])
            chaotic_gradient += perturbation * np.exp(-0.18 * i)  # Slightly increased decay rate
        
        # Multi-scale interference with exponentially decaying weights and cross-terms
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + (i + j) * 0.15)
                interference_term += weight * np.sin(12 * x_normalized[i] * x_normalized[j]) * np.cos(10 * x_normalized[i] + 8 * x_normalized[j]) * np.exp(-0.2 * (i + j))
        
        # Additional high-frequency oscillation component
        high_freq_term = 0.0
        for i in range(self.dim):
            freq = 15 * (1 + 0.2 * np.sin(i * 0.3))
            high_freq_term += np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.8) * np.exp(-0.05 * i**2)
        
        # Combined function with dynamic weighting (slightly adjusted coefficients)
        return (0.35 * radial_term + 
                0.25 * modulated_term + 
                0.2 * curvature_term + 
                0.12 * chaotic_gradient +  # Increased weight
                0.38 * interference_term +  # Slightly reduced weight
                0.15 * high_freq_term)