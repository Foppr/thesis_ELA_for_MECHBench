import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for scalability
        self.chaotic_params = [3.8, 4.0, 3.9, 4.1, 3.7][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Chaotic gradient component with sine-based chaotic maps
        chaotic_grad = 0.0
        for i in range(self.dim):
            # Logistic map-inspired chaotic behavior
            param = self.chaotic_params[i % len(self.chaotic_params)]
            chaotic_grad += np.sin(param * x[i]) * np.cos(param * x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
        
        # Saddle point embedding with hyperbolic tangent components
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(2.5 * x[i]) * np.sin(3.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Multi-scale harmonic modulations with varying frequencies
        harmonics = 0.0
        for i in range(self.dim):
            harmonics += (1.5 * np.sin(7 * x[i]) + 
                         1.0 * np.sin(11 * x[i]) + 
                         0.8 * np.sin(15 * x[i]) + 
                         0.6 * np.sin(19 * x[i]))
        
        # Discontinuous regions with step-like behavior
        discontinuous = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                discontinuous += np.exp(-0.5 * (x[i] + 2)**2) * np.sin(10 * x[i])
            else:
                discontinuous += np.exp(-0.5 * (x[i] - 2)**2) * np.cos(8 * x[i])
        
        # Coupled chaotic fields with asymmetric interactions
        coupled = 0.0
        for i in range(self.dim - 1):
            coupled += 0.7 * np.sin(6 * x[i]) * np.cos(5 * x[i+1]) * \
                      np.exp(-0.1 * (x[i] - x[i+1])**2)
        
        # Ruggedness through fractional Brownian motion-like scaling
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.5 * np.sin(4 * x[i]) * np.cos(3 * x[i]**2) * \
                     np.exp(-0.15 * np.abs(x[i]))
        
        # Asymmetric coupling with exponential decay
        asym_coupling = 0.0
        for i in range(self.dim - 2):
            asym_coupling += 0.6 * np.sin(2.5 * x[i]) * np.exp(-0.3 * x[i+1]**2) * \
                           np.cos(4.0 * x[i+2])
        
        # Global modulation with chaotic sine-cosine patterns
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.8 * np.sin(5.5 * x[i]) * np.cos(3.5 * x[i]) * \
                         np.exp(-0.08 * np.abs(x[i]))
        
        # Add noise-like perturbations for increased ruggedness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.4 * np.sin(60 * x[i]) * np.exp(-0.03 * x[i]**2) + \
                    0.3 * np.cos(50 * x[i]) * np.exp(-0.07 * x[i]**2)
        
        # Combine all components with different weights to create complex landscape
        return base + 1.8 * chaotic_grad + 1.2 * saddle + 0.9 * harmonics + 0.7 * discontinuous + \
               0.6 * coupled + 0.5 * rugged + 0.4 * asym_coupling + 0.3 * global_mod + 0.4 * noise