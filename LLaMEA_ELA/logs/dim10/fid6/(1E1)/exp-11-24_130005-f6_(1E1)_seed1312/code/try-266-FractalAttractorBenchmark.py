import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using recursive sine-cosine patterns with chaotic modulation
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic modulation of frequency and amplitude with higher dimensional coupling
            freq = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0 + i * 0.3)
            amp = 1.5 + 0.5 * np.cos(x_scaled[i] * 3.0 + i * 0.2)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * \
                      np.exp(-0.5 * (x_scaled[i] - np.sin(i * 0.4))**2)
        
        # Dynamic attractor fields with position-dependent strength and multi-modal centers
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths, positions, and interaction terms
            center1 = np.sin(i * 0.8) * 0.9 + 0.1 * np.cos(i * 0.3)
            center2 = np.cos(i * 0.6) * 0.7 + 0.2 * np.sin(i * 0.5)
            center3 = 0.5 * np.sin(i * 0.4) * np.cos(i * 0.2)
            
            strength1 = 1.2 + 0.3 * np.sin(i * 0.9)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.6)
            strength3 = 0.7 + 0.1 * np.sin(i * 0.8)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Dimensionally adaptive complexity with recursive interaction terms and cross-dimensional coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Adaptive interaction based on dimensionality - modified weights with exponential decay
                weight = 2.0 / (1.0 + np.abs(i - j) + 0.1 * np.sin(i * 0.5))  
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.1 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multi-scale fractal component with self-similar structure and additional frequency harmonics
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Increased scale values and added 6
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * np.cos(x_scaled[i]))
        
        # Sharp transition regions with sigmoidal boundary effects - increased sharpness and additional critical points
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near multiple critical points - increased steepness and added complexity
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-10.0 * (x_scaled[i] - 0.2)))  # Additional critical point
            sig4 = 1.0 / (1.0 + np.exp(-10.0 * (x_scaled[i] + 0.2)))  # Additional critical point
            
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Cross-dimensional interaction terms with polynomial and trigonometric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_scaled[i] * x_scaled[j]) * \
                             np.cos(x_scaled[i] + x_scaled[j]) * \
                             (x_scaled[i]**2 + x_scaled[j]**2)
        
        # Combined function with modified weighted components and enhanced non-linearity
        return 0.8 * fractal + 1.5 * attractor + 0.7 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * cross_term