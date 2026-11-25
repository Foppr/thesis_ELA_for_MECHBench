import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using chaotic sine-cosine patterns with higher dimensionality coupling
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 0.8 * np.sin(x_scaled[i] * 4.0)
            amp = 1.5 + 0.5 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Enhanced dynamic attractor fields with multiple centers and position-dependent strength
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8) * 0.9
            center2 = np.cos(i * 0.6) * 0.7
            center3 = np.sin(i * 0.4) * 0.5
            strength1 = 1.2 + 0.3 * np.sin(i * 0.9)
            strength2 = 1.0 + 0.2 * np.cos(i * 0.5)
            strength3 = 0.8 + 0.1 * np.sin(i * 0.3)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Increased dimensionally adaptive complexity with higher-order interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Increased weight and modified decay
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(x_scaled[i] * x_scaled[j])
        
        # Multi-scale fractal component with additional frequency harmonics
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Added new scale values and increased complexity
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * x_scaled[i] * 0.5)
        
        # Sharp transition regions with enhanced sigmoidal boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.2)))  # Additional sharp transition
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2
        
        # Cross-dimensional coupling and interaction terms for increased complexity
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j < self.dim:  # Conditional coupling based on dimension indices
                    cross_coupling += np.sin(x_scaled[i] * x_scaled[j]) * \
                                    np.cos(x_scaled[i] + x_scaled[j]) * \
                                    (1.0 / (1.0 + np.abs(i - j)**0.5))
        
        # Combined function with increased weights and new interaction terms
        return 0.9 * fractal + 1.5 * attractor + 0.7 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * cross_coupling