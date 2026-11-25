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
            freq = 4.5 + 2.0 * np.sin(x_scaled[i] * 7.5) * np.cos(x_scaled[i] * 5.3)
            amp = 2.3 + 1.0 * np.cos(x_scaled[i] * 6.9) * np.sin(x_scaled[i] * 4.5)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.87) * \
                      np.exp(-0.5 * (x_scaled[i]**2))
        
        # Chaotic attractor fields with dynamic centers and exponential decay
        attractor = 0.0
        for i in range(self.dim):
            # Multiple chaotic attractor centers with time-varying positions and strengths
            center1 = np.sin(i * 0.87 + 0.32 * np.sin(x_scaled[i])) * 0.94
            center2 = np.cos(i * 0.67 + 0.42 * np.cos(x_scaled[i])) * 0.80
            center3 = np.sin(i * 0.97 + 0.22 * np.sin(x_scaled[i] * 1.25)) * 0.64
            strength1 = 1.9 + 0.47 * np.sin(i * 1.12 + 0.52 * np.cos(x_scaled[i]))
            strength2 = 1.4 + 0.37 * np.cos(i * 0.72 + 0.62 * np.sin(x_scaled[i]))
            strength3 = 1.0 + 0.27 * np.sin(i * 0.52 + 0.72 * np.cos(x_scaled[i]))
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.82) + strength2 * np.exp(-dist2 * 0.62) + strength3 * np.exp(-dist3 * 0.92)
        
        # Multi-dimensional interaction complexity with exponential weights and chaotic terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):  # Increased interaction range
                # Exponentially weighted interactions with chaotic modulation
                weight = 4.5 / (1.0 + np.abs(i - j)**1.9)  # Stronger exponential decay
                phase = np.sin(0.52 * x_scaled[i] + 0.32 * x_scaled[j]) * \
                       np.cos(0.42 * x_scaled[i] - 0.62 * x_scaled[j])
                complexity += weight * phase * \
                             np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2)) * \
                             np.sin(1.25 * (x_scaled[i] + x_scaled[j])**3)
        
        # Multi-scale fractal with chaotic frequency modulation and exponential decay
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6, 8, 10, 12]:  # More scales with larger values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.92) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.52 * scale * x_scaled[i] + 0.22 * np.cos(scale * x_scaled[i]))
        
        # Extremely sharp transition regions with enhanced sigmoidal effects and chaotic modulation
        sharpness = 0.0
        for i in range(self.dim):
            # Highly steep sigmoidal transitions with chaotic boundary positions
            pos1 = 0.32 + 0.22 * np.sin(i * 0.72)
            pos2 = -0.32 + 0.22 * np.cos(i * 0.52)
            sig1 = 1.0 / (1.0 + np.exp(-50.0 * (x_scaled[i] - pos1)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-50.0 * (x_scaled[i] + pos2)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-45.0 * x_scaled[i]))  # Additional sharper transition
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**3
        
        # Novel cross-dimensional coupling with higher-order polynomial interactions and chaotic modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Higher-order polynomial coupling with chaotic weights and phase shifts
                weight = 2.7 / (1.0 + np.abs(i - j)**2.3)  # Stronger exponential decay
                phase_shift = np.sin(0.32 * x_scaled[i] + 0.42 * x_scaled[j]) * \
                             np.cos(0.22 * x_scaled[i] - 0.52 * x_scaled[j])
                poly_term = (x_scaled[i]**3 + x_scaled[j]**3) * (x_scaled[i] + x_scaled[j])**2
                cross_coupling += weight * phase_shift * poly_term * \
                                 np.exp(-0.32 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Additional chaotic oscillation with time-varying frequency and amplitude
        oscillation = 0.0
        for i in range(self.dim):
            freq_mod = 3.2 + 1.6 * np.sin(x_scaled[i] * 8.2)
            amp_mod = 1.9 + 0.75 * np.cos(x_scaled[i] * 9.2)
            oscillation += amp_mod * np.sin(freq_mod * x_scaled[i]) * \
                          np.cos(freq_mod * x_scaled[i] * 0.62) * \
                          np.exp(-0.42 * x_scaled[i]**2)
        
        # Combined function with highly modified weighted components for maximum algorithm discrimination
        return 1.35 * fractal + 2.6 * attractor + 1.25 * complexity + 0.95 * multiscale + 1.65 * sharpness + 0.85 * cross_coupling + 1.15 * oscillation