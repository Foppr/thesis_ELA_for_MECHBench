import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using chaotic sine-cosine patterns with exponential modulation
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0)
            amp = 1.2 + 0.4 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3) * np.exp(-np.abs(x_scaled[i]))
        
        # Dynamic attractor fields with position-dependent strength and cross-dimensional coupling
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8) * 0.9
            center2 = np.cos(i * 0.6) * 0.7
            strength1 = 1.5 + 0.3 * np.sin(i * 0.9)
            strength2 = 1.2 + 0.2 * np.cos(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.7)
        
        # Dimensionally adaptive complexity with long-range interaction terms and non-linear coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Increased non-linearity in weighting
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-np.abs(x_scaled[i] - x_scaled[j]))
        
        # Multi-scale fractal component with self-similar structure and enhanced decay
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Extended scales including 6
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i]) * 0.5)
        
        # Sharp transition regions with enhanced sigmoidal boundary effects and additional critical points
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.2)))  # Additional sharp transition
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.2)))  # Additional sharp transition
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Combined function with enhanced weighted components and additional non-linear terms
        return 1.0 * fractal + 1.5 * attractor + 0.8 * complexity + 0.7 * multiscale + 0.6 * sharpness