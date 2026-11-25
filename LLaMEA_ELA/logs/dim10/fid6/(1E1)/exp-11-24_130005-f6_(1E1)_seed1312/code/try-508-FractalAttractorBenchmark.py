import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal component with chaotic sine-cosine patterns and increased complexity
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation with exponential scaling
            freq = 3.8 + 2.1 * np.sin(x_scaled[i] * 6.7) * np.cos(x_scaled[i] * 4.9)
            amp = 2.5 + 0.8 * np.cos(x_scaled[i] * 7.1) * np.sin(x_scaled[i] * 3.8)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.9) * \
                      np.exp(-0.4 * (x_scaled[i]**2))
        
        # Chaotic attractor fields with dynamic centers and exponential decay
        attractor = 0.0
        for i in range(self.dim):
            # Multiple chaotic attractor centers with time-varying positions and strengths
            center1 = np.sin(i * 0.9 + 0.35 * np.sin(x_scaled[i])) * 0.88
            center2 = np.cos(i * 0.7 + 0.45 * np.cos(x_scaled[i])) * 0.75
            center3 = np.sin(i * 1.0 + 0.25 * np.sin(x_scaled[i] * 1.1)) * 0.65
            strength1 = 2.0 + 0.5 * np.sin(i * 1.2 + 0.55 * np.cos(x_scaled[i]))
            strength2 = 1.5 + 0.4 * np.cos(i * 0.8 + 0.65 * np.sin(x_scaled[i]))
            strength3 = 1.1 + 0.3 * np.sin(i * 0.6 + 0.75 * np.cos(x_scaled[i]))
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.75) + strength2 * np.exp(-dist2 * 0.65) + strength3 * np.exp(-dist3 * 0.85)
        
        # Multi-dimensional interaction complexity with exponential weights and chaotic terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased interaction range
                # Exponentially weighted interactions with chaotic modulation
                weight = 4.5 / (1.0 + np.abs(i - j)**2.0)  # Stronger exponential decay
                phase = np.sin(0.6 * x_scaled[i] + 0.35 * x_scaled[j]) * \
                       np.cos(0.45 * x_scaled[i] - 0.55 * x_scaled[j])
                complexity += weight * phase * \
                             np.exp(-0.4 * (x_scaled[i]**2 + x_scaled[j]**2)) * \
                             np.sin(1.3 * (x_scaled[i] + x_scaled[j])**3)
        
        # Multi-scale fractal with chaotic frequency modulation and exponential decay
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 5, 7, 9]:  # More scales with larger values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.85) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.6 * scale * x_scaled[i] + 0.25 * np.cos(scale * x_scaled[i]))
        
        # Extremely sharp transition regions with enhanced sigmoidal effects and chaotic modulation
        sharpness = 0.0
        for i in range(self.dim):
            # Highly steep sigmoidal transitions with chaotic boundary positions
            pos1 = 0.35 + 0.15 * np.sin(i * 0.75)
            pos2 = -0.35 + 0.15 * np.cos(i * 0.55)
            sig1 = 1.0 / (1.0 + np.exp(-50.0 * (x_scaled[i] - pos1)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-50.0 * (x_scaled[i] + pos2)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-45.0 * x_scaled[i]))  # Additional sharper transition
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**3
        
        # Combined function with highly modified weighted components for maximum algorithm discrimination
        return 1.3 * fractal + 2.5 * attractor + 1.2 * complexity + 1.0 * multiscale + 1.5 * sharpness