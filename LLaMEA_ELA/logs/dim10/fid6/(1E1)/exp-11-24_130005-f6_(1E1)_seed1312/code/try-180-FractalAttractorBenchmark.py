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
            # Enhanced fractal pattern with increased frequency modulation and amplitude
            freq = 3.0 + 0.8 * np.sin(x_scaled[i] * 4.0)
            amp = 1.5 + 0.4 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Enhanced attractor fields with dynamic positioning and multi-center interactions
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths and dynamic positions
            center1 = np.sin(i * 0.6) * 0.9
            center2 = np.cos(i * 0.4) * 0.7
            center3 = np.tan(i * 0.3) * 0.5  # Added tan for more complex positioning
            
            strength1 = 1.2 + 0.3 * np.sin(i * 0.8)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.5)
            strength3 = 0.7 + 0.1 * np.sin(i * 0.6)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Enhanced dimensionally adaptive complexity with extended interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                # Adaptive interaction based on dimensionality - modified weights
                weight = 2.0 / (1.0 + np.abs(i - j))  # Increased weight
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.5 * (x_scaled[i] + x_scaled[j]))  # Added sine modulation
        
        # Enhanced multi-scale fractal component with additional frequency harmonics
        multiscale = 0.0
        for scale in [1, 2, 3, 4]:  # Extended scale values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * x_scaled[i] * 0.3)  # Added harmonic component
        
        # Enhanced sharp transition regions with modified sigmoidal boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points - increased steepness and added asymmetry
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.3)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.3)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] - 0.6)))  # Additional transition
            
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2
        
        # Combined function with modified weighted components for better algorithm discrimination
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.6 * multiscale + 0.5 * sharpness