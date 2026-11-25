import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with enhanced recursive patterns and chaotic elements
        fractal = 0.0
        for i in range(self.dim):
            # Enhanced fractal pattern with chaotic modulation
            freq = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0)
            amp = 1.5 + 0.5 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * \
                      (1.0 + 0.3 * np.sin(x_scaled[i] * 10.0))
        
        # Complex multi-attractor fields with dynamic positioning and varying strengths
        attractor = 0.0
        for i in range(self.dim):
            # Multiple dynamically positioned attractors with time-varying strengths
            center1 = np.sin(i * 0.8) * 0.9 + 0.1 * np.cos(x_scaled[i] * 2.0)
            center2 = np.cos(i * 0.5) * 0.7 + 0.2 * np.sin(x_scaled[i] * 3.0)
            center3 = np.sin(i * 0.3) * 0.6 + 0.15 * np.cos(x_scaled[i] * 5.0)
            
            strength1 = 1.2 + 0.4 * np.sin(i * 0.9)
            strength2 = 0.9 + 0.3 * np.cos(i * 0.6)
            strength3 = 0.7 + 0.2 * np.sin(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Enhanced dimensionally adaptive complexity with higher-order interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                for k in range(j+1, min(j+3, self.dim)):  # Added third-order interactions
                    weight = 2.0 / (1.0 + np.abs(i - j) + 0.5 * np.abs(j - k))
                    complexity += weight * np.sin(x_scaled[i] + x_scaled[j] + x_scaled[k]) * \
                                 np.cos(x_scaled[i] - x_scaled[j]) * \
                                 np.sin(x_scaled[j] - x_scaled[k])
        
        # Multi-scale fractal component with additional chaotic frequency modulation
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Added scale 6 and changed existing scales
            for i in range(self.dim):
                freq_mod = 1.0 + 0.4 * np.sin(x_scaled[i] * scale * 2.0)
                multiscale += freq_mod * np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i]))
        
        # Chaotic transition regions with enhanced sharpness and multiple boundaries
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple sigmoidal transitions with varying steepness and positions
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] - 0.2)))  # Different steepness
            sig4 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] + 0.2)))  # Different steepness
            
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Novel chaotic component with cross-dimensional coupling and exponential decay
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-dimensional chaotic interaction with exponential weighting
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = np.exp(-dist * 3.0) + 0.1 * np.sin(dist * 10.0)
                chaotic += weight * np.sin(x_scaled[i] * x_scaled[j] * 5.0) * \
                          np.cos(x_scaled[i] * x_scaled[j] * 2.0)
        
        # Combined function with reweighted components and added chaos
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * chaotic