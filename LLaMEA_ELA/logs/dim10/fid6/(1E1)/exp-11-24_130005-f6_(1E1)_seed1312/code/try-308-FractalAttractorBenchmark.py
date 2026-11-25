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
            # Enhanced fractal pattern with increased frequency and amplitude modulation
            freq = 3.0 + 0.7 * np.sin(x_scaled[i] * 4.0)
            amp = 1.5 + 0.4 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Enhanced attractor fields with more complex position dependencies
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with non-linear strength variations
            center1 = np.sin(i * 0.6) * 0.9
            center2 = np.cos(i * 0.4) * 0.7
            center3 = np.tan(i * 0.3) * 0.5
            
            strength1 = 1.2 + 0.3 * np.sin(i * 0.8)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.5)
            strength3 = 0.7 + 0.1 * np.tan(i * 0.6)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Increased complexity with higher-order interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                for k in range(j+1, min(j+3, self.dim)):  # Added third-order interactions
                    weight = 2.0 / (1.0 + np.abs(i - j) + 0.5 * np.abs(j - k))
                    complexity += weight * np.sin(x_scaled[i] + x_scaled[j] + x_scaled[k]) * \
                                 np.cos(x_scaled[i] - x_scaled[j]) * \
                                 np.sin(x_scaled[j] - x_scaled[k])
        
        # Multi-scale fractal component with additional frequency harmonics
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Added more scales and changed to 5
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * x_scaled[i] * 0.3)
        
        # Enhanced sharp transition regions with more aggressive sigmoidal effects
        sharpness = 0.0
        for i in range(self.dim):
            # More aggressive sigmoidal transitions with multiple critical points
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.2)))  # Added third transition
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.2)))  # Added third transition
            
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Combined function with adjusted weights for improved balance
        return 0.8 * fractal + 1.5 * attractor + 0.7 * complexity + 0.6 * multiscale + 0.5 * sharpness