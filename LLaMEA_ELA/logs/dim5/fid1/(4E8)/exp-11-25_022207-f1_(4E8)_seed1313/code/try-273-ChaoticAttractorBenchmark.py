import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic attractor with higher frequency interactions
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(7.0 * x_norm[i]) * np.cos(5.0 * x_norm[i]) + 
                       np.cos(9.0 * x_norm[i]) * np.sin(6.0 * x_norm[i]) +
                       0.5 * np.sin(11.0 * x_norm[i]) * np.cos(8.0 * x_norm[i]))
        
        # Multi-scale periodic attractors with dynamic amplitude modulation
        attractor = 0
        freqs = np.linspace(2.0, 12.0, self.dim)
        amps = np.logspace(0.8, 3.0, self.dim)
        for i in range(self.dim):
            attractor += amps[i] * (np.sin(freqs[i] * np.pi * x_norm[i]) * 
                                  np.cos(freqs[i] * np.pi * x_norm[i]) +
                                  0.3 * np.sin(2 * freqs[i] * np.pi * x_norm[i]))
        
        # Asymmetric dynamic coupling with polynomial interaction terms
        coupling = 0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            if diff > 0:
                coupling += 0.7 * (diff**4) * np.sin(3.0 * np.pi * x_norm[i]) + \
                           0.3 * (diff**2) * np.cos(4.0 * np.pi * x_norm[i+1])
            else:
                coupling += 0.4 * (diff**4) * np.cos(3.0 * np.pi * x_norm[i]) + \
                           0.6 * (diff**2) * np.sin(4.0 * np.pi * x_norm[i+1])
        
        # Multi-scale saddle points with varying exponents and exponential decay
        saddle = 0
        for i in range(self.dim):
            if x_norm[i] > 0:
                saddle += (x_norm[i]**5) * np.exp(-0.4 * x_norm[i]**2) + \
                         0.5 * (x_norm[i]**3) * np.exp(-0.2 * x_norm[i]**2)
            else:
                saddle += (x_norm[i]**7) * np.exp(-0.6 * x_norm[i]**2) + \
                         0.3 * (x_norm[i]**4) * np.exp(-0.3 * x_norm[i]**2)
        
        # Multi-scale modulation with complex phase relationships
        modulation = 0
        scales = [0.3, 0.7, 1.2, 1.8, 2.5]
        for s in scales:
            modulation += np.sum(np.sin(s * np.pi * x_norm) * np.cos(s * np.pi * x_norm) + 
                               0.4 * np.sin(2*s * np.pi * x_norm) * np.cos(2*s * np.pi * x_norm))
        
        # Asymmetric noise with dynamic scaling based on landscape curvature
        noise = 0.015 * np.random.randn()
        mean_val = np.mean(x_norm)
        if mean_val > 0:
            noise *= (1.0 + 0.7 * np.abs(mean_val) + 0.2 * np.std(x_norm))
        else:
            noise *= (1.0 - 0.4 * np.abs(mean_val) + 0.3 * np.std(x_norm))
        
        # Combine all components with adaptive weights and additional complexity
        result = 3.0 * chaotic + 2.0 * attractor + 1.0 * coupling + 1.5 * saddle + 0.8 * modulation
        
        return result + noise