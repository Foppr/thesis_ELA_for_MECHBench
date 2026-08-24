import numpy as np

class ChaoticSinusoidalBasisBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple sinusoidal modulations and chaotic perturbations
        r = np.sqrt(np.sum(x_norm**2))
        radial_component = np.exp(-0.3 * r**2) * np.sin(3 * np.pi * r) * np.cos(2 * np.pi * r) * (1 + 0.4 * np.sin(17 * r * np.pi))
        
        # Multi-sinusoidal harmonic terms with increased frequency diversity and amplitude decay
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 3**(i % 5 + 1)
            amplitude = 1.0 / (1.0 + 0.15 * i**1.5)
            harmonic_sum += amplitude * np.sin(freq * x_norm[i] * np.pi) * np.cos(freq * x_norm[i] * np.pi) * np.tanh(2 * x_norm[i])
        
        # Enhanced cross-dimensional coupling with multiple radial basis functions and chaotic modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                coupling = np.exp(-0.4 * distance**2) * np.sin(7 * x_norm[i] * x_norm[j] * np.pi) * np.cos(4 * x_norm[i] * x_norm[j] * np.pi)
                cross_coupling += coupling
        
        # Stronger chaotic perturbation using multiple logistic maps with complex sinusoidal modulation
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            logistic_input1 = 3.9 * (x_norm[i] + 0.15) % 1.0
            logistic_input2 = 3.7 * (x_norm[i] - 0.2) % 1.0
            chaotic_perturbation += (np.sin(logistic_input1 * 20 * np.pi) * np.cos(logistic_input2 * 15 * np.pi) * 
                                   np.sin(x_norm[i] * 10 * np.pi) * np.cos(x_norm[i] * 7 * np.pi)) * np.tanh(4 * x_norm[i])
        
        # Complex polynomial interaction terms with higher-order exponents and exponential decay
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**4 + x_norm[j]**4) * np.exp(-0.4 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(4 * x_norm[i] * x_norm[j] + 0.7)
        
        # Enhanced multimodal component with multiple overlapping peaks and increased complexity
        multimodal_component = 0.0
        for i in range(self.dim):
            multimodal_component += (np.sin(9 * x_norm[i] * np.pi) * np.cos(5 * x_norm[i] * np.pi) * 
                                   np.sin(3 * x_norm[i] * np.pi) * np.cos(2 * x_norm[i] * np.pi)) * np.exp(-0.3 * x_norm[i]**2)
        
        # Advanced cross-dimensional chaotic interaction with multiple trigonometric components
        cross_dim_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim_chaos += (np.sin(5 * x_norm[i] * x_norm[j]) * np.cos(6 * x_norm[i] * x_norm[j]) * 
                                  np.sin(3 * x_norm[i] * x_norm[j]) * np.cos(2 * x_norm[i] * x_norm[j])) * np.exp(-0.6 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Additional high-frequency oscillatory component
        high_freq_component = 0.0
        for i in range(self.dim):
            high_freq_component += np.sin(15 * x_norm[i] * np.pi) * np.cos(12 * x_norm[i] * np.pi) * np.exp(-0.1 * x_norm[i]**2)
        
        # Combine all components with adjusted weights for increased complexity
        return (0.8 * radial_component + 0.4 * harmonic_sum + 0.3 * cross_coupling + 
                0.35 * chaotic_perturbation + 0.25 * poly_interaction + 0.2 * multimodal_component + 
                0.15 * cross_dim_chaos + 0.1 * high_freq_component)