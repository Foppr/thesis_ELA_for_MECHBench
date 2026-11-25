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
            # Enhanced fractal pattern with higher frequency and amplitude modulation
            freq = 3.0 + 1.0 * np.sin(x_scaled[i] * 4.0)
            amp = 1.5 + 0.5 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * \
                      np.exp(-0.5 * np.abs(x_scaled[i]))
        
        # Chaotic attractor fields with dynamic positioning and strength
        attractor = 0.0
        for i in range(self.dim):
            # Multiple chaotic attractor centers with time-varying positions
            center1 = np.sin(i * 0.8 + x_scaled[i] * 0.3) * 0.9
            center2 = np.cos(i * 0.5 + x_scaled[i] * 0.4) * 0.7
            strength1 = 1.2 + 0.3 * np.sin(i * 0.9 + x_scaled[i] * 0.2)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.6 + x_scaled[i] * 0.3)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1 * 2.0) + strength2 * np.exp(-dist2 * 1.5)
        
        # High-dimensional complex interaction with exponential coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Exponential interaction weights and enhanced coupling
                weight = 2.0 / (1.0 + np.exp(2.0 * np.abs(i - j)))  # Stronger decay
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multi-scale fractal with ultra-high frequency components and complex self-similarity
        multiscale = 0.0
        for scale in [1, 2, 3, 6, 8]:  # Added more scales including 6 and 8
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * x_scaled[i] * 0.5)
        
        # Extreme sharp transition regions with ultra-high sigmoidal steepness
        sharpness = 0.0
        for i in range(self.dim):
            # Ultra-sharp sigmoidal transitions at multiple critical points
            sig1 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.2)))  # Additional sharp transition
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**2
        
        # Add chaotic noise component for additional difficulty
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(10.0 * x_scaled[i]) * np.cos(7.0 * x_scaled[i]) * \
                    np.exp(-x_scaled[i]**2)
        
        # Combined function with enhanced weighted components and additional chaotic influence
        return 1.0 * fractal + 1.5 * attractor + 0.8 * complexity + 0.7 * multiscale + 0.6 * sharpness + 0.3 * chaos