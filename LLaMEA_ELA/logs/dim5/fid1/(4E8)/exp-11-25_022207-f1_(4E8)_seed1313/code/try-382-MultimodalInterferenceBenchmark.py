import numpy as np

class MultimodalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Adaptive conditioning parameters with exponential scaling
        self.conditioning_factors = np.exp(np.linspace(0.5, 3.5, min(12, dim))) * 2.0
        # Periodic sinusoidal frequencies with irregular spacing
        self.sinusoidal_frequencies = np.logspace(0.8, 2.8, min(10, dim)) * 1.2
        # Interference pattern strengths for complex optima clustering
        self.interference_strengths = np.random.uniform(0.5, 2.5, min(8, dim)) * 1.3
        # Dynamic phase shifts for enhanced complexity
        self.phase_shifts = np.linspace(0.1, 1.9, min(9, dim)) * np.pi
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Adaptive conditioning with exponential scaling and dynamic gradients
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            factor = self.conditioning_factors[i]
            # Exponential conditioning with higher-order polynomial terms
            cond_val = factor * (x_norm[i] ** 2) + 0.6 * (x_norm[i] ** 3) + 0.15 * (x_norm[i] ** 5) + 0.03 * (x_norm[i] ** 7)
            conditioning_term += cond_val
            
        # Periodic sinusoidal components with varying frequencies and amplitudes
        sinusoidal_term = 0.0
        for i in range(min(len(self.sinusoidal_frequencies), self.dim)):
            freq = self.sinusoidal_frequencies[i]
            # Multi-frequency sinusoidal interaction with phase modulation
            sin_val = 0.4 * np.sin(freq * x_norm[i]) + 0.25 * np.sin(2 * freq * x_norm[i]) + 0.1 * np.sin(3 * freq * x_norm[i])
            sinusoidal_term += sin_val
            
        # Cross-dimensional interference patterns with complex coupling
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Complex interference with phase shifts and adaptive coupling
                phase_diff = x_norm[i] * np.cos(self.phase_shifts[i % len(self.phase_shifts)]) - x_norm[j] * np.sin(self.phase_shifts[j % len(self.phase_shifts)])
                interference_val = self.interference_strengths[i % len(self.interference_strengths)] * np.sin(5.0 * phase_diff) * np.cos(3.0 * phase_diff)
                interference_term += interference_val
                
        # Multi-scale optima clustering with irregular spacing and varying depths
        cluster_term = 0.0
        for i in range(self.dim):
            # Clustering with variable distances and polynomial minima shapes
            cluster_pos = 2.5 * np.cos(0.5 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - cluster_pos
            cluster_val = 1.2 * (distance ** 3) + 0.8 * (distance ** 5) + 0.3 * (distance ** 7) + 0.09 * (distance ** 9)
            cluster_term += cluster_val
            
        # Combined terms with adjusted weights for optimal benchmarking difficulty
        result = 0.85 * conditioning_term + 0.7 * sinusoidal_term + 0.6 * interference_term + 0.5 * cluster_term
        
        # Add dynamic noise with amplitude scaling based on dimensionality and problem complexity
        noise_amplitude = 0.035 * (1.0 + 0.08 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise