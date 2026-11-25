import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using recursive sine-cosine patterns with enhanced complexity
        fractal = 0.0
        for i in range(self.dim):
            # Enhanced fractal pattern with higher frequency and amplitude modulation
            freq = 3.5 + 0.9 * np.sin(x_scaled[i] * 4.5)
            amp = 1.6 + 0.5 * np.cos(x_scaled[i] * 3.5)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.75)
        
        # Dynamic attractor fields with position-dependent strength and increased complexity
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths, positions, and interaction
            center1 = np.sin(i * 0.65) * 0.95
            center2 = np.cos(i * 0.45) * 0.75
            center3 = np.sin(i * 0.85) * 0.55
            strength1 = 1.3 + 0.35 * np.sin(i * 0.95)
            strength2 = 1.0 + 0.25 * np.cos(i * 0.55)
            strength3 = 0.8 + 0.15 * np.sin(i * 0.35)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Dimensionally adaptive complexity with recursive interaction terms and modified weights
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                # Adaptive interaction based on dimensionality - increased weight and complexity
                weight = 2.5 / (1.0 + np.abs(i - j))  # Further increased weight
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.6 * (x_scaled[i] + x_scaled[j])**2)
        
        # Multi-scale fractal component with self-similar structure and modified frequencies
        multiscale = 0.0
        for scale in [1, 2, 3, 5, 7]:  # Added more scales and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.85) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.35 * scale * x_scaled[i])
        
        # Sharp transition regions with sigmoidal boundary effects - further increased sharpness
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points - even higher steepness
            sig1 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-30.0 * (x_scaled[i])))  # Additional transition
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2
        
        # Combined function with modified weighted components for better algorithm discrimination
        return 0.9 * fractal + 1.6 * attractor + 0.7 * complexity + 0.7 * multiscale + 0.6 * sharpness