import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal component with chaotic sine-cosine combinations and increased frequency modulation
        fractal = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.2 * np.sin(x_scaled[i] * 5.0)
            amp = 2.0 + 0.6 * np.cos(x_scaled[i] * 4.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8) * \
                      np.exp(-0.5 * x_scaled[i]**2)
        
        # Modified attractor fields with dynamic center positions and interaction weights
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.7) * 0.8
            center2 = np.cos(i * 0.5) * 0.6
            center3 = np.sin(i * 0.9) * 0.4
            strength1 = 1.5 + 0.4 * np.sin(i * 1.1)
            strength2 = 1.0 + 0.3 * np.cos(i * 0.6)
            strength3 = 0.8 + 0.2 * np.sin(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 2.0) + strength2 * np.exp(-dist2 * 1.5) + strength3 * np.exp(-dist3 * 1.8)
        
        # Increased complexity with higher-order interaction terms and dimensionally adaptive weights
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                weight = 3.0 / (1.0 + np.abs(i - j)**1.5)  # Modified weight decay
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.7 * (x_scaled[i] + x_scaled[j])**2) * \
                             np.cos(0.3 * (x_scaled[i] - x_scaled[j])**2)
        
        # Multi-scale fractal with self-similar structure and modified amplitude decay
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6]:  # Added more scales and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.4 * scale * x_scaled[i]) * \
                             (1.0 + 0.2 * np.sin(scale * x_scaled[i]))
        
        # Enhanced sharp transition regions with multiple sigmoidal boundaries and increased steepness
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple sigmoidal transitions with varying steepness and positions
            sig1 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i] - 0.3)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i] + 0.3)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i])))  # Additional transition
            sig4 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.6)))  # New transition point
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Combined function with refined weighted components for improved algorithm discrimination
        return 1.0 * fractal + 1.8 * attractor + 0.7 * complexity + 0.7 * multiscale + 0.6 * sharpness