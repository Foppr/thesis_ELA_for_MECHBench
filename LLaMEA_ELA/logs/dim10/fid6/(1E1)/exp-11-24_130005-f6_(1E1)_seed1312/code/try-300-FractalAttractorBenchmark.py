import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component using recursive sine-cosine patterns
        fractal = 0.0
        for i in range(self.dim):
            # Recursive fractal pattern with varying frequency and amplitude
            freq = 2.0 + 0.5 * np.sin(x_scaled[i] * 3.0)
            amp = 1.0 + 0.3 * np.cos(x_scaled[i] * 2.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Dynamic attractor fields with position-dependent strength
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths and positions
            center1 = np.sin(i * 0.5) * 0.8
            center2 = np.cos(i * 0.3) * 0.6
            strength1 = 1.0 + 0.2 * np.sin(i * 0.7)
            strength2 = 0.8 + 0.1 * np.cos(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2)
        
        # Dimensionally adaptive complexity with recursive interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction for scalability
                # Adaptive interaction based on dimensionality - modified weights
                weight = 1.5 / (1.0 + np.abs(i - j))  # Increased weight
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j])
        
        # Multi-scale fractal component with self-similar structure - modified frequencies
        multiscale = 0.0
        for scale in [1, 2, 4]:  # Changed scale values and added 4
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.7) * \
                             np.exp(-scale * np.abs(x_scaled[i]))
        
        # Sharp transition regions with sigmoidal boundary effects - increased sharpness
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points - increased steepness
            sig1 = 1.0 / (1.0 + np.exp(-15.0 * (x_scaled[i] - 0.3)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-15.0 * (x_scaled[i] + 0.3)))  # Increased steepness
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2
        
        # Chaotic logistic map component with time-delayed feedback and modified coupling
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with delayed feedback
            r = 3.9 + 0.1 * np.sin(i * 0.8)  # Modified parameter
            x_delay = x_scaled[(i-1) % self.dim] if i > 0 else x_scaled[self.dim-1]
            chaotic += r * x_scaled[i] * (1 - x_scaled[i]) + 0.3 * x_delay * (1 - x_delay)
        
        # Combined function with modified weighted components
        return 0.7 * fractal + 1.3 * attractor + 0.5 * complexity + 0.5 * multiscale + 0.4 * sharpness + 0.3 * chaotic