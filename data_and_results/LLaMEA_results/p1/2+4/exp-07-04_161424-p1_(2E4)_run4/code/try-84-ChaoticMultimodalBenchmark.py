import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity and phase shifts
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 30):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute trigonometric coupling coefficients
        self.coupling_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
        # Precompute adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with dynamic phase shifts and chaotic scaling
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            phase_shift = np.sin(self.logistic_seq[i] * np.pi * 2) * 0.5
            weight = np.abs(np.cos(self.logistic_seq[i] * np.pi)) + 0.2
            rbfs[i] = weight * np.exp(-dist / (2 * (0.02 + phase_shift)**2))
        
        # Trigonometric coupling with chaotic modulation
        coupling = np.sum(np.sin(self.coupling_coeffs * x_norm + self.logistic_seq) * 
                         np.cos(self.coupling_coeffs * x_norm + self.logistic_seq * 2))
        
        # Adaptive noise with dynamic scaling based on conditioning
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.1, 2.0, self.dim) * self.conditioning_factors)
        
        # Higher-order polynomial interactions with dynamic exponents
        poly_interaction = np.sum(self.coupling_coeffs * (x_norm**5 + 0.3 * x_norm**7 + 0.05 * x_norm**9))
        
        # Add sharp transition zones with dynamic thresholds
        transitions = np.sum(np.abs(np.cos(x_norm * np.pi * 1.5)) > 0.8)
        
        # Add dynamic conditioning factor that changes based on input magnitude
        conditioning = np.sum(self.conditioning_factors * (x_norm**2 + 0.1 * x_norm**4))
        
        # Combine all components with dynamic weights
        total = 0.25 * np.sum(rbfs) + 0.25 * coupling + 0.2 * noise + 0.2 * poly_interaction + 0.1 * transitions + 0.05 * conditioning
        
        # Add a global scaling factor with chaotic modulation
        chaotic_scale = 1 + 0.8 * np.sin(np.sum(x_norm**3) * self.logistic_seq[0])
        return total * chaotic_scale