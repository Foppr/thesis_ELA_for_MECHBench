import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with enhanced complexity and higher frequency modulation
        fractal = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.2 * np.sin(x_scaled[i] * 5.0)
            amp = 1.8 + 0.6 * np.cos(x_scaled[i] * 4.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8)
        
        # Dynamic attractor fields with increased complexity and position-dependent strength
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.7) * 0.9
            center2 = np.cos(i * 0.5) * 0.8
            center3 = np.sin(i * 0.9) * 0.6
            strength1 = 1.4 + 0.4 * np.sin(i * 1.0)
            strength2 = 1.1 + 0.3 * np.cos(i * 0.6)
            strength3 = 0.9 + 0.2 * np.sin(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Dimensionally adaptive complexity with increased interaction range and modified weights
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased interaction range
                weight = 3.0 / (1.0 + np.abs(i - j)**1.5)  # Modified weight function
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.7 * (x_scaled[i] + x_scaled[j])**2)
        
        # Multi-scale fractal component with additional scales and modified interaction
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6, 8]:  # Added more scales and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.4 * scale * x_scaled[i])
        
        # Sharp transition regions with enhanced sigmoidal boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            # Enhanced sigmoidal transitions with increased steepness and additional points
            sig1 = 1.0 / (1.0 + np.exp(-40.0 * (x_scaled[i] - 0.35)))
            sig2 = 1.0 / (1.0 + np.exp(-40.0 * (x_scaled[i] + 0.35)))
            sig3 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i])))
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.6)))
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Combined function with modified weighted components
        return 0.9 * fractal + 1.8 * attractor + 0.8 * complexity + 0.7 * multiscale + 0.7 * sharpness