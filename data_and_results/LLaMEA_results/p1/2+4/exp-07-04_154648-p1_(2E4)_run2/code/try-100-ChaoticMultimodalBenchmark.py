import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.harmonic_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.harmonic_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.saddle_points = np.random.uniform(-5.0, 5.0, (10, dim))
        self.time_variant_phase = np.random.uniform(0, 2*np.pi, dim)
        self.noise_level = 0.05
        
    def f(self, x):
        x_norm = x / 5.0
        t = np.sum(x_norm) % 1.0  # Time-like parameter
        
        # Time-variant harmonic components
        harmonic = 0.0
        for i in range(self.dim):
            phase = self.time_variant_phase[i] + t * 0.5
            harmonic += (self.harmonic_amplitudes[i] * 
                        np.sin(self.harmonic_frequencies[i] * x_norm[i] + phase) * 
                        np.cos(self.harmonic_frequencies[i] * x_norm[i] * 0.7 + phase))
        
        # Saddle-point potential fields
        saddle_potential = 0.0
        for i in range(10):
            diff = x_norm - self.saddle_points[i]
            distance = np.sqrt(np.sum(diff**2))
            # Create saddle-like structure with repulsive and attractive regions
            saddle_potential += 1.0 / (1.0 + distance**2) * np.sin(distance * 2.0)
        
        # Chaotic gradient components
        chaotic_grad = 0.0
        for i in range(self.dim):
            chaotic_grad += (np.sin(x_norm[i] * 7.0) * 
                           np.cos(x_norm[i] * 3.0) * 
                           np.tan(x_norm[i] * 1.5))
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += (np.sin(x_norm[i] * x_norm[i+1] * 3.0) * 
                             np.cos(x_norm[i] + x_norm[i+1]) * 
                             np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2))
        
        # Polynomial and noise components
        poly_term = 0.02 * np.sum(x_norm**4)
        noise = self.noise_level * np.random.uniform(-1, 1)
        
        # Global minimum at origin with chaotic penalty
        penalty = 0.0
        for i in range(10):
            diff = x_norm - self.saddle_points[i]
            penalty += 1.0 / (1.0 + np.sum(diff**2))
        
        # Combine all components
        return harmonic + saddle_potential + chaotic_grad + cross_coupling + poly_term + noise + 0.3 * penalty