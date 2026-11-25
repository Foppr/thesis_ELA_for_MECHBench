import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using chaotic sine-cosine patterns with higher complexity
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic fractal pattern with non-linear frequency modulation and multi-harmonic components
            freq = 3.0 + 2.0 * np.sin(x_scaled[i] * 4.0) + 0.5 * np.cos(x_scaled[i] * 7.0)
            amp = 1.5 + 0.8 * np.sin(x_scaled[i] * 3.0) + 0.3 * np.cos(x_scaled[i] * 5.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3) * \
                      (1.0 + 0.2 * np.sin(x_scaled[i] * 11.0))
        
        # Enhanced dynamic attractor fields with multiple centers and time-varying strengths
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths, positions, and temporal dependencies
            center1 = np.sin(i * 0.8) * 0.9 + 0.1 * np.cos(i * 0.3)
            center2 = np.cos(i * 0.5) * 0.7 + 0.2 * np.sin(i * 0.4)
            center3 = np.sin(i * 0.2) * 0.6 + 0.15 * np.cos(i * 0.6)
            
            strength1 = 1.2 + 0.3 * np.sin(i * 0.9)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.7)
            strength3 = 0.8 + 0.15 * np.sin(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # High-dimensional complex interaction terms with non-local dependencies and cross-terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                # Complex interaction based on dimensionality with additional nonlinear coupling
                weight = 2.0 / (1.0 + np.abs(i - j) + 0.1 * np.sin(i * 0.5))  # Increased weight and added sine modulation
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             (1.0 + 0.2 * np.sin(x_scaled[i] * x_scaled[j]))
        
        # Multi-scale fractal component with exponential decay and irregular frequency patterns
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Extended scales with irregular spacing
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             (1.0 + 0.1 * np.sin(scale * x_scaled[i] * 2.0))
        
        # Sharp transition regions with enhanced sigmoidal boundary effects and chaotic thresholds
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points with chaotic threshold modulation
            threshold1 = 0.3 + 0.1 * np.sin(i * 0.4)
            threshold2 = -0.3 + 0.1 * np.cos(i * 0.6)
            
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - threshold1)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - threshold2)))  # Increased steepness
            
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3  # Cubic sharpness for more challenging optimization
        
        # Add chaotic noise component to make landscape highly irregular and non-smooth
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.1 * np.sin(x_scaled[i] * 20.0) * np.cos(x_scaled[i] * 15.0) + \
                     0.05 * np.sin(x_scaled[i] * 30.0)
        
        # Combined function with enhanced weighted components and chaotic modulation
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.2 * chaos