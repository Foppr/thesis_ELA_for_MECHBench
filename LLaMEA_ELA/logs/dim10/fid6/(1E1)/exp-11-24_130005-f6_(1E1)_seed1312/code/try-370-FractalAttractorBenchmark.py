import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal component with increased complexity and modified frequencies
        fractal = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.2 * np.sin(x_scaled[i] * 5.0)
            amp = 2.0 + 0.8 * np.cos(x_scaled[i] * 4.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8)
        
        # Dynamic attractor fields with stronger interactions and modified centers
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.7) * 0.9
            center2 = np.cos(i * 0.5) * 0.8
            center3 = np.sin(i * 0.9) * 0.6
            strength1 = 1.5 + 0.4 * np.sin(i * 1.0)
            strength2 = 1.2 + 0.3 * np.cos(i * 0.6)
            strength3 = 0.9 + 0.2 * np.sin(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Increased dimensional complexity with modified interaction weights and higher-order terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended interaction range
                weight = 3.0 / (1.0 + np.abs(i - j)**1.5)  # Modified weighting scheme
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.7 * (x_scaled[i] + x_scaled[j])**2) * \
                             np.cos(0.5 * (x_scaled[i] - x_scaled[j])**2)
        
        # Multi-scale fractal with additional frequency components and modified amplitude
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6, 8]:  # Extended scale range
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.4 * scale * x_scaled[i]) * \
                             np.cos(0.3 * scale * x_scaled[i])
        
        # Sharper transition regions with enhanced nonlinearity and additional critical points
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i] - 0.3)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i] + 0.3)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i])))  # Additional transition
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.6)))  # New critical point
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**3 + (sig4 - 0.5)**3
        
        # Combined function with reweighted components for better discrimination and bias reduction
        return 1.0 * fractal + 1.8 * attractor + 0.8 * complexity + 0.8 * multiscale + 0.7 * sharpness