import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal component with increased complexity and modified interaction
        fractal = 0.0
        for i in range(self.dim):
            # Higher frequency and amplitude modulation with additional harmonics
            freq = 4.2 + 1.1 * np.sin(x_scaled[i] * 5.0)
            amp = 2.1 + 0.7 * np.cos(x_scaled[i] * 4.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8) * \
                      np.sin(0.5 * freq * x_scaled[i]**2)
        
        # Dynamic attractor fields with position-dependent strength and increased complexity
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths, positions, and interaction
            center1 = np.sin(i * 0.7) * 1.05
            center2 = np.cos(i * 0.5) * 0.85
            center3 = np.sin(i * 0.9) * 0.65
            strength1 = 1.5 + 0.4 * np.sin(i * 1.0)
            strength2 = 1.2 + 0.3 * np.cos(i * 0.6)
            strength3 = 0.9 + 0.2 * np.sin(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Dimensionally adaptive complexity with recursive interaction terms and modified weights
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased interaction range
                # Adaptive interaction based on dimensionality - increased weight and complexity
                weight = 3.0 / (1.0 + np.abs(i - j)**1.5)  # Further increased weight and non-linearity
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.7 * (x_scaled[i] + x_scaled[j])**2) * \
                             np.cos(0.3 * (x_scaled[i] - x_scaled[j])**2)
        
        # Multi-scale fractal component with self-similar structure and modified frequencies
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6, 8]:  # Added more scales and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.4 * scale * x_scaled[i]) * \
                             np.cos(0.2 * scale * x_scaled[i]**2)
        
        # Sharp transition regions with sigmoidal boundary effects - further increased sharpness
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points - even higher steepness and more transitions
            sig1 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i])))  # Additional transition
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.2)))  # New transition
            sig5 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.2)))  # New transition
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + \
                        (sig4 - 0.5)**2 + (sig5 - 0.5)**2
        
        # Combined function with modified weighted components for better algorithm discrimination
        return 1.1 * fractal + 1.8 * attractor + 0.9 * complexity + 0.9 * multiscale + 0.7 * sharpness