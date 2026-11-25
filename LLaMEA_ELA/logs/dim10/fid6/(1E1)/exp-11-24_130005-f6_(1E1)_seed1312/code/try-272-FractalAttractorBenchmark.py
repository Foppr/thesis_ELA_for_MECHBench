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
            # Enhanced fractal pattern with higher frequency components and modified amplitude
            freq1 = 3.0 + 0.8 * np.sin(x_scaled[i] * 4.0)
            freq2 = 1.5 + 0.6 * np.cos(x_scaled[i] * 2.5)
            amp1 = 1.2 + 0.4 * np.cos(x_scaled[i] * 3.0)
            amp2 = 0.8 + 0.3 * np.sin(x_scaled[i] * 1.5)
            fractal += amp1 * np.sin(freq1 * x_scaled[i]) * np.cos(freq2 * x_scaled[i] * 0.7) + \
                      amp2 * np.cos(freq1 * x_scaled[i] * 0.8) * np.sin(freq2 * x_scaled[i])
        
        # Enhanced attractor fields with more complex position-dependent strength
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths and positions - increased complexity
            center1 = np.sin(i * 0.6) * 0.9
            center2 = np.cos(i * 0.4) * 0.7
            center3 = np.tan(i * 0.3) * 0.5
            strength1 = 1.2 + 0.3 * np.sin(i * 0.8)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.5)
            strength3 = 0.7 + 0.1 * np.tan(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Enhanced dimensionally adaptive complexity with stronger interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Adaptive interaction based on dimensionality - increased weights and modified formula
                weight = 2.0 / (1.0 + np.abs(i - j))  # Increased weight
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multi-scale fractal component with additional frequency components
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Added scale 5 and modified existing scales
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * x_scaled[i] * 0.3)
        
        # Enhanced sharp transition regions with sigmoidal boundary effects - increased sharpness
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points - increased steepness and added more transitions
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-18.0 * (x_scaled[i] - 0.2)))  # Additional transition
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2
        
        # Combined function with reweighted components for better optimization challenge
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.6 * multiscale + 0.5 * sharpness