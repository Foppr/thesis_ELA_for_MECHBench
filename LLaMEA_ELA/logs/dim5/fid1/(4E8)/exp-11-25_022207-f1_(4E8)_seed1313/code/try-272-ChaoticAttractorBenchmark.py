import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic attractor component with sine and cosine interactions
        chaotic = 0
        for i in range(self.dim):
            # Slightly modified chaotic terms with altered coefficients
            chaotic += 0.8 * np.sin(3.2 * x_norm[i]) * np.cos(1.8 * x_norm[i]) + \
                       1.2 * np.cos(4.8 * x_norm[i]) * np.sin(3.5 * x_norm[i])
        
        # Periodic attractor terms with varying frequencies and amplitudes
        attractor = 0
        freqs = np.linspace(1.2, 7.8, self.dim)
        amps = np.logspace(0.6, 2.3, self.dim)
        for i in range(self.dim):
            attractor += amps[i] * np.sin(freqs[i] * np.pi * x_norm[i]) * \
                        np.cos(freqs[i] * np.pi * x_norm[i])
        
        # Dynamic coupling terms with asymmetric interaction
        coupling = 0
        for i in range(self.dim - 1):
            # Modified coupling with different weights and additional nonlinear term
            diff = x_norm[i] - x_norm[i+1]
            if diff > 0:
                coupling += 0.4 * (diff**3) * np.sin(2.5 * np.pi * x_norm[i]) + \
                           0.1 * diff**5
            else:
                coupling += 0.25 * (diff**3) * np.cos(1.5 * np.pi * x_norm[i+1]) - \
                           0.05 * diff**4
        
        # Saddle point perturbations with varying curvature
        saddle = 0
        for i in range(self.dim):
            # Modified saddle points with different exponents and decay rates
            if x_norm[i] > 0:
                saddle += 1.2 * (x_norm[i]**3.8) * np.exp(-0.4 * x_norm[i]**2)
            else:
                saddle += 0.8 * (x_norm[i]**5.5) * np.exp(-0.25 * x_norm[i]**2)
        
        # Multi-scale periodic modulation with dynamic phase shifts
        modulation = 0
        scales = [0.4, 1.2, 1.8, 2.2]
        for s in scales:
            modulation += np.sum(0.7 * np.sin(s * np.pi * x_norm) * np.cos(s * np.pi * x_norm))
        
        # Additional asymmetric noise injection
        noise = 0.015 * np.random.randn()
        if np.mean(x_norm) > 0:
            noise *= (1.0 + 0.4 * np.abs(np.mean(x_norm)))
        else:
            noise *= (1.0 - 0.2 * np.abs(np.mean(x_norm)))
        
        # Combine all components with updated weights
        result = 1.8 * chaotic + 1.3 * attractor + 0.9 * coupling + 1.1 * saddle + 0.7 * modulation
        
        return result + noise