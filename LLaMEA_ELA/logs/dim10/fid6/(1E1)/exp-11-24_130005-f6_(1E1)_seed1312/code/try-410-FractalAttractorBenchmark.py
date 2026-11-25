import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with chaotic sine-cosine patterns and increased complexity
        fractal = 0.0
        for i in range(self.dim):
            freq = 4.2 + 1.1 * np.sin(x_scaled[i] * 5.2)
            amp = 2.1 + 0.7 * np.cos(x_scaled[i] * 4.1)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.85)
        
        # Dynamic attractor fields with enhanced multi-center interactions and increased complexity
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.75) * 1.1
            center2 = np.cos(i * 0.55) * 0.9
            center3 = np.sin(i * 0.95) * 0.7
            center4 = np.cos(i * 0.65) * 0.8
            strength1 = 1.5 + 0.4 * np.sin(i * 1.1)
            strength2 = 1.2 + 0.3 * np.cos(i * 0.7)
            strength3 = 0.9 + 0.2 * np.sin(i * 0.4)
            strength4 = 1.0 + 0.25 * np.cos(i * 0.8)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            dist4 = (x_scaled[i] - center4)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + \
                        strength3 * np.exp(-dist3) + strength4 * np.exp(-dist4)
        
        # Dimensionally adaptive complexity with recursive interaction terms and modified weights
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased interaction range further
                weight = 3.0 / (1.0 + np.abs(i - j)**1.5)  # Non-linear weight decay
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.8 * (x_scaled[i] + x_scaled[j])**2) * \
                             np.cos(0.6 * (x_scaled[i] - x_scaled[j])**3)
        
        # Multi-scale fractal component with self-similar structure and modified frequencies
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6, 8]:  # Added more scales and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.4 * scale * x_scaled[i]) * \
                             np.cos(0.3 * scale * x_scaled[i])
        
        # Sharp transition regions with sigmoidal boundary effects - even higher sharpness
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-40.0 * (x_scaled[i] - 0.5)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-40.0 * (x_scaled[i] + 0.5)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i])))  # Additional transition
            sig4 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i] - 0.2)))  # New transition
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Additional chaotic component with cross-dimensional coupling and fractal recursion
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(x_scaled[i] * 7.0) * np.cos(x_scaled[i] * 6.0) * \
                      np.exp(-np.abs(x_scaled[i])) * (1.0 + 0.5 * np.sin(3.0 * x_scaled[i]))
        
        # Combined function with modified weighted components for better algorithm discrimination
        return 1.2 * fractal + 1.8 * attractor + 0.9 * complexity + 0.9 * multiscale + \
               0.7 * sharpness + 0.8 * chaotic