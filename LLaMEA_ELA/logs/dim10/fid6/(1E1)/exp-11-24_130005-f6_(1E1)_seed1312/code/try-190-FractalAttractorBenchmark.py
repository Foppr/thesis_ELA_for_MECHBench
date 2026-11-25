import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with enhanced chaotic behavior
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0)
            amp = 1.5 + 0.8 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * \
                      np.tanh(2.0 * x_scaled[i])
        
        # Dynamic attractor fields with position-dependent strength and multiple centers
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8) * 0.9
            center2 = np.cos(i * 0.5) * 0.7
            center3 = np.tan(i * 0.3) * 0.5
            strength1 = 1.2 + 0.3 * np.sin(i * 0.9)
            strength2 = 1.0 + 0.2 * np.cos(i * 0.6)
            strength3 = 0.9 + 0.1 * np.sin(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Dimensionally adaptive complexity with higher-order interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Non-linear weight decay
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.tanh(x_scaled[i] * x_scaled[j])
        
        # Multi-scale fractal component with enhanced self-similarity and decaying amplitudes
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Added new scale values and increased range
            for i in range(self.dim):
                multiscale += (1.0 / scale) * np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sinh(0.5 * x_scaled[i])
        
        # Sharp transition regions with multiple sigmoidal boundaries and enhanced non-linearity
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] - 0.2)))  # Different steepness
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**2
        
        # Additional chaotic component with exponential decay and cross-terms
        chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i+j < self.dim:  # Ensure indices are valid
                    chaos += np.exp(-np.abs(x_scaled[i] - x_scaled[j])) * \
                            np.sin(x_scaled[i] * x_scaled[j]) * \
                            np.cos(x_scaled[i] + x_scaled[j])
        
        # Combined function with modified weighted components and additional complexity
        return 0.8 * fractal + 1.5 * attractor + 0.7 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * chaos