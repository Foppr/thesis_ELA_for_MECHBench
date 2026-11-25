import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using recursive sine-cosine patterns
        fractal = 0.0
        for i in range(self.dim):
            # Recursive fractal pattern with varying frequency and amplitude
            freq = 2.5 + 0.7 * np.sin(x_scaled[i] * 3.5)
            amp = 1.2 + 0.4 * np.cos(x_scaled[i] * 2.5)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Dynamic attractor fields with position-dependent strength
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths and positions
            center1 = np.sin(i * 0.6) * 0.9
            center2 = np.cos(i * 0.4) * 0.7
            strength1 = 1.2 + 0.3 * np.sin(i * 0.8)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2)
        
        # Dimensionally adaptive complexity with recursive interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Adaptive interaction based on dimensionality - modified weights
                weight = 2.0 / (1.0 + np.abs(i - j))  # Increased weight
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j])
        
        # Multi-scale fractal component with self-similar structure - modified frequencies
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Changed scale values and added 5
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i]))
        
        # Sharp transition regions with sigmoidal boundary effects - increased sharpness
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points - increased steepness
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.3)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.3)))  # Increased steepness
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2
        
        # Combined function with modified weighted components
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.6 * multiscale + 0.5 * sharpness