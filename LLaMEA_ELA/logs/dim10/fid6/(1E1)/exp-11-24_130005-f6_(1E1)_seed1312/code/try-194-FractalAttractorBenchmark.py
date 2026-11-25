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
            # Enhanced fractal pattern with higher frequency components and amplitude modulation
            freq = 3.0 + 0.8 * np.sin(x_scaled[i] * 4.0)
            amp = 1.2 + 0.4 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Dynamic attractor fields with position-dependent strength and increased complexity
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths, positions, and interaction terms
            center1 = np.sin(i * 0.6) * 0.9
            center2 = np.cos(i * 0.4) * 0.7
            center3 = np.tan(i * 0.5) * 0.5  # Added tan component for more complex attractor
            strength1 = 1.2 + 0.3 * np.sin(i * 0.8)
            strength2 = 0.9 + 0.2 * np.cos(i * 0.5)
            strength3 = 0.7 + 0.1 * np.sin(i * 0.3)  # Added third attractor
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2) + strength3 * np.exp(-dist3)
        
        # Dimensionally adaptive complexity with recursive interaction terms and increased coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Adaptive interaction based on dimensionality with stronger coupling
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Increased weight effect
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))  # Added Gaussian decay
        
        # Multi-scale fractal component with self-similar structure and added complexity
        multiscale = 0.0
        for scale in [1, 2, 3, 5]:  # Changed scale values and added 5 for more complexity
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             (1.0 + 0.2 * np.sin(scale * x_scaled[i] * 2.0))  # Added modulation
        
        # Sharp transition regions with sigmoidal boundary effects - increased sharpness and added complexity
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points with increased steepness and multiple transitions
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.3)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.3)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-15.0 * (x_scaled[i] - 0.6)))  # Added third transition
            sig4 = 1.0 / (1.0 + np.exp(-15.0 * (x_scaled[i] + 0.6)))  # Added third transition
            
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Additional harmonic complexity term for increased multimodality
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += np.sin(2.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[i]) * \
                       np.exp(-0.5 * x_scaled[i]**2)
        
        # Combined function with modified weighted components for better optimization challenge
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * harmonic