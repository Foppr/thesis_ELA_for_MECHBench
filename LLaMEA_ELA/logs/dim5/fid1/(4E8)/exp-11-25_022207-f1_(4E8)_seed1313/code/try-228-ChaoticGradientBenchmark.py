import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component with logistic map modulation
        chaotic = np.sum(np.sin(2.0 * np.pi * x_norm) * 
                        np.cos(3.0 * np.pi * x_norm) * 
                        np.exp(-0.5 * np.sum(x_norm**2)) * 
                        np.tan(0.7 * x_norm))
        
        # Polynomial coupling with chaotic modulation
        poly_coupling = 0
        for i in range(self.dim - 1):
            poly_coupling += (x_norm[i]**3.5 + x_norm[i+1]**3.5)**2 * \
                           np.sin(2.5 * np.pi * (x_norm[i] + x_norm[i+1])) * \
                           np.exp(-0.3 * (x_norm[i] - x_norm[i+1])**2)
        
        # Saddle-point structure with dynamic scaling
        saddle = 0
        for i in range(self.dim):
            saddle += (x_norm[i]**2 - 0.5)**3.2 * np.exp(-0.4 * x_norm[i]**2)
            
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        sinusoidal = 0
        frequencies = [1.2, 2.8, 4.1]
        amplitudes = [1.5, 0.8, 0.3]
        for freq, amp in zip(frequencies, amplitudes):
            sinusoidal += amp * np.sin(freq * np.pi * x_norm) * \
                         np.cos(freq * np.pi * x_norm) * \
                         np.exp(-0.2 * np.sum(x_norm**2))
        
        # Gradient-asymmetric component with exponential decay
        asym = np.sum(np.abs(x_norm)**1.7 * np.exp(-0.3 * x_norm**2) * 
                     np.sin(3.2 * np.pi * x_norm) * 
                     np.cos(1.8 * np.pi * x_norm))
        
        # Embedded noise structure with chaotic perturbation
        noise = 0.05 * np.sum(np.sin(5.0 * x_norm) * np.cos(4.0 * x_norm) * 
                            np.exp(-0.1 * np.abs(x_norm)) * 
                            (1.0 + 0.1 * np.random.rand()))
        
        # Combine all components
        result = chaotic + poly_coupling + saddle + sinusoidal + asym + noise
        
        return result