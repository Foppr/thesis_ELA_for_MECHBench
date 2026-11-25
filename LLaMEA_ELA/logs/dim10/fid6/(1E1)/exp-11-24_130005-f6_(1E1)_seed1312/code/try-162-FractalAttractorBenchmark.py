import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with enhanced recursive patterns and higher frequency interactions
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 0.8 * np.sin(x_scaled[i] * 4.0)
            amp = 1.5 + 0.4 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * \
                      np.sin(2.0 * x_scaled[i] * freq) * np.cos(1.5 * x_scaled[i] * freq)
        
        # Enhanced attractor fields with dynamic positioning and multi-scale influence
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8) * 1.2
            center2 = np.cos(i * 0.5) * 0.9
            center3 = np.tan(i * 0.3) * 0.7
            
            strength1 = 1.5 + 0.3 * np.sin(i * 0.9)
            strength2 = 1.2 + 0.2 * np.cos(i * 0.6)
            strength3 = 0.9 + 0.1 * np.sin(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.7) + strength3 * np.exp(-dist3 * 0.3)
        
        # Multi-dimensional interaction terms with chaotic coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 2.0 / (1.0 + np.abs(i - j) * 0.5)
                interaction = np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
                chaos_factor = np.sin(x_scaled[i] * x_scaled[j] * 2.0) * np.cos(x_scaled[i] * x_scaled[j] * 1.5)
                complexity += weight * interaction * (1.0 + 0.3 * chaos_factor)
        
        # Multi-scale fractal with chaotic frequency modulation and enhanced self-similarity
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Added scale 6 and modified others
            for i in range(self.dim):
                freq_mod = 1.0 + 0.5 * np.sin(i * 0.7)
                multiscale += np.sin(scale * x_scaled[i] * freq_mod) * \
                             np.cos(scale * x_scaled[i] * 0.8 * freq_mod) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * x_scaled[i] * 0.3)
        
        # Chaotic transition regions with multiple sigmoidal boundaries and fractal modulation
        sharpness = 0.0
        for i in range(self.dim):
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] - 0.2)))  # New boundary
            sig4 = 1.0 / (1.0 + np.exp(-12.0 * (x_scaled[i] + 0.2)))  # New boundary
            
            chaotic_mod = np.sin(x_scaled[i] * 10.0) * np.cos(x_scaled[i] * 7.0)
            sharpness += ((sig1 - 0.5)**2 + (sig2 - 0.5)**2 + 
                         (sig3 - 0.5)**2 + (sig4 - 0.5)**2) * (1.0 + 0.2 * chaotic_mod)
        
        # Add a novel chaotic harmonic component
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                harmonic += np.sin(x_scaled[i] * x_scaled[j] * 5.0) * \
                           np.cos(x_scaled[i] + x_scaled[j]) * \
                           np.exp(-np.abs(x_scaled[i] - x_scaled[j]))
        
        # Combined function with new weighted components and chaotic amplification
        return (0.8 * fractal + 1.5 * attractor + 0.7 * complexity + 
                0.6 * multiscale + 0.5 * sharpness + 0.3 * harmonic)