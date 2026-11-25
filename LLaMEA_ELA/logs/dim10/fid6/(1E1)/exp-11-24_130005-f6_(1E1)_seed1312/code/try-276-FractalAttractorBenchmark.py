import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with enhanced recursive patterns
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 0.8 * np.sin(x_scaled[i] * 2.5)
            amp = 1.2 + 0.4 * np.cos(x_scaled[i] * 1.5)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3)
        
        # Enhanced attractor fields with dynamic positioning
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.4) * 0.9
            center2 = np.cos(i * 0.6) * 0.7
            strength1 = 1.2 + 0.3 * np.sin(i * 0.8)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.8) + strength2 * np.exp(-dist2 * 0.6)
        
        # Increased interaction complexity with higher-order terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                weight = 2.0 / (1.0 + np.abs(i - j) * 0.5)  # Increased weight
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(x_scaled[i] * x_scaled[j])
        
        # Enhanced multi-scale fractal with additional frequency components
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Added scale 5 and modified others
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.6) * \
                             np.exp(-scale * np.abs(x_scaled[i]) * 0.5)
        
        # Sharper transition regions with additional boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.25)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.25)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] - 0.4)))   # Additional transition
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2
        
        # Combined function with modified weights for better discrimination
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.6 * multiscale + 0.5 * sharpness