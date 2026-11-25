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
            freq = 5.2 + 2.1 * np.sin(x_scaled[i] * 8.3) * np.cos(x_scaled[i] * 6.1)
            amp = 2.8 + 1.2 * np.cos(x_scaled[i] * 7.7) * np.sin(x_scaled[i] * 5.3)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.95) * \
                      np.exp(-0.5 * (x_scaled[i]**2))
        
        # Chaotic attractor fields with dynamic centers and exponential decay
        attractor = 0.0
        for i in range(self.dim):
            # Multiple chaotic attractor centers with time-varying positions and strengths
            center1 = np.sin(i * 0.95 + 0.35 * np.sin(x_scaled[i])) * 1.02
            center2 = np.cos(i * 0.75 + 0.45 * np.cos(x_scaled[i])) * 0.88
            center3 = np.sin(i * 1.05 + 0.25 * np.sin(x_scaled[i] * 1.3)) * 0.72
            strength1 = 2.1 + 0.55 * np.sin(i * 1.2 + 0.55 * np.cos(x_scaled[i]))
            strength2 = 1.6 + 0.45 * np.cos(i * 0.8 + 0.65 * np.sin(x_scaled[i]))
            strength3 = 1.2 + 0.35 * np.sin(i * 0.6 + 0.75 * np.cos(x_scaled[i]))
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.9) + strength2 * np.exp(-dist2 * 0.7) + strength3 * np.exp(-dist3 * 1.0)
        
        # Multi-dimensional interaction complexity with exponential weights and chaotic terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+9, self.dim)):  # Increased interaction range
                # Exponentially weighted interactions with chaotic modulation
                weight = 5.2 / (1.0 + np.abs(i - j)**2.1)  # Stronger exponential decay
                phase = np.sin(0.6 * x_scaled[i] + 0.4 * x_scaled[j]) * \
                       np.cos(0.5 * x_scaled[i] - 0.7 * x_scaled[j])
                complexity += weight * phase * \
                             np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2)) * \
                             np.sin(1.4 * (x_scaled[i] + x_scaled[j])**3)
        
        # Multi-scale fractal with chaotic frequency modulation and exponential decay
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]:  # More scales with larger values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.95) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.6 * scale * x_scaled[i] + 0.25 * np.cos(scale * x_scaled[i]))
        
        # Extremely sharp transition regions with enhanced sigmoidal effects and chaotic modulation
        sharpness = 0.0
        for i in range(self.dim):
            # Highly steep sigmoidal transitions with chaotic boundary positions
            pos1 = 0.35 + 0.25 * np.sin(i * 0.75)
            pos2 = -0.35 + 0.25 * np.cos(i * 0.55)
            sig1 = 1.0 / (1.0 + np.exp(-50.0 * (x_scaled[i] - pos1)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-50.0 * (x_scaled[i] + pos2)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-45.0 * x_scaled[i]))  # Additional sharper transition
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + (sig3 - 0.5)**3
        
        # Novel cross-dimensional coupling with higher-order polynomial interactions and chaotic modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Higher-order polynomial coupling with chaotic weights and phase shifts
                weight = 3.0 / (1.0 + np.abs(i - j)**2.5)  # Stronger exponential decay
                phase_shift = np.sin(0.4 * x_scaled[i] + 0.5 * x_scaled[j]) * \
                             np.cos(0.3 * x_scaled[i] - 0.6 * x_scaled[j])
                poly_term = (x_scaled[i]**4 + x_scaled[j]**4) * (x_scaled[i] + x_scaled[j])**3
                cross_coupling += weight * phase_shift * poly_term * \
                                 np.exp(-0.35 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Additional chaotic oscillation with time-varying frequency and amplitude
        oscillation = 0.0
        for i in range(self.dim):
            freq_mod = 3.5 + 2.0 * np.sin(x_scaled[i] * 9.0)
            amp_mod = 2.2 + 0.8 * np.cos(x_scaled[i] * 10.0)
            oscillation += amp_mod * np.sin(freq_mod * x_scaled[i]) * \
                          np.cos(freq_mod * x_scaled[i] * 0.65) * \
                          np.exp(-0.45 * x_scaled[i]**2)
        
        # New mathematical construct: Quaternion-like interaction terms
        quaternion = 0.0
        for i in range(0, self.dim, 4):
            if i+3 < self.dim:
                a, b, c, d = x_scaled[i], x_scaled[i+1], x_scaled[i+2], x_scaled[i+3]
                # Quaternion-like interaction with hyperbolic functions
                quaternion += (np.sinh(a*b) + np.cosh(c*d)) * np.exp(-0.5*(a**2+b**2+c**2+d**2))
        
        # Combined function with highly modified weighted components for maximum algorithm discrimination
        return 1.5 * fractal + 3.0 * attractor + 1.5 * complexity + 1.1 * multiscale + 1.8 * sharpness + 0.9 * cross_coupling + 1.3 * oscillation + 0.7 * quaternion