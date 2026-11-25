import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal component with chaotic sine-cosine patterns and higher frequency harmonics
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic pattern with exponentially increasing frequencies and amplitudes
            freq = 3.0 + 2.0 * np.sin(x_scaled[i] * 5.0) + 0.5 * np.cos(x_scaled[i] * 7.0)
            amp = 1.5 + 0.8 * np.sin(x_scaled[i] * 4.0) + 0.3 * np.cos(x_scaled[i] * 6.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3) * \
                      np.exp(-np.abs(x_scaled[i]) * 2.0)
        
        # Multi-center dynamic attractor fields with complex interaction potentials
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with time-varying positions and strengths
            center1 = np.sin(i * 0.8 + x_scaled[i] * 0.5) * 0.9
            center2 = np.cos(i * 0.6 + x_scaled[i] * 0.3) * 0.7
            center3 = np.sin(i * 0.4 + x_scaled[i] * 0.7) * 0.5
            
            strength1 = 1.2 + 0.4 * np.sin(i * 0.9)
            strength2 = 0.9 + 0.3 * np.cos(i * 0.6)
            strength3 = 0.7 + 0.2 * np.sin(i * 0.8)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 1.5) + strength2 * np.exp(-dist2 * 2.0) + strength3 * np.exp(-dist3 * 1.8)
        
        # High-dimensional complex interaction terms with exponentially decaying weights
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Enhanced interaction with exponential decay and dynamic weights
                weight = 2.0 / (1.0 + np.abs(i - j)) * np.exp(-0.1 * np.abs(i - j))
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-np.abs(x_scaled[i] - x_scaled[j]))
        
        # Multi-scale fractal component with exponentially decaying frequencies and complex phase relationships
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Added more scales and increased highest scale
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.4) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(scale * x_scaled[i] * 0.3)
        
        # Ultra-sharp transition regions with multiple sigmoidal boundaries and enhanced non-linearity
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple ultra-sharp transitions with different steepness parameters
            sig1 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.2)))  # Different steepness
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**2
        
        # Additional chaotic noise component with random phase modulation
        chaos_noise = 0.0
        for i in range(self.dim):
            # Random phase modulation and chaotic scaling factors
            phase_mod = np.sin(x_scaled[i] * 10.0 + i * 0.3) * 0.5
            scale_factor = 1.0 + 0.5 * np.sin(x_scaled[i] * 8.0)
            chaos_noise += scale_factor * np.sin(x_scaled[i] * 12.0 + phase_mod) * \
                          np.cos(x_scaled[i] * 9.0 + phase_mod) * \
                          np.exp(-np.abs(x_scaled[i]) * 3.0)
        
        # Combined function with enhanced weighted components and increased complexity
        return 1.0 * fractal + 1.5 * attractor + 0.8 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * chaos_noise