import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with chaotic sine-cosine patterns and nested recursion
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic fractal pattern with recursive feedback loops
            freq = 3.0 + 2.0 * np.sin(x_scaled[i] * 5.0) + 0.5 * np.cos(x_scaled[i] * 7.0)
            amp = 1.5 + 0.8 * np.sin(x_scaled[i] * 4.0) + 0.3 * np.cos(x_scaled[i] * 6.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3) * \
                      np.exp(-0.5 * np.abs(x_scaled[i]))
        
        # Multi-attractor field with chaotic center positions and time-varying strengths
        attractor = 0.0
        for i in range(self.dim):
            # Chaotic attractor centers with sinusoidal position variations
            center1 = np.sin(i * 0.8 + x_scaled[i] * 2.0) * 0.9
            center2 = np.cos(i * 0.6 + x_scaled[i] * 3.0) * 0.7
            center3 = np.sin(i * 1.2 + x_scaled[i] * 4.0) * 0.5
            
            strength1 = 1.2 + 0.4 * np.sin(i * 0.9 + x_scaled[i] * 1.5)
            strength2 = 0.9 + 0.3 * np.cos(i * 0.7 + x_scaled[i] * 2.5)
            strength3 = 0.7 + 0.2 * np.sin(i * 1.1 + x_scaled[i] * 3.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # High-dimensional complexity with chaotic interaction terms and nested coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Chaotic adaptive weights based on position and dimension
                weight = 2.0 / (1.0 + np.abs(i - j) + 0.1 * np.sin(x_scaled[i] + x_scaled[j]))
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.3 * np.abs(x_scaled[i] - x_scaled[j]))
        
        # Multi-scale fractal with chaotic frequency modulation and nested self-similarity
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Added more scales and increased max scale
            for i in range(self.dim):
                # Chaotic frequency modulation based on position
                mod_freq = 1.0 + 0.5 * np.sin(x_scaled[i] * scale * 2.0)
                multiscale += mod_freq * np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i]))
        
        # Extreme sharp transition regions with chaotic sigmoidal boundaries and multiple critical points
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple chaotic sigmoidal transitions with varying steepness
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.2)))  # Additional sharp transition
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.2)))  # Additional sharp transition
            
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Chaos injection with deterministic chaos component
        chaos = 0.0
        for i in range(self.dim):
            # Logistic map inspired chaotic component
            chaos += np.sin(10.0 * x_scaled[i]) * np.cos(15.0 * x_scaled[i]) * \
                    np.exp(-2.0 * np.abs(x_scaled[i]))
        
        # Combined function with enhanced weighted components and chaotic mixing
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.7 * multiscale + 0.5 * sharpness + 0.3 * chaos