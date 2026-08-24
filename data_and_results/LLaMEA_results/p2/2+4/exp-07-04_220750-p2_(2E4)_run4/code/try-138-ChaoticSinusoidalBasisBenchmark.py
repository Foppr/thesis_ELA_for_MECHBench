import numpy as np

class ChaoticSinusoidalBasisBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with sinusoidal modulation and chaotic perturbation
        r = np.sqrt(np.sum(x_norm**2))
        radial_component = np.exp(-0.5 * r**2) * np.sin(2 * np.pi * r) * (1 + 0.3 * np.sin(13 * r * np.pi))
        
        # Multi-sinusoidal harmonic terms with varying frequencies and amplitudes
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amplitude = 1.0 / (1.0 + 0.1 * i)
            harmonic_sum += amplitude * np.sin(freq * x_norm[i] * np.pi) * np.cos(freq * x_norm[i] * np.pi)
        
        # Cross-dimensional coupling with radial basis function and chaotic modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                coupling = np.exp(-0.5 * distance**2) * np.sin(5 * x_norm[i] * x_norm[j] * np.pi)
                cross_coupling += coupling
        
        # Chaotic perturbation using logistic map with sinusoidal modulation
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            logistic_input = 3.8 * (x_norm[i] + 0.2) % 1.0
            chaotic_perturbation += np.sin(logistic_input * 15 * np.pi) * np.cos(x_norm[i] * 8 * np.pi) * np.tanh(3 * x_norm[i])
        
        # Polynomial interaction terms with exponential decay - slightly modified
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(3 * x_norm[i] * x_norm[j] + 0.5)
        
        # Multimodal component with multiple sinusoidal peaks - slightly modified
        multimodal_component = 0.0
        for i in range(self.dim):
            multimodal_component += np.sin(7 * x_norm[i] * np.pi) * np.cos(4 * x_norm[i] * np.pi) * np.exp(-0.2 * x_norm[i]**2)
        
        # Additional chaotic cross-dimensional interaction with radial basis - increased complexity
        cross_dim_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim_chaos += np.sin(4 * x_norm[i] * x_norm[j]) * np.cos(3 * x_norm[i] * x_norm[j]) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine all components with adaptive weights - slightly adjusted
        return radial_component + 0.35 * harmonic_sum + 0.2 * cross_coupling + 0.25 * chaotic_perturbation + 0.15 * poly_interaction + 0.18 * multimodal_component + 0.12 * cross_dim_chaos