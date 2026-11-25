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
            # Enhanced fractal pattern with higher frequency components
            freq = 3.0 + 0.8 * np.sin(x_scaled[i] * 4.0)
            amp = 1.2 + 0.4 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Enhanced attractor fields with dynamic positioning
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with dynamic strengths
            center1 = np.sin(i * 0.6) * 0.9
            center2 = np.cos(i * 0.4) * 0.7
            strength1 = 1.2 + 0.3 * np.sin(i * 0.8)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1 * 1.5) + strength2 * np.exp(-dist2 * 1.2)
        
        # Increased interaction complexity with higher-order terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                # Enhanced weighted interactions with modified exponents
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Increased weight effect
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Enhanced multi-scale fractal component with additional frequencies
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Added scale 5 and increased scale range
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i]) * 0.5)
        
        # Sharper transition regions with enhanced sigmoidal effects
        sharpness = 0.0
        for i in range(self.dim):
            # Enhanced sigmoidal transitions with steeper gradients
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3  # Cubic sharpness
        
        # Additional noise component for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(10.0 * x_scaled[i]) * np.cos(8.0 * x_scaled[i])
        
        # Combined function with adjusted weights for better optimization challenge
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.2 * noise