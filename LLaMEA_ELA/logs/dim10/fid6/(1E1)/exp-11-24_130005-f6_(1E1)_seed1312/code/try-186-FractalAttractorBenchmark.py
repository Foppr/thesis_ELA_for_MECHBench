import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with chaotic sine-cosine patterns and exponential modulation
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0)
            amp = 2.0 + 0.8 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3) * np.exp(-np.abs(x_scaled[i]))
        
        # Chaotic attractor fields with multiple centers and exponential decay
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8) * 1.2
            center2 = np.cos(i * 0.6) * 0.9
            center3 = np.tan(i * 0.4) * 0.7
            strength1 = 1.5 + 0.5 * np.sin(i * 0.9)
            strength2 = 1.2 + 0.3 * np.cos(i * 0.5)
            strength3 = 0.9 + 0.4 * np.tan(i * 0.3)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.3) + strength3 * np.exp(-dist3 * 0.7)
        
        # High-dimensional complexity with exponentially weighted interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 2.0 / (1.0 + np.exp(2.0 * np.abs(i - j)))  # Exponentially weighted interactions
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multi-scale fractal with chaotic frequency modulation and enhanced interference
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Added scale 6 and changed frequencies
            for i in range(self.dim):
                freq_mod = 1.0 + 0.5 * np.sin(scale * x_scaled[i])
                multiscale += freq_mod * np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i]))
        
        # Extreme sharp transition regions with multi-sigmoidal boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.2)))  # Added third sharp transition
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.2)))  # Added third sharp transition
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**3 + (sig4 - 0.5)**3
        
        # Combined function with enhanced weighted components and chaotic modulation
        return 1.2 * fractal + 1.8 * attractor + 0.8 * complexity + 0.7 * multiscale + 0.6 * sharpness