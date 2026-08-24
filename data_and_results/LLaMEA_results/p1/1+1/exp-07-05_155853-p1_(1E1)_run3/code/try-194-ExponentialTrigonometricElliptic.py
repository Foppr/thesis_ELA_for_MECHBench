import numpy as np

class ExponentialTrigonometricElliptic:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with adaptive rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.5 + 0.5 * np.sin(i * 0.6)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.cos(rate * x[i]**2)
        
        # Trigonometric wave interactions with dynamic amplitudes
        wave_interaction = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.4)
            wave_interaction += amp * np.sin(x[i]) * np.cos(x[i]**2) + 0.3 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Adaptive elliptic contours with varying eccentricity
        elliptic = 0
        for i in range(self.dim - 1):
            eccentricity = 0.3 + 0.7 * np.abs(np.sin(i * 0.5))
            elliptic += (x[i]**2 / (1.0 + eccentricity)) + (x[i+1]**2 / (1.0 + 1.0 / (1.0 + eccentricity)))
        
        # Dynamic conditioning with chaotic scaling factors
        conditioning = 0
        for i in range(self.dim):
            scale = 1.0 + 2.0 * np.abs(np.sin(i * 0.3))
            conditioning += scale * x[i]**4
        
        # Saddle-point structures with alternating signs
        saddle = 0
        for i in range(self.dim - 1):
            sign = (-1)**i
            saddle += sign * x[i] * x[i+1]
        
        # High-frequency oscillation with amplitude modulation
        high_freq = 0
        for i in range(self.dim):
            amp = 0.5 + 0.5 * np.cos(i * 0.7)
            high_freq += amp * np.sin(10.0 * x[i]) * np.cos(15.0 * x[i])
        
        # Cross-dimensional coupling with exponential weights
        cross_coupling = 0
        for i in range(self.dim - 1):
            weight = np.exp(-0.1 * np.abs(x[i]))
            cross_coupling += weight * (x[i]**2 + x[i+1]**2)
        
        # Multi-scale harmonic components with varying frequencies
        multi_harmonic = 0
        for i in range(self.dim):
            freq1 = 1.0 + 0.5 * np.sin(i * 0.8)
            freq2 = 2.0 + 0.3 * np.cos(i * 0.6)
            multi_harmonic += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        
        # Asymmetric penalty terms for conditioning
        penalty = 0
        for i in range(self.dim):
            if x[i] > 0:
                penalty += 0.1 * x[i]**3
            else:
                penalty += 0.2 * x[i]**3
        
        # Combine all components with optimized weights
        return 0.8 * exp_decay + 0.6 * wave_interaction + 0.4 * elliptic + 0.3 * conditioning + 0.2 * saddle + 0.15 * high_freq + 0.1 * cross_coupling + 0.05 * multi_harmonic + 0.03 * penalty