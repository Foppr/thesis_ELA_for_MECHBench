import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using recursive sine-cosine patterns with increased complexity
        fractal = 0.0
        for i in range(self.dim):
            # Enhanced fractal pattern with higher frequency components and dynamic amplitude
            freq1 = 3.0 + 1.0 * np.sin(x_scaled[i] * 4.0)
            freq2 = 2.5 + 0.8 * np.cos(x_scaled[i] * 3.0)
            amp1 = 1.2 + 0.4 * np.sin(x_scaled[i] * 2.0)
            amp2 = 0.8 + 0.3 * np.cos(x_scaled[i] * 1.5)
            fractal += amp1 * np.sin(freq1 * x_scaled[i]) * np.cos(freq2 * x_scaled[i] * 0.7) + \
                      amp2 * np.cos(freq1 * x_scaled[i] * 0.8) * np.sin(freq2 * x_scaled[i])
        
        # Dynamic attractor fields with position-dependent strength and increased complexity
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths, positions, and interaction terms
            center1 = np.sin(i * 0.6) * 0.9
            center2 = np.cos(i * 0.4) * 0.7
            center3 = np.tan(i * 0.3) * 0.5
            
            strength1 = 1.2 + 0.3 * np.sin(i * 0.8)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.5)
            strength3 = 0.7 + 0.1 * np.sin(i * 0.6)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 2.0) + \
                        strength2 * np.exp(-dist2 * 1.5) + \
                        strength3 * np.exp(-dist3 * 1.8)
        
        # Dimensionally adaptive complexity with increased interaction terms and weights
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Enhanced interaction with more complex weighting function
                weight = 2.0 / (1.0 + np.abs(i - j) * 0.5)
                complex_term = np.sin(x_scaled[i] + x_scaled[j]) * \
                              np.cos(x_scaled[i] - x_scaled[j]) * \
                              np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                complexity += weight * complex_term
        
        # Multi-scale fractal component with additional frequency components and modified structure
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Added scale 5 and increased scale values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.6) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             (1.0 + 0.2 * np.sin(scale * x_scaled[i] * 2.0))
        
        # Sharp transition regions with enhanced sigmoidal boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            # Enhanced sigmoidal transitions with multiple critical points and increased steepness
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-15.0 * (x_scaled[i] - 0.2)))  # Additional transition
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2
        
        # Combined function with adjusted weights for improved landscape characteristics
        return 0.8 * fractal + 1.5 * attractor + 0.7 * complexity + 0.6 * multiscale + 0.5 * sharpness