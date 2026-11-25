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
            amp = 1.2 + 0.5 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * \
                      np.exp(-0.5 * np.abs(x_scaled[i]))
        
        # Dynamic attractor fields with chaotic center positions and multi-scale attraction
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8 + 1.0) * 0.9
            center2 = np.cos(i * 0.6 + 0.5) * 0.7
            strength1 = 1.5 + 0.3 * np.sin(i * 0.9)
            strength2 = 1.0 + 0.2 * np.cos(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.3)
        
        # Enhanced complexity with chaotic cross-terms and higher-order interactions
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Exponential weight decay
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multi-scale fractal with chaotic frequency components and self-similar chaos
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Added scale 6 and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i] * 1.2) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * np.pi * x_scaled[i])
        
        # Chaotic sharp transition regions with multiple sigmoidal boundaries
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] - 0.2)))  # Additional boundary
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**2
        
        # Chaotic coupling between components with non-linear mixing
        chaotic_mix = 0.0
        for i in range(self.dim):
            chaotic_mix += np.sin(x_scaled[i] * 7.0) * \
                          np.cos(x_scaled[i] * 5.0) * \
                          np.exp(-x_scaled[i]**4)
        
        # Combined function with enhanced chaotic weights and exponential scaling
        return 1.2 * fractal + 1.8 * attractor + 0.7 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * chaotic_mix