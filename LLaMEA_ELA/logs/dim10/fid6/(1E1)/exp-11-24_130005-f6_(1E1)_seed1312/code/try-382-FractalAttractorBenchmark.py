import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal component with increased complexity and modified interactions
        fractal = 0.0
        for i in range(self.dim):
            # Higher frequency modulation with additional sine-cosine combinations
            freq1 = 4.2 + 1.1 * np.sin(x_scaled[i] * 5.0)
            freq2 = 2.8 + 0.7 * np.cos(x_scaled[i] * 3.0)
            amp1 = 2.1 + 0.6 * np.sin(x_scaled[i] * 2.5)
            amp2 = 1.4 + 0.4 * np.cos(x_scaled[i] * 4.0)
            fractal += amp1 * np.sin(freq1 * x_scaled[i]) * np.cos(freq2 * x_scaled[i] * 0.6) + \
                      amp2 * np.cos(freq1 * x_scaled[i] * 0.8) * np.sin(freq2 * x_scaled[i])
        
        # Complex attractor fields with dynamic center positions and multi-scale interactions
        attractor = 0.0
        for i in range(self.dim):
            # Multiple dynamic attractor centers with time-varying strengths and positions
            center1 = np.sin(i * 0.7) * 0.9 + 0.1 * np.cos(x_scaled[i] * 2.0)
            center2 = np.cos(i * 0.5) * 0.7 + 0.15 * np.sin(x_scaled[i] * 1.5)
            center3 = np.sin(i * 0.9) * 0.5 + 0.1 * np.cos(x_scaled[i] * 3.0)
            strength1 = 1.5 + 0.4 * np.sin(i * 1.1)
            strength2 = 1.2 + 0.3 * np.cos(i * 0.8)
            strength3 = 0.9 + 0.2 * np.sin(i * 0.6)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.7) + strength3 * np.exp(-dist3 * 0.9)
        
        # Increased dimensional interaction complexity with higher-order terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended interaction range
                weight = 3.0 / (1.0 + np.abs(i - j)**1.5)  # Increased weight with power scaling
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.8 * (x_scaled[i] + x_scaled[j])**2) * \
                             np.cos(0.5 * (x_scaled[i] - x_scaled[j])**3)
        
        # Multi-scale fractal with self-similar structure and additional frequency components
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6, 8]:  # Added more scales and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.4 * scale * x_scaled[i]) * \
                             np.cos(0.3 * scale * x_scaled[i]**2)
        
        # Enhanced sharp transition regions with multiple sigmoidal boundaries and increased steepness
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple sigmoidal transitions with varying steepness and positions
            sig1 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i] - 0.3)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i] + 0.3)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i])))  # Additional transition
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.6)))  # New transition
            sig5 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.6)))  # New transition
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + \
                        (sig4 - 0.5)**2 + (sig5 - 0.5)**2
        
        # Combined function with significantly modified weighted components
        return 1.2 * fractal + 2.0 * attractor + 0.9 * complexity + 0.8 * multiscale + 0.7 * sharpness