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
            # Use a combination of sine and cosine to create chaotic behavior
            chaotic += np.sin(3.0 * x_norm[i]) * np.cos(2.0 * x_norm[i]) + \
                       np.cos(5.0 * x_norm[i]) * np.sin(4.0 * x_norm[i])
        
        # Periodic attractor terms with varying frequencies and amplitudes
        attractor = 0
        freqs = np.linspace(1.0, 8.0, self.dim)
        amps = np.logspace(0.5, 2.5, self.dim)
        for i in range(self.dim):
            attractor += amps[i] * np.sin(freqs[i] * np.pi * x_norm[i]) * \
                        np.cos(freqs[i] * np.pi * x_norm[i])
        
        # Dynamic coupling terms with asymmetric interaction
        coupling = 0
        for i in range(self.dim - 1):
            # Asymmetric coupling: different weights for positive and negative differences
            diff = x_norm[i] - x_norm[i+1]
            if diff > 0:
                coupling += 0.5 * (diff**3) * np.sin(2.0 * np.pi * x_norm[i])
            else:
                coupling += 0.3 * (diff**3) * np.cos(2.0 * np.pi * x_norm[i+1])
        
        # Saddle point perturbations with varying curvature
        saddle = 0
        for i in range(self.dim):
            # Create asymmetric saddle points with different exponents
            if x_norm[i] > 0:
                saddle += (x_norm[i]**4) * np.exp(-0.5 * x_norm[i]**2)
            else:
                saddle += (x_norm[i]**6) * np.exp(-0.3 * x_norm[i]**2)
        
        # Multi-scale periodic modulation with dynamic phase shifts
        modulation = 0
        scales = [0.5, 1.0, 1.5, 2.0]
        for s in scales:
            modulation += np.sum(np.sin(s * np.pi * x_norm) * np.cos(s * np.pi * x_norm))
        
        # Asymmetric noise injection to increase robustness
        noise = 0.01 * np.random.randn()
        if np.mean(x_norm) > 0:
            noise *= (1.0 + 0.5 * np.abs(np.mean(x_norm)))
        else:
            noise *= (1.0 - 0.3 * np.abs(np.mean(x_norm)))
        
        # Combine all components with adaptive weights
        result = 2.0 * chaotic + 1.5 * attractor + 0.8 * coupling + 1.2 * saddle + 0.6 * modulation
        
        return result + noise