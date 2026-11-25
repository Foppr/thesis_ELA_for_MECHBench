import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal component with increased frequency modulation and amplitude variation
        fractal = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.2 * np.sin(x_scaled[i] * 5.0)
            amp = 2.0 + 0.6 * np.cos(x_scaled[i] * 4.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8)
        
        # Multi-attractor fields with non-linear interaction and position-dependent strengths
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
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.7) + strength3 * np.exp(-dist3 * 0.9)
        
        # Increased interaction complexity with higher-order terms and modified weights
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                weight = 2.5 / (1.0 + np.abs(i - j)**1.5)  # Modified weight decay
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.6 * (x_scaled[i] + x_scaled[j])**2)
        
        # Multi-scale fractal with modified scaling factors and additional frequency components
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6]:  # Added more scales and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.4 * scale * x_scaled[i])
        
        # Sharper transition regions with modified sigmoidal functions and increased steepness
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i] - 0.3)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i] + 0.3)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i])))  # Modified steepness
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2
        
        # Modified weighted combination to improve algorithm discrimination and reduce bias
        return 0.9 * fractal + 1.7 * attractor + 0.7 * complexity + 0.7 * multiscale + 0.6 * sharpness