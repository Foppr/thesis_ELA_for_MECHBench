import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with enhanced chaotic patterns
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 0.8 * np.sin(x_scaled[i] * 4.0)
            amp = 1.5 + 0.5 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * \
                      np.exp(-0.5 * np.abs(x_scaled[i]))
        
        # Enhanced attractor fields with non-linear coupling
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8) * 1.2
            center2 = np.cos(i * 0.6) * 0.9
            strength1 = 1.5 + 0.3 * np.sin(i * 0.9)
            strength2 = 1.2 + 0.2 * np.cos(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.3)
        
        # Increased interaction complexity with higher-order terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Non-linear weight decay
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.tanh(x_scaled[i] * x_scaled[j])
        
        # Multi-scale fractal with enhanced self-similarity and additional frequency bands
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Added scale 5 and changed others
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * np.pi * x_scaled[i])
        
        # Novel boundary regularization with enhanced sharpness and multiple transition zones
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple sigmoidal transitions at different points
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] - 0.7)))  # Additional transition
            sig4 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] + 0.7)))  # Additional transition
            
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Novel chaotic component with time-delayed feedback
        chaotic = 0.0
        for i in range(self.dim):
            if i > 0:
                # Time-delayed interaction
                chaotic += 0.8 * np.sin(x_scaled[i] + 0.3 * x_scaled[i-1]) * \
                          np.cos(2.0 * x_scaled[i])
            else:
                chaotic += 0.8 * np.sin(x_scaled[i]) * np.cos(2.0 * x_scaled[i])
        
        # Combined function with new weighted components and additional regularization
        return 1.2 * fractal + 1.8 * attractor + 0.7 * complexity + 0.6 * multiscale + \
               0.5 * sharpness + 0.3 * chaotic