import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using chaotic sine-cosine patterns with exponential growth
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic fractal pattern with exponentially increasing frequency and amplitude
            freq = 2.0 * np.exp(0.3 * np.abs(x_scaled[i]))
            amp = 1.0 + 0.5 * np.exp(0.2 * np.abs(x_scaled[i]))
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Dynamic attractor fields with chaotic position-dependent strength
        attractor = 0.0
        for i in range(self.dim):
            # Multiple chaotic attractor centers with exponential strength variations
            center1 = np.sin(i * 0.5) * 0.8 * np.exp(-0.1 * i)
            center2 = np.cos(i * 0.3) * 0.6 * np.exp(-0.05 * i)
            strength1 = 1.0 + 0.3 * np.sin(i * 0.7) * np.exp(0.1 * i)
            strength2 = 0.8 + 0.2 * np.cos(i * 0.4) * np.exp(0.05 * i)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2)
        
        # Highly complex dimensional adaptive complexity with exponential interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Exponential interaction based on dimensionality - highly modified weights
                weight = 2.0 / (1.0 + np.exp(0.5 * np.abs(i - j)))  # Exponential decay weights
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.1 * (i + j))  # Dimensional decay
        
        # Multi-scale fractal component with chaotic self-similar structure and exponential scaling
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Increased scale values and added 6
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.7) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.5 * scale * x_scaled[i])
        
        # Extremely sharp transition regions with chaotic sigmoidal boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            # Chaotic sigmoidal transition near critical points - extremely increased steepness
            sig1 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.3)))  # Very high steepness
            sig2 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.3)))  # Very high steepness
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3  # Cubic sharpness
        
        # Add chaotic noise component to increase landscape complexity
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(10 * x_scaled[i]) * np.cos(7 * x_scaled[i]) * \
                    np.exp(-0.5 * x_scaled[i]**2)
        
        # Combined function with highly modified weighted components and chaotic additions
        return 1.2 * fractal + 1.8 * attractor + 0.8 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * noise