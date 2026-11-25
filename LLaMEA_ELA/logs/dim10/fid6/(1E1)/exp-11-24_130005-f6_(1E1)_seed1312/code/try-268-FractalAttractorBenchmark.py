import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using chaotic sine-cosine patterns with higher frequency
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0)
            amp = 1.2 + 0.4 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3)
        
        # Enhanced attractor fields with multiple centers and dynamic strengths
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8) * 0.9
            center2 = np.cos(i * 0.6) * 0.7
            center3 = np.tan(i * 0.4) * 0.5
            strength1 = 1.5 + 0.3 * np.sin(i * 0.9)
            strength2 = 1.2 + 0.2 * np.cos(i * 0.5)
            strength3 = 0.9 + 0.1 * np.tan(i * 0.3)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Increased complexity with higher-order interaction terms and cross-dimensional coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Increased non-linearity
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(x_scaled[i] * x_scaled[j])
        
        # Multi-scale fractal component with additional frequency harmonics and exponential decay
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Added new scale values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * x_scaled[i] * 0.5)
        
        # Enhanced sharp transition regions with multiple sigmoidal boundaries and increased steepness
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-18.0 * (x_scaled[i] - 0.2)))  # Additional boundary
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2
        
        # Additional chaotic coupling terms for increased landscape complexity
        chaos = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaos += np.sin(x_scaled[i] * x_scaled[i+1]) * \
                        np.cos(x_scaled[i] + x_scaled[i+1]) * \
                        np.exp(-np.abs(x_scaled[i] - x_scaled[i+1]))
        
        # Combined function with modified weighted components and increased non-linearity
        return 0.8 * fractal + 1.5 * attractor + 0.7 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * chaos